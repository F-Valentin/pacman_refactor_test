from __future__ import annotations
from typing import TYPE_CHECKING
import arcade
from button import Button

if TYPE_CHECKING:
    from game import Game


class MenuView(arcade.View):
    def __init__(self, game: Game) -> None:
        super().__init__()

        self._game = game
        self.__start_button: Button

        self.setup()

    @property
    def game(self) -> Game:
        return self._game

    def setup(self) -> None:
        self.__start_button = Button(
            self.window.width // 2,
            self.window.height // 2 + 100,
            "assets/button/game01.png"
        )

    def on_show_view(self) -> None:
        print("Menu View started")

    def on_key_press(self, symbol: int, modifiers: int) -> None:
        if symbol == arcade.key.SPACE:
            self.game.start()

        if symbol == arcade.key.Q:
            pass

    def on_draw(self) -> None:
        """ Draw everything """
        self.clear()

        self.__start_button.draw()

        arcade.Text(
            "Menu View",
            self.window.width / 2,
            self.window.height / 2,
            arcade.color.WHITE,
            20.0).draw()
