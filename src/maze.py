import arcade
from cell import Cell

class Maze:
    def __init__(self, width: int, height: int,
                 top_left_pos: arcade.Vec2, cell_size: int) -> None:
        self._grid: list[list[Cell]] = []
        self._width = width
        self._height = height
        self._top_left_pos = top_left_pos
        self._cell_size = cell_size
    
    @property
    def grid(self) -> list[list[Cell]]:
        return self._grid
    
    @property
    def width(self) -> int:
        return self._width

    @property
    def height(self) -> int:
        return self._height
    
    @property
    def top_left_pos(self) -> arcade.Vec2:
        return self._top_left_pos