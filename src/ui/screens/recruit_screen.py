import pygame
from typing import List
from src.core.interfaces import Component
from src.engine.card import Minion
from src.ui.components.card_view import CardView
from src.ui.components.board_view import BoardView
import src.config as config # برای دسترسی به ابعاد صفحه

# TODO: نام‌های واقعی ایونت‌ها را از فایل event_names.py وارد کنید
# from src.core.event_names import EVENT_CMD_BUY_MINION, EVENT_CMD_REFRESH_SHOP, EVENT_CMD_FREEZE_SHOP

# --- کلاس کمکی برای دکمه‌ها ---
class Button:
    def __init__(self, text, position, size=(100, 50), on_click=None):
        self.rect = pygame.Rect(position, size)
        self.text = text
        self.on_click = on_click
        self.font = pygame.font.Font(None, 32)
        self.color = (100, 120, 140)
        self.text_color = (255, 255, 255)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                if self.on_click:
                    self.on_click()
                    return True # برای نشان دادن اینکه رویداد مدیریت شده
        return False

    def render(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, border_radius=8)
        text_surf = self.font.render(self.text, True, self.text_color)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)

# --- کلاس اصلی صفحه خرید ---
# فرض می‌کنیم یک BaseScreen وجود دارد که از Component ارث می‌برد.
# اگر نه، مستقیم از Component ارث ببرید.
from src.ui.screens.base_screen import BaseScreen 

class RecruitScreen(BaseScreen):
    """
    صفحه خرید مینیون‌ها. این صفحه شامل Board بازیکن، کارت‌های فروشگاه
    و دکمه‌های کنترلی است.
    """
    def __init__(self, screen_manager, event_bus):
        super().__init__(screen_manager, event_bus)

        # 1. ساخت BoardView برای بازیکن در پایین صفحه
        board_height = 250
        board_pos = (0, config.SCREEN_HEIGHT - board_height)
        board_size = (config.SCREEN_WIDTH, board_height)
        self.player_board_view = BoardView(position=board_pos, size=board_size)

        # 2. آماده‌سازی جایگاه برای کارت‌های فروشگاه
        self.shop_card_views: List[CardView] = []
        
        # 3. ساخت دکمه‌ها
        self._create_buttons()

    def _create_buttons(self):
        """ متد کمکی برای ساخت و تنظیم موقعیت دکمه‌ها """
        # TODO: موقعیت دکمه‌ها را بر اساس UI نهایی تنظیم کنید
        button_y = 100 
        self.buy_button = Button("Buy", (100, button_y), on_click=self.on_buy_click)
        self.refresh_button = Button("Refresh", (220, button_y), on_click=self.on_refresh_click)
        self.freeze_button = Button("Freeze", (340, button_y), on_click=self.on_freeze_click)
        self.buttons = [self.buy_button, self.refresh_button, self.freeze_button]


    def set_state(self, player_minions: List[Minion], shop_minions: List[Minion]):
        """
        این متد توسط GameEngine فراخوانی می‌شود تا وضعیت صفحه را به‌روز کند.
        """
        # به‌روزرسانی کارت‌های Board بازیکن
        self.player_board_view.set_minions(player_minions)
        
        # ساخت CardView برای کارت‌های جدید فروشگاه
        self.shop_card_views = []
        # TODO: موقعیت کارت‌های فروشگاه را بر اساس UI نهایی تنظیم کنید
        shop_card_y = 200
        for i, minion in enumerate(shop_minions):
            pos = (150 + i * 180, shop_card_y)
            self.shop_card_views.append(CardView(minion, pos))

    # --- توابع Callback برای کلیک دکمه‌ها ---
    def on_buy_click(self):
        print("UI: Buy button clicked. Sending CMD_BUY_MINION event.")
        # self.event_bus.post(EVENT_CMD_BUY_MINION, minion_id=selected_minion.id)
        # نکته: منطق انتخاب کارت باید اضافه شود
        pass

    def on_refresh_click(self):
        print("UI: Refresh button clicked. Sending CMD_REFRESH_SHOP event.")
        # self.event_bus.post(EVENT_CMD_REFRESH_SHOP)
        pass
        
    def on_freeze_click(self):
        print("UI: Freeze button clicked. Sending CMD_FREEZE_SHOP event.")
        # self.event_bus.post(EVENT_CMD_FREEZE_SHOP)
        pass

    def handle_event(self, event):
        """ مدیریت ورودی کاربر برای دکمه‌ها """
        for button in self.buttons:
            if button.handle_event(event):
                return # اگر دکمه‌ای کلیک شد، دیگر نیازی به بررسی نیست
        
        self.player_board_view.handle_event(event)
        # TODO: منطق کلیک روی کارت‌های فروشگاه برای انتخاب (Buy)

    def update(self, dt):
        """ آپدیت تمام اجزای داخلی """
        self.player_board_view.update(dt)
        for cv in self.shop_card_views:
            cv.update(dt)

    def render(self, surface):
        """ رندر کردن تمام اجزای صفحه """
        surface.fill((30, 40, 50)) # رنگ پس‌زمینه صفحه
        
        # رندر Board بازیکن
        self.player_board_view.render(surface)
        
        # رندر کارت‌های فروشگاه
        for cv in self.shop_card_views:
            cv.render(surface)
            
        # رندر دکمه‌ها
        for button in self.buttons:
            button.render(surface)
