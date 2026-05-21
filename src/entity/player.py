import arcade
import math
from enum import Enum
from typing import Optional
from utils import Direction


class PlayerState(Enum):
    IDLE = 0
    MOVE = 1
    DEAD = 2


class PlayerDirection(Enum, str):
    UP = "Up"
    DOWN = "Down"
    LEFT = "Left"
    RIGHT = "Right"


class Player(arcade.Sprite):
    def __init__(self) -> None:
        super().__init__()

        self._lives: int = 0
        self.next_direction: PlayerDirection = PlayerDirection.RIGHT
        self.speed: float = 0.0
        # self._grid_coordinate: arcade.Vec2 = arcade.Vec2(0.0, 0.0)
        self.state: PlayerState = PlayerState.IDLE
        # self.tile_size: int

    # def get_grid_coordinate(self) -> arcade.Vec2:
    #     return self._grid_coordinate

    # def _update_grid_coordinate(self) -> None:
    #     tile_size: int = self.tile_size

    #     x: float = self.center_x / float(tile_size)
    #     y: float = self.center_y / float(tile_size)

    #     self._grid_coordinate = arcade.Vec2(
    #         math.floor(x),
    #         math.floor(y),
    #     )
    def set_next_direction(self, key: int) -> None:
        match key:
            case arcade.key.UP | arcade.key.W:
                self.next_direction = PlayerDirection.UP
            case arcade.key.DOWN | arcade.key.S:
                self.next_direction = PlayerDirection.DOWN
            case arcade.key.LEFT | arcade.key.A:
                self.next_direction = PlayerDirection.LEFT
            case arcade.key.RIGHT | arcade.key.D:
                self.next_direction = PlayerDirection.RIGHT

    def update(self, delta_time: float = 1 / 60) -> None:
        self.center_x += self.change_x
        self.center_y += self.change_y

    def collide_with_ghosts(self, ghosts) -> bool:
        return False

    def draw(self) -> None:
        match self.state:
            case PlayerState.IDLE:
                pass
            case PlayerState.MOVE:
                pass
            case PlayerState.DEAD:
                pass
