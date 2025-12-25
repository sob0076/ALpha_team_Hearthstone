import pygame
import sys
import os

# تنظیم مسیرها
current_script_path = os.path.abspath(__file__)
src_directory = os.path.dirname(current_script_path)
project_root = os.path.dirname(src_directory)
sys.path.append(project_root)

from src.core.event_bus import EventBus
import src.core.event_names as Events
from src.engine.card import Minion
from src.ui.components.card_view import CardView
from src.engine.game_engine import GameEngine  # <--- ایمپورت کلاس جدید

# تنظیمات
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FPS = 60
BG_COLOR = (40, 40, 40)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Hearthstone - Modular Architecture")
    clock = pygame.time.Clock()

    # 1. زیرساخت (EventBus)
    event_bus = EventBus()

    # 2. هسته مرکزی (Game Engine)
    game_engine = GameEngine()

    # 3. ساخت داده‌ها (Model)
    razorfen = Minion(
        id="razorfen_1",  
        name="Razorfen Geomancer",
        image_path="assets/images/minions/BG20_100_render_80.webp",
        attack=3,
        health=10,
        tier=1,
        minion_type="Quilboar"
    )

    # **مهم:** معرفی مینیون به موتور بازی (Registration)
    # اگر این کار را نکنیم، انجین نمی‌تواند پیدایش کند
    game_engine.register_minion(razorfen)

    # 4. رابط کاربری (UI)
    card_view = CardView(razorfen, x=(SCREEN_WIDTH // 2) - 140, y=100, scale=0.7)

    print("--- Game Started: Fully Modular ---")
    
    running = True
    while running:
        dt = clock.tick(FPS)

        # --- UI Loop ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            card_view.handle_event(event)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # UI فقط پکت استاندارد می‌سازد و شوت می‌کند
                    packet = {
                        "type": Events.CMD_DEBUG_DAMAGE,
                        "source": "ui",
                        "target": "razorfen_1",
                        "payload": {"amount": 1}
                    }
                    event_bus.send_to_server(packet)
                    print(f"[UI] Request Sent: {packet['type']}")

        # --- Logic Loop ---
        # به جای تابع داخلی، متد انجین را صدا می‌زنیم
        # Main دیگر نمی‌داند داخل انجین چه خبر است
        event_bus.process_server_events(game_engine.process_event)

        # --- Render Loop ---
        card_view.update(dt)
        screen.fill(BG_COLOR)
        card_view.render(screen)
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()