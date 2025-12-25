import pygame
from src.ui.screens.base_screen import Screen
# هیچ CardView یا Modelی ایمپورت نمی‌شود

class BattleScreen(Screen):
    # ببین! آرگومان model_minion حذف شد. این صفحه هیچی نمی‌داند.
    def __init__(self, event_bus):
        super().__init__("Combat", event_bus)
        self.bg_color = (60, 20, 20) # قرمز زرشکی

    def handle_event(self, event):
        # هیچ کارتی نیست که ایونت بگیرد
        pass

    def update(self, dt):
        pass

    def render(self, surface):
        surface.fill(self.bg_color)
        
        # فقط متن خالی (بدون کارت)
        font = pygame.font.SysFont(None, 48)
        img = font.render("COMBAT PHASE (Empty Room)", True, (255, 100, 100))
        surface.blit(img, (50, 50))