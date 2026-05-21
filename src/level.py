import arcade

from entity.player import Player


class Level(arcade.View):
    def __init__(self, player: Player) -> None:
        super().__init__()

        self.__player = player

    def on_update(self, delta_time: float) -> bool | None:
        self.__fixed_update(delta_time)

    def __fixed_update(self, delta_time: float) -> None:
        time_accumulator: float = delta_time
        time_step: float = 1 / 60

        while time_accumulator >= time_step:

            time_accumulator -= time_step

    def on_key_press(self, symbol: int, modifiers: int) -> bool | None:
        self.__player.set_next_direction(key=symbol)

    def on_draw(self) -> bool | None:
        self.clear()

        self.__player.draw()
