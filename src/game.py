import arcade
from level import Level


class Game:
    def __init__(self, window: arcade.Window) -> None:
        self._window = window

    def start(self) -> None:
        # 1 - create levels
        # 2 - start the first level
        level = Level()
        self._window.show_view(level)

    def pause(self) -> None:
        pass
