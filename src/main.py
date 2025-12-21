import pygame
import sys
import os

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Hearthstone Battlegrounds - Alpha Team")
    clock = pygame.time.Clock()

    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    test_image_path = os.path.join(
        project_root, 
        "assets", "images", "minions", "BG20_100_render_80.webp"
    )

    try:
        original_image = pygame.image.load(test_image_path)
        image = pygame.transform.scale(original_image, (200, 300))
        print("Success: Image loaded correctly!")
    except Exception as e:
        print(f"Error loading image: {e}")
        image = None

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK) 

        if image:
            rect = image.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
            screen.blit(image, rect)
            
            font = pygame.font.SysFont("Arial", 24)
            text = font.render("Engine initialized successfully!", True, WHITE)
            screen.blit(text, (20, 20))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()