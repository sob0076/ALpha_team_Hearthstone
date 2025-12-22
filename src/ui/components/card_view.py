import pygame
from src.core.interfaces import Component
from src.engine.card import Minion

# تنظیمات رنگ (RGB)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 80, 80)
GREEN = (80, 255, 80)
YELLOW = (255, 215, 0)
HOVER_COLOR = (255, 255, 255) # رنگ کادر دور کارت موقع هاور

class CardView(Component):
    def __init__(self, card_model, x, y, scale=0.7):
        self.model = card_model
        self.rect = pygame.Rect(x, y, 0, 0)
        self.scale = scale
        self.is_hovered = False  # وضعیت موس
        
        # 1. لود کردن تصویر
        try:
            original = pygame.image.load(self.model.image_path).convert_alpha()
            width = int(original.get_width() * scale)
            height = int(original.get_height() * scale)
            self.image = pygame.transform.smoothscale(original, (width, height))
            self.rect.width = width
            self.rect.height = height
        except Exception as e:
            print(f"Texture Error: {e}")
            self.image = pygame.Surface((int(200*scale), int(300*scale)))
            self.image.fill((50, 50, 50))
            self.rect.width = self.image.get_width()
            self.rect.height = self.image.get_height()

        # 2. ساخت لایه مرگ (Dead Overlay)
        # یک صفحه هم‌اندازه کارت که سیاه و نیمه‌شفاف است
        self.dead_surface = pygame.Surface((self.rect.width, self.rect.height), pygame.SRCALPHA)
        self.dead_surface.fill((20, 20, 20, 200)) # رنگ سیاه با شفافیت 200 (از 255)

        # 3. فونت
        self.font = pygame.font.SysFont("Arial", int(38 * scale), bold=True)

    def handle_event(self, event):
        """مدیریت رویدادهای مربوط به کارت (مثل هاور شدن موس)"""
        if event.type == pygame.MOUSEMOTION:
            # اگر موس روی مستطیل کارت بود، هاور فعال شود
            if self.rect.collidepoint(event.pos):
                self.is_hovered = True
            else:
                self.is_hovered = False

    def update(self, dt):
        """آپدیت وضعیت (فعلاً انیمیشن نداریم)"""
        pass

    def render(self, surface):
        """رسم نهایی کارت"""
        
        # 1. رسم خود کارت
        surface.blit(self.image, self.rect)

        # 2. رسم اعداد (اگر زنده است یا حتی اگر مرده، اعداد را زیر سایه نشان بده)
        if isinstance(self.model, Minion):
            self._draw_stats(surface)

        # 3. اعمال افکت مرگ (اگر مرده است)
        if isinstance(self.model, Minion) and not self.model.is_alive:
            # کشیدن لایه تیره روی کل کارت
            surface.blit(self.dead_surface, self.rect)
            
            # (اختیاری) نوشتن متن Dead روی کارت برای وضوح بیشتر
            # dead_text = self.font.render("DEAD", True, RED)
            # text_rect = dead_text.get_rect(center=self.rect.center)
            # surface.blit(dead_text, text_rect)

        # 4. افکت هاور (اگر زنده است و موس رویش است)
        # معمولاً کارت مرده تعامل ندارد، پس شرط is_alive را هم اضافه می‌کنیم
        if self.is_hovered and self.model.is_alive:
            # کشیدن یک کادر سفید دور کارت با ضخامت 3
            pygame.draw.rect(surface, HOVER_COLOR, self.rect, 4, border_radius=5)

    def _draw_stats(self, surface):
        offset_x = 35 * self.scale
        offset_y = 45 * self.scale 

        attack_pos = (self.rect.left + offset_x, self.rect.bottom - offset_y)
        health_pos = (self.rect.right - offset_x, self.rect.bottom - offset_y)
        
        # تعیین رنگ هوشمند جان
        health_display = max(0, self.model.health)
        health_color = WHITE
        
        if health_display < self.model.max_health:
            health_color = RED
        elif health_display > self.model.max_health:
            health_color = GREEN

        self._render_bubble(surface, str(self.model.attack), attack_pos, YELLOW)
        self._render_bubble(surface, str(health_display), health_pos, health_color)

    def _render_bubble(self, surface, text, center, text_color):
        radius = int(28 * self.scale)
        # دایره سیاه توپر
        pygame.draw.circle(surface, BLACK, center, radius)
        # قاب سفید دور دایره
        pygame.draw.circle(surface, WHITE, center, radius, 2)
        # متن
        text_surf = self.font.render(text, True, text_color)
        text_rect = text_surf.get_rect(center=center)
        surface.blit(text_surf, text_rect)