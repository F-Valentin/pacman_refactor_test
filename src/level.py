import arcade

from entity.player import Player
from maze import Maze


class Level(arcade.View):
    def __init__(self, player: Player, maze: Maze) -> None:
        super().__init__()

        self.__player = player
        self.__maze = maze

    def on_update(self, delta_time: float) -> None:
        # self.__fixed_update(delta_time)
        pass

    def __fixed_update(self, delta_time: float) -> None:
        time_accumulator: float = delta_time
        time_step: float = 1 / 60

        while time_accumulator >= time_step:

            time_accumulator -= time_step

    def on_key_press(self, symbol: int, modifiers: int) -> None:
        self.__player.set_next_direction(key=symbol)

    def on_draw(self) -> None:
        self.clear()

        # self.__player.draw()
        self.__maze.draw()
