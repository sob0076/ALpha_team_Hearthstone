import pygame
from typing import List
from src.core.interfaces import Component
from src.engine.card import Minion
from src.ui.components.card_view import CardView, CARD_WIDTH, CARD_HEIGHT

# --- کانفیگ و تنظیمات ظاهری Board ---
BOARD_MAX_MINIONS = 7
CARD_SPACING = 15 # فاصله بین کارت‌ها
BOARD_BG_COLOR = (20, 30, 40, 150) # رنگ پس‌زمینه نیمه‌شفاف برای Board

class BoardView(Component):
    """
    وظیفه این کلاس، نمایش گرافیکی مجموعه‌ای از کارت‌های Minion
    در یک ردیف (صفحه بازی) است.
    """
    def __init__(self, position=(0, 0), size=(0,0)):
        """
        موقعیت اولیه (گوشه بالا-چپ) و اندازه Board را دریافت می‌کند.
        """
        self.position = position
        self.size = size
        
        # لیستی برای نگهداری نمونه‌های CardView
        self.card_views: List[CardView] = []
        
        # یک سطح (Surface) برای خود Board تا اجزا را روی آن بکشد
        self.surface = pygame.Surface(self.size, pygame.SRCALPHA)
        self.surface.fill(BOARD_BG_COLOR)
        
        # محاسبه جایگاه‌ها (slots) برای کارت‌ها
        self._calculate_slots()

    def _calculate_slots(self):
        """
        موقعیت دقیق هر یک از ۷ جایگاه کارت را محاسبه می‌کند.
        این متد کارت‌ها را در مرکز افقی Board قرار می‌دهد.
        """
        self.slots_positions = []
        total_cards_width = (BOARD_MAX_MINIONS * CARD_WIDTH) + ((BOARD_MAX_MINIONS - 1) * CARD_SPACING)
        
        # محاسبه نقطه شروع اولین کارت برای وسط‌چین کردن
        start_x = (self.size[0] - total_cards_width) / 2
        
        # محاسبه مرکز عمودی
        start_y = (self.size[1] - CARD_HEIGHT) / 2

        for i in range(BOARD_MAX_MINIONS):
            x = start_x + i * (CARD_WIDTH + CARD_SPACING)
            self.slots_positions.append((x, start_y))

    def set_minions(self, minions: List[Minion]):
        """
        لیستی از Minion ها را از Engine دریافت کرده و برای هر کدام
        یک CardView می‌سازد و در جایگاه مناسب قرار می‌دهد.
        """
        self.card_views = [] # لیست قبلی را پاک کن
        for i, minion in enumerate(minions):
            if i < BOARD_MAX_MINIONS:
                # ساخت CardView جدید با Minion و موقعیت اسلات مربوطه
                pos = self.slots_positions[i]
                new_card_view = CardView(minion, pos)
                self.card_views.append(new_card_view)

    def handle_event(self, event):
        """ رویدادها را به هر یک از کارت‌ها پاس می‌دهد. """
        for cv in self.card_views:
            cv.handle_event(event)

    def update(self, dt):
        """ وضعیت هر یک از کارت‌ها را آپدیت می‌کند. """
        for cv in self.card_views:
            cv.update(dt)

    def render(self, parent_surface: pygame.Surface):
        """
        ابتدا پس‌زمینه خود Board و سپس تمام کارت‌ها را روی آن رسم می‌کند.
        """
        # 1. پس‌زمینه خود Board را رسم کن
        self.surface.fill(BOARD_BG_COLOR)
        
        # 2. تمام CardView ها را روی سطح Board رندر کن
        for cv in self.card_views:
            cv.render(self.surface)
            
        # 3. در نهایت، سطح خود Board را روی سطح والد (صفحه اصلی) بکش
        parent_surface.blit(self.surface, self.position)
