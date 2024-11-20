import random
from typing import Sequence

import pygame

from constants import AsteroidProps
from .circleshape import CircleShape


class Asteroid(CircleShape):

    containers: Sequence[pygame.sprite.Group] = []
    
    def __init__(self, position: pygame.Vector2, velocity: pygame.Vector2, size: int) -> None:
        super().__init__(position.x, position.y, size * AsteroidProps.MIN_RADIUS)
        self.velocity = velocity
        self.size = size

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, delta: float) -> None:
        self.position += self.velocity * delta

    def spawn_children(self) -> None:
        deflection = random.uniform(20, 50)
        velocity_left = self.velocity.rotate(deflection)
        velocity_right= self.velocity.rotate(-deflection)
        
        Asteroid(self.position, velocity_left, self.size - 1)
        Asteroid(self.position, velocity_right, self.size - 1)
        
    def split(self) -> None:
        if self.size > 1:
            self.spawn_children()
            
        self.kill()
