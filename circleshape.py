from abc import ABC, abstractmethod
from typing import Sequence

import pygame
from pygame import Vector2
from pygame.surface import Surface


class CircleShape(pygame.sprite.Sprite, ABC):

    containers: Sequence[pygame.sprite.Group] = []

    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(*self.containers)
        self.position = Vector2(x, y)
        self.velocity = Vector2(0, 0)
        self.radius = radius

    @abstractmethod
    def draw(self, screen: Surface) -> None:
        pass

    @abstractmethod
    def update(self, delta: float) -> None:
        pass

    def __xor__(self, other) -> bool:
        if not isinstance(other, CircleShape):
            raise ValueError("Only allowed to compare distances between CircleShapes")

        return self.position.distance_to(other.position) < self.radius + other.radius

