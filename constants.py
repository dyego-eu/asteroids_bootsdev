from enum import Enum


class ScreenProps(int, Enum):
    WIDTH = 1280
    HEIGHT = 720


class AsteroidProps(int, Enum):
    MIN_RADIUS = 20
    KINDS = 3
    SPAWN_RATE = 1  # seconds
    MAX_RADIUS = MIN_RADIUS * KINDS


class PlayerProps(float, Enum):
    RADIUS = 20
    ROTATION_SPEED = 300
    SPEED = 5
    SHOT_COOLDOWN = 0.3


class ShotProps(int, Enum):
    SPEED = 500
    RADIUS = 5

