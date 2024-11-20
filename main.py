import pygame

from constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
)

def main() -> None:
    """Main function for game loop"""
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()

    delta = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event == pygame.QUIT:
                running = False
        screen.fill("black")
        pygame.display.flip()
        delta = clock.tick(60) / 1000

    pygame.quit()

if __name__ == "__main__":
    main()

