from pygame import Vector2, Surface
from pygame.draw import circle as draw_circle

from constants import ShotProps
from .circleshape import CircleShape

class Shot(CircleShape):

    def __init__(self, position: Vector2, velocity: Vector2) -> None:
        super().__init__(position.x, position.y, ShotProps.RADIUS)
        self.velocity = velocity

    def draw(self, screen: Surface) -> None:
        draw_circle(screen, "white", self.position, ShotProps.RADIUS, 0)

    def update(self, delta: float) -> None:
        self.position += self.velocity * delta

