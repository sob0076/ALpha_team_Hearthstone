import pygame
from src.ui.screens.base_screen import Screen
import src.core.event_names as Events
from src.ui.components.card_view import CardView

class RecruitScreen(Screen):
    def __init__(self, event_bus, model_minion):
        super().__init__("Recruit", event_bus)
        self.bg_color = (20, 20, 50) 
        self.minion_id = model_minion.id # نگه داشتن آیدی برای ارسال دستور
        
        # ✅ ساخت CardView اختصاصی برای این صفحه
        # مختصات وسط صفحه
        center_x = 1280 // 2 - 140
        self.card_view = CardView(model_minion, x=center_x, y=100, scale=0.7)

    def handle_event(self, event):
        self.card_view.handle_event(event)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # لاجیک دمیج فقط اینجا کار می‌کند
                packet = {
                    "type": Events.CMD_DEBUG_DAMAGE,
                    "source": "ui_recruit",
                    "target": self.minion_id,
                    "payload": {"amount": 1}
                }
                self.event_bus.send_to_server(packet)
                print(f"[Recruit] Sent Damage Command!")

    def update(self, dt):
        self.card_view.update(dt)

    def render(self, surface):
        surface.fill(self.bg_color)
        self.card_view.render(surface)
        
        # راهنما
        font = pygame.font.SysFont(None, 36)
        text = font.render("RECRUIT PHASE: Press SPACE to Damage | TAB to Switch", True, (200, 200, 255))
        surface.blit(text, (20, 20))