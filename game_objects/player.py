from typing import Sequence

import pygame
from pygame.key import get_pressed
from pygame.sprite import Group
from pygame.math import Vector2

from constants import PlayerProps, ScreenProps, ShotProps 
from .circleshape import CircleShape
from .shot import Shot

class Player(CircleShape):

    containers: Sequence[Group] = []
   
    def __init__(self, x: float, y:float, rotation: float) -> None:
        self.rotation = rotation
        super().__init__(x, y, PlayerProps.RADIUS)
        self.shot_timer = 0.0

    @property
    def triangle(self) -> list[Vector2]:
        right = Vector2(1, 0).rotate(self.rotation + 90) / 1.5
        return [
            self.position + self.forward * self.radius,
            self.position - self.forward * self.radius + right * self.radius,
            self.position - self.forward * self.radius - right * self.radius,
        ]

    @property
    def forward(self) -> Vector2:
        return Vector2(1, 0).rotate(self.rotation)

    def shoot(self) ->  None:
        if self.shot_timer > PlayerProps.SHOT_COOLDOWN:
            self.shot_timer = 0.0
            Shot(self.position, self.forward * ShotProps.SPEED)


    def handle_keypress(self, delta: float) -> None:
        key = get_pressed()

        if key[pygame.K_a]:
            self.rotation -= PlayerProps.ROTATION_SPEED * delta

        if key[pygame.K_d]:
            self.rotation += PlayerProps.ROTATION_SPEED * delta

        if key[pygame.K_w]:
            self.velocity += self.forward * PlayerProps.SPEED * delta

        if key[pygame.K_s]:
            self.velocity -= self.forward * PlayerProps.SPEED * delta

        if key[pygame.K_SPACE]:
            self.shoot()

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.polygon(screen, "white", self.triangle, 0)

    
    def wrap_around(self) -> None:
        if self.position.x > ScreenProps.WIDTH:
            self.position.x = 0
        if self.position.x < 0:
            self.position.x = ScreenProps.WIDTH
        if self.position.y > ScreenProps.HEIGHT:
            self.position.y = 0
        if self.position.y < 0:
            self.position.y = ScreenProps.HEIGHT

    def update(self, delta: float) -> None:

        self.handle_keypress(delta)
        self.position += self.velocity
        self.wrap_around()
        self.shot_timer += delta
   
