import pygame

from constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    running = True
    while running:
        for event in pygame.event.get():
            if event == pygame.QUIT:
                running = False
        screen.fill("black")
        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main()

