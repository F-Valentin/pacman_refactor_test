import arcade
import math
from enum import Enum
from typing import Optional


class PlayerState(Enum):
    IDLE = 0
    MOVE = 1
    DEAD = 2


class Player(arcade.Sprite):
    def __init__(self) -> None:
        super().__init__()

        self._lives: int = 0
        self.direction: arcade.Vec2 = arcade.Vec2(0.0, 0.0)
        self._grid_coordinate: arcade.Vec2 = arcade.Vec2(0.0, 0.0)
        self.state: PlayerState = PlayerState.IDLE

    @property
    def grid_coordinate(self) -> arcade.Vec2:
        return self._grid_coordinate

    @grid_coordinate.setter
    def grid_coordinate(self, tile_size: int) -> None:
        x: float = self.center_x / float(tile_size)
        y: float = self.center_y / float(tile_size)

        self._grid_coordinate = arcade.Vec2(
            math.floor(x),
            math.floor(y),
        )

    def move(self) -> None:
        pass

    def handle_input_key(self, key: int) -> None:
        from arcade import Vec2

        direction: Optional[Vec2] = None

        match key:
            case arcade.key.UP | arcade.key.W:
                direction = Vec2(0.0, 1.0)
            case arcade.key.DOWN| arcade.key.S:
                direction = Vec2(0.0, -1.0)
            case arcade.key.LEFT | arcade.key.A:
                direction = Vec2(-1.0, 0.0)
            case arcade.key.RIGHT | arcade.key.D:
                direction = Vec2(1.0, 0.0)
        
        if direction:
            self.direction = direction

    def draw(self) -> None:
        match self.state:
            case PlayerState.IDLE:
                pass
            case PlayerState.MOVE:
                pass
            case PlayerState.DEAD:
                pass
