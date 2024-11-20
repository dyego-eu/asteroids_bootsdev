import pygame

from player import Player
from constants import (
    PLAYER_RADIUS,
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
)

def main() -> None:
    """Main function for game loop"""
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()

    delta = 0

    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 0)

    running = True
    while running:

        for event in pygame.event.get():
            if event == pygame.QUIT:
                running = False

        player.update(delta)
        screen.fill("red")
        player.draw(screen)
        
        delta = clock.tick(60) / 1000

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()

