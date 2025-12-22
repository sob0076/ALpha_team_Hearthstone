import pygame
import sys
import os

# ---------------------------------------------------------
# تنظیم مسیرهای پایتون برای شناختن پوشه src و ریشه پروژه
# ---------------------------------------------------------
current_script_path = os.path.abspath(__file__)
src_directory = os.path.dirname(current_script_path)
project_root = os.path.dirname(src_directory)
sys.path.append(project_root)
# ---------------------------------------------------------

# ایمپورت‌های جدید بر اساس ساختار Refactor شده
from src.engine.card import Minion
from src.ui.components.card_view import CardView  # <--- مسیر جدید
from src.core.event_bus import EventBus           # <--- اضافه شدن هسته معماری

# تنظیمات صفحه
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FPS = 60
BG_COLOR = (30, 30, 30)

def main():
    # 1. راه‌اندازی اولیه
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Hearthstone Battlegrounds - Alpha Architecture")
    clock = pygame.time.Clock()

    # 2. راه‌اندازی معماری (Event Bus)
    # این شیء بعداً وظیفه جابجایی پیام‌ها بین سرور و UI را دارد
    event_bus = EventBus()

    # 3. ساخت مدل (Logic)
    razorfen_minion = Minion(
        name="Razorfen Geomancer",
        image_path="assets/images/minions/BG20_100_render_80.webp",
        attack=3,
        health=10,
        tier=1,
        minion_type="Quilboar"
    )

    # 4. ساخت کامپوننت (UI)
    # y=100 قرار دادیم تا کارت در جای مناسبی باشد
    card_view = CardView(razorfen_minion, x=SCREEN_WIDTH//2 - 100, y=100, scale=0.8)

    print("--- Game Started ---")
    print("Architecture loaded: EventBus ready, UI Component ready.")

    # 5. حلقه اصلی بازی
    running = True
    while running:
        # الف) مدیریت زمان (Delta Time)
        dt = clock.tick(FPS)

        # ب) پردازش ورودی‌ها (Event Handling)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            # ارسال ایونت به کامپوننت (طبق قرارداد جدید)
            card_view.handle_event(event)

            # تست دمیج با اسپیس
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    razorfen_minion.take_damage(1)

        # ج) آپدیت منطق (Update)
        card_view.update(dt)

        # د) رسم (Render)
        screen.fill(BG_COLOR)
        card_view.render(screen) # استفاده از متد استاندارد render به جای draw

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()