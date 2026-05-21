import arcade
from enum import Enum


class Direction(Enum):
    UP = arcade.Vec2(0.0, 1.0)
    DOWN = arcade.Vec2(0.0, -1.0)
    LEFT = arcade.Vec2(-1.0, 0.0)
    RIGHT = arcade.Vec2(1.0, 0.0)
