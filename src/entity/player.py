import arcade
import math
from enum import Enum
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from entity.ghost import Ghost
    from maze import Maze


class PlayerState(Enum):
    IDLE = 0
    MOVE = 1
    DEAD = 2


class PlayerDirection(Enum):
    UP = "Up"
    DOWN = "Down"
    LEFT = "Left"
    RIGHT = "Right"


class Player(arcade.Sprite):
    def __init__(self, maze: Maze) -> None:
        super().__init__()

        self._lives: int = 0
        self.next_direction: Optional[PlayerDirection] = None
        self.speed: float = 0.0
        self.state: PlayerState = PlayerState.IDLE
        self.__maze = maze

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

    def update(self, delta_time: float = 1 / 60, *args, **kwargs) -> None:
        pass

    def collide_with_ghosts(self, ghosts: Ghost) -> bool:
        return False

    def draw(self) -> None:
        # match self.state:
        #     case PlayerState.IDLE:
        #         pass
        #     case PlayerState.MOVE:
        #         pass
        #     case PlayerState.DEAD:
        #         pass
        arcade.draw_circle_filled(
            self.center_x,
            self.center_y,
            20,
            arcade.color.YELLOW)
