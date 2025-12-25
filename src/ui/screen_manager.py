import src.core.event_names as Events
from src.ui.screens.recruit_screen import RecruitScreen
from src.ui.screens.battle_screen import BattleScreen

class ScreenManager:
    def __init__(self, event_bus, screen_width, screen_height, test_minion):
        self.event_bus = event_bus
        self.width = screen_width
        self.height = screen_height

        # ✅ اصلاح معماری:
        # Recruit: مینیون را لازم دارد -> بهش می‌دهیم.
        # Combat: فعلاً خالی است -> بهش نمی‌دهیم.
        self.screens = {
            "RECRUIT": RecruitScreen(event_bus, test_minion), 
            "COMBAT": BattleScreen(event_bus)  # <--- ببین! هیچ مینیونی پاس داده نشد.
        }
        
        self.current_screen = self.screens["RECRUIT"]
        print(f"[ScreenManager] Initialized. Minion passed ONLY to Recruit.")

    def change_phase(self, new_phase_name):
        key = new_phase_name.upper()
        if key in self.screens:
            self.current_screen = self.screens[key]
            print(f"[ScreenManager] Switched to -> {key}")

    def handle_event(self, event):
        self.current_screen.handle_event(event)

        # لاجیک TAB (تغییر فاز)
        import pygame
        if event.type == pygame.KEYDOWN and event.key == pygame.K_TAB:
            current = self.current_screen.name
            next_phase = "COMBAT" if "Recruit" in current else "RECRUIT"
            
            self.event_bus.send_to_ui({
                "type": Events.SYS_PHASE_CHANGED,
                "source": "ui_manager",
                "target": None,
                "payload": {"new_phase": next_phase}
            })

    def update(self, dt):
        self.current_screen.update(dt)

    def render(self, surface):
        self.current_screen.render(surface)
        
    def handle_system_event(self, event):
        if event["type"] == Events.SYS_PHASE_CHANGED:
            new_phase = event["payload"].get("new_phase")
            self.change_phase(new_phase)