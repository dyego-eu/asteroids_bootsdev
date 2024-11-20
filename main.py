import sys

import pygame

from player import Player
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

    drawables = pygame.sprite.Group()
    updatables = pygame.sprite.Group()

    Player.containers = (drawables, updatables)
    Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 0)

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("black")

        for object in drawables:
            object.draw(screen)

        for object in updatables:
            object.update(delta)
    
        delta = clock.tick(60) / 1000

        pygame.display.flip()

    pygame.quit()
    sys.exit(0)

if __name__ == "__main__":
    main()

