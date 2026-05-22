import arcade
from arcade.types import PathOrTexture
from utils import Rect


class Button(Rect):
    def __init__(self, x: float, y: float,
                 path_to_images: str) -> None:
        self.center: arcade.Vec2 = arcade.Vec2(x, y)
        self.__sprite: arcade.Sprite = arcade.Sprite(path_to_images)
        self.__sprite_list = arcade.SpriteList()

        super().__init__(
            x, y, self.__sprite.width, self.__sprite.height
        )

        self.__sprite.position = self.center
        self.__sprite_list.append(self.__sprite)

        print(len(self.__sprite_list))

    @property
    def width(self) -> float:
        return self._width

    @property
    def height(self) -> float:
        return self._height

    def draw(self) -> None:
        self.__sprite_list.draw()
        # arcade.draw_circle_filled(self.center.x, self.center.y, 6, arcade.color.WHITE)
