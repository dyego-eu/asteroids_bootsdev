import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_ROTATION_SPEED

class Player(CircleShape):
    def __init__(self, x: float, y:float, rotation: float) -> None:
        self.rotation = rotation
        super().__init__(x, y, PLAYER_RADIUS)

    @property
    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(1, 0).rotate(self.rotation)
        right = pygame.Vector2(1, 0).rotate(self.rotation + 90) / 1.5
        return [
            self.position + forward * self.radius,
            self.position - forward * self.radius + right * self.radius,
            self.position - forward * self.radius - right * self.radius,
        ]

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.polygon(screen, "white", self.triangle, 0)

    
    def update(self, delta: float) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotation -= PLAYER_ROTATION_SPEED * delta

        if keys[pygame.K_d]:
            self.rotation += PLAYER_ROTATION_SPEED * delta
            
