from typing import Sequence
import pygame
import random
from asteroids import Asteroid
from constants import AsteroidProps, ScreenProps


class AsteroidField(pygame.sprite.Sprite):
    edges = [
        [
            pygame.Vector2(1, 0),
            lambda y: pygame.Vector2(-AsteroidProps.MAX_RADIUS, y * ScreenProps.HEIGHT),
        ],
        [
            pygame.Vector2(-1, 0),
            lambda y: pygame.Vector2(
                ScreenProps.WIDTH + AsteroidProps.MAX_RADIUS, y * ScreenProps.HEIGHT
            ),
        ],
        [
            pygame.Vector2(0, 1),
            lambda x: pygame.Vector2(x * ScreenProps.WIDTH, -AsteroidProps.MAX_RADIUS),
        ],
        [
            pygame.Vector2(0, -1),
            lambda x: pygame.Vector2(
                x * ScreenProps.WIDTH, ScreenProps.HEIGHT + AsteroidProps.MAX_RADIUS
            ),
        ],
    ]
    containers: Sequence[pygame.sprite.Group] = []

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, *self.containers)
        self.spawn_timer = 0.0

    def spawn(self):
        edge = random.choice(self.edges)
        speed = random.randint(40, 100)
        velocity = (edge[0] * speed).rotate(random.randint(-30, 30))
        position = edge[1](random.uniform(0, 1))
        kind = random.randint(1, AsteroidProps.KINDS)
        Asteroid(position, velocity, kind)

    def update(self, dt):
        self.spawn_timer += dt
        if self.spawn_timer > AsteroidProps.SPAWN_RATE:
            self.spawn_timer = 0
            self.spawn()
