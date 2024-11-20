import pygame
from pygame import Vector2
from pygame.surface import Surface


class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x: float, y: float, radius: float) -> None:
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = Vector2(x, y)
        self.velocity = Vector2(0, 0)
        self.radius = radius

    def draw(self, screen: Surface) -> None:
        pass

    def update(self, delta: float) -> None:
        pass
