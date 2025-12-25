import pygame
import sys
import os

current_script_path = os.path.abspath(__file__)
src_directory = os.path.dirname(current_script_path)
project_root = os.path.dirname(src_directory)
sys.path.append(project_root)

from src.core.event_bus import EventBus
from src.engine.game_engine import GameEngine
from src.ui.screen_manager import ScreenManager
from src.engine.card import Minion # <--- ایمپورت مدل

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FPS = 60

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Hearthstone - A4 Completed")
    clock = pygame.time.Clock()

    event_bus = EventBus()
    game_engine = GameEngine()

    # --- 1. ساخت مدل (داده‌ها) ---
    razorfen = Minion(
        id="razorfen_1",  
        name="Razorfen Geomancer",
        image_path="assets/images/minions/BG20_100_render_80.webp",
        attack=3,
        health=10,
        tier=1,
        minion_type="Quilboar"
    )

    # --- 2. ثبت در لاجیک (انجین) ---
    # انجین باید مینیون را بشناسد تا بتواند از جانش کم کند
    game_engine.register_minion(razorfen)

    # --- 3. ثبت در گرافیک (منیجر) ---
    # منیجر مینیون را به RecruitScreen می‌دهد تا آن را رسم کند
    screen_manager = ScreenManager(event_bus, SCREEN_WIDTH, SCREEN_HEIGHT, test_minion=razorfen)

    print("--- Game Started: A1(Logic) + A2(Events) + A4(Screens) ---")
    
    running = True
    while running:
        dt = clock.tick(FPS)

        # --- Input ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            screen_manager.handle_event(event)

        # --- Logic ---
        event_bus.process_server_events(game_engine.process_event)
        
        def handle_ui_events(event):
            screen_manager.handle_system_event(event)
        event_bus.process_ui_events(handle_ui_events)

        # --- Render ---
        screen_manager.update(dt)
        screen_manager.render(screen)
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()