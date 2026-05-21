import arcade
from dataclasses import dataclass


@dataclass
class Pacgum:
    alive: bool
    radius: float
    point: int
    color: tuple[int, int, int, int]


def draw_pacgum(x: float, y: float, pacgum: Pacgum) -> None:
    arcade.draw_circle_filled(x, y, pacgum.radius, pacgum.color)
