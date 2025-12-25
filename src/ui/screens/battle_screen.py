import pygame
from typing import List
from src.core.interfaces import Component
from src.engine.card import Minion
from src.ui.components.board_view import BoardView
from src.ui.screens.base_screen import BaseScreen
import src.config as config

class CombatScreen(BaseScreen):
    """
    صفحه مبارزه. این صفحه فقط نمایشی است و وضعیت Board بازیکن و حریف را
    نمایش می‌دهد. هیچ ورودی از کاربر دریافت نمی‌کند.
    """
    def __init__(self, screen_manager, event_bus):
        super().__init__(screen_manager, event_bus)

        # 1. ساخت BoardView برای بازیکن در پایین صفحه
        board_height = 250
        player_board_pos = (0, config.SCREEN_HEIGHT - board_height)
        player_board_size = (config.SCREEN_WIDTH, board_height)
        self.player_board_view = BoardView(position=player_board_pos, size=player_board_size)

        # 2. ساخت BoardView برای حریف در بالای صفحه
        opponent_board_pos = (0, 0)
        opponent_board_size = (config.SCREEN_WIDTH, board_height)
        self.opponent_board_view = BoardView(position=opponent_board_pos, size=opponent_board_size)
        
        # فضای خالی در وسط صفحه برای انیمیشن‌های آینده مبارزه باقی می‌ماند

    def set_state(self, player_minions: List[Minion], opponent_minions: List[Minion]):
        """
        این متد توسط GameEngine فراخوانی می‌شود تا وضعیت هر دو Board را به‌روز کند.
        """
        self.player_board_view.set_minions(player_minions)
        self.opponent_board_view.set_minions(opponent_minions)

    def handle_event(self, event):
        """
        این صفحه به هیچ رویدادی واکنش نشان نمی‌دهد، چون کاملاً نمایشی است.
        """
        pass

    def update(self, dt):
        """ آپدیت تمام اجزای داخلی (در آینده برای انیمیشن‌ها استفاده می‌شود) """
        self.player_board_view.update(dt)
        self.opponent_board_view.update(dt)

    def render(self, surface):
        """ رندر کردن تمام اجزای صفحه """
        surface.fill((50, 30, 30)) # یک رنگ پس‌زمینه متفاوت برای تم مبارزه
        
        # رندر Board بازیکن
        self.player_board_view.render(surface)
        
        # رندر Board حریف
        self.opponent_board_view.render(surface)
        
        # TODO: در آینده، انیمیشن‌های مبارزه در فضای خالی وسط رندر می‌شوند.