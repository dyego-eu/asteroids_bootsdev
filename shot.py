import pygame
from circleshape import CircleShape
from constants import ShotProps

class Shot(CircleShape):

    def __init__(self, position: pygame.Vector2, velocity: pygame.Vector2) -> None:
        super().__init__(position.x, position.y, ShotProps.RADIUS)
        self.velocity = velocity

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, ShotProps.RADIUS, 0)

    def update(self, delta: float) -> None:
        self.position += self.velocity * delta

