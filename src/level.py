import arcade


class Level(arcade.View):
    def __init__(self) -> None:
        super().__init__()

    def on_update(self, delta_time: float) -> bool | None:
        self._fixed_update(delta_time)

    def _fixed_update(self, delta_time: float) -> None:
        time_accumulator: float = delta_time
        time_step: float = 1 / 60

        while time_accumulator >= time_step:

            time_accumulator -= time_step

    def on_draw(self) -> bool | None:
        self.clear()

        arcade.Text(
            "Level View",
            self.window.width / 2,
            self.window.height / 2,
            font_size=20).draw()
