import random
from typing import Sequence

from pygame.sprite import Sprite, Group
from pygame.math import Vector2

from constants import AsteroidProps, ScreenProps
from .asteroids import Asteroid


class AsteroidField(Sprite):
    edges = [
        [
            Vector2(1, 0),
            lambda y: Vector2(-AsteroidProps.MAX_RADIUS, y * ScreenProps.HEIGHT),
        ],
        [
            Vector2(-1, 0),
            lambda y: Vector2(
                ScreenProps.WIDTH + AsteroidProps.MAX_RADIUS, y * ScreenProps.HEIGHT
            ),
        ],
        [
            Vector2(0, 1),
            lambda x: Vector2(x * ScreenProps.WIDTH, -AsteroidProps.MAX_RADIUS),
        ],
        [
            Vector2(0, -1),
            lambda x: Vector2(
                x * ScreenProps.WIDTH, ScreenProps.HEIGHT + AsteroidProps.MAX_RADIUS
            ),
        ],
    ]
    containers: Sequence[Group] = []

    def __init__(self) -> None:
        Sprite.__init__(self, *self.containers)
        self.spawn_timer = 0.0

    def spawn(self) -> None:
        edge = random.choice(self.edges)
        speed = random.randint(40, 100)
        velocity = (edge[0] * speed).rotate(random.randint(-30, 30))
        position = edge[1](random.uniform(0, 1))
        kind = random.randint(1, AsteroidProps.KINDS)
        Asteroid(position, velocity, kind)

    def update(self, delta: float) -> None:
        self.spawn_timer += delta
        if self.spawn_timer > AsteroidProps.SPAWN_RATE:
            self.spawn_timer = 0
            self.spawn()

