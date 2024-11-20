import sys
from itertools import product

import pygame

from asteroids import Asteroid
from asteroidfield import AsteroidField
from player import Player
from shot import Shot
from constants import ScreenProps

def main() -> None:
    """Main function for game loop"""
    pygame.init()
    screen = pygame.display.set_mode((ScreenProps.WIDTH, ScreenProps.HEIGHT))

    clock = pygame.time.Clock()

    delta = 0

    drawables = pygame.sprite.Group()
    updatables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (drawables, updatables)
    Shot.containers = (drawables, updatables, shots)
    Asteroid.containers = (drawables, updatables, asteroids)
    AsteroidField.containers = (updatables,)

    player = Player(ScreenProps.WIDTH // 2, ScreenProps.HEIGHT // 2, 0)
    AsteroidField()

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
    
        for object in asteroids:
            if object ^ player:
                print("Game Over")
                running = False

        for shot, asteroid in product(shots, asteroids):
            if shot ^ asteroid:
                shot.kill()
                asteroid.split()

        delta = clock.tick(60) / 1000
        pygame.display.set_caption(str(delta))

        pygame.display.flip()

    pygame.quit()
    sys.exit(0)

if __name__ == "__main__":
    main()

