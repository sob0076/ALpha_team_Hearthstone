import pygame
from src.core.interfaces import Component
from src.engine.card import Minion

# --- کانفیگ و تنظیمات ظاهری کارت ---
CARD_WIDTH, CARD_HEIGHT = 120, 180
FONT_SIZE = 24
FONT_COLOR = (255, 255, 255)
HEALTH_COLOR_NORMAL = (255, 255, 255) # رنگ عادی جان
HEALTH_COLOR_DAMAGED = (255, 80, 80) # رنگ قرمز برای جان آسیب‌دیده
BACKGROUND_COLOR = (40, 40, 60) # رنگ پس‌زمینه کارت اگر تصویر نبود
DEAD_OVERLAY_COLOR = (50, 50, 50, 180) # رنگ نیمه‌شفاف خاکستری برای حالت مرگ

class CardView(Component):
    """
    وظیفه این کلاس، نمایش گرافیکی یک کارت Minion است.
    این کلاس هیچ منطقی از بازی را تغییر نمی‌دهد و فقط اطلاعات
    دریافتی از engine.card.Minion را به تصویر می‌کشد.
    """
    def __init__(self, minion: Minion, position=(0, 0)):
        """
        یک نمونه Minion و موقعیت اولیه کارت را دریافت می‌کند.
        """
        self.minion = minion
        self.position = position
        
        # ساخت یک سطح (Surface) برای کارت که تمام اجزا روی آن کشیده می‌شوند
        self.surface = pygame.Surface((CARD_WIDTH, CARD_HEIGHT), pygame.SRCALPHA)
        
        # بارگذاری و تنظیم فونت برای نمایش Attack و Health
        try:
            self.font = pygame.font.Font(None, FONT_SIZE) # استفاده از فونت پیش‌فرض پایگیم
        except Exception:
            self.font = pygame.font.SysFont('Arial', FONT_SIZE)

        # بارگذاری تصویر کارت (اگر وجود داشته باشد)
        self.card_image = None
        try:
            # تصویر را بارگذاری و به اندازه کارت تغییر سایز می‌دهد
            self.card_image = pygame.image.load(self.minion.image_path).convert_alpha()
            self.card_image = pygame.transform.scale(self.card_image, (CARD_WIDTH, CARD_HEIGHT))
        except (pygame.error, FileNotFoundError) as e:
            print(f"Warning: Could not load image for {self.minion.name} from '{self.minion.image_path}'. Error: {e}")

        # سطح نیمه‌شفاف برای حالت مرگ
        self.dead_overlay = pygame.Surface((CARD_WIDTH, CARD_HEIGHT), pygame.SRCALPHA)
        self.dead_overlay.fill(DEAD_OVERLAY_COLOR)

    def handle_event(self, event):
        """ در این فاز، کارت‌ها به هیچ رویدادی (مثل کلیک) واکنش نشان نمی‌دهند. """
        pass

    def update(self, dt):
        """ در این فاز، کارت‌ها انیمیشن یا آپدیت زمانی ندارند. """
        pass

    def render(self, parent_surface: pygame.Surface):
        """
        کارت را بر روی سطح والد (مثلاً صفحه بازی) رسم می‌کند.
        این متد وضعیت Minion را بررسی کرده و ظاهر کارت را بر اساس آن تنظیم می‌کند.
        """
        # 1. رسم پس‌زمینه یا تصویر کارت
        if self.card_image:
            self.surface.blit(self.card_image, (0, 0))
        else:
            # اگر تصویری وجود نداشت، یک پس‌زمینه رنگی ساده رسم کن
            self.surface.fill(BACKGROUND_COLOR)
            pygame.draw.rect(self.surface, (100, 100, 120), self.surface.get_rect(), 3) # حاشیه
