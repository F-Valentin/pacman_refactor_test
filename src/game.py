import arcade
from level import Level
from entity.player import Player


class Game:
    def __init__(self, window: arcade.Window) -> None:
        self.__window = window

    def start(self) -> None:
        # 1 - create levels
        # 2 - start the first level
        level = Level(Player())
        self.__window.show_view(level)

    def pause(self) -> None:
        pass
