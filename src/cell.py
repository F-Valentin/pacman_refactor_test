import arcade
from typing import Optional

class Cell:
    def __init__(self, grid_pos: arcade.Vec2, walls: int, size: int) -> None:
        self._grid_x: float = grid_pos.x
        self._grid_y: float = grid_pos.y
        self._size = size
        self._walls = walls
        self.center: Optional[arcade.Vec2] = None
    
    @property
    def grid_x(self) -> float:
        return self._grid_x

    @property
    def grid_y(self) -> float:
        return self._grid_y
    
    @property
    def size(self) -> int:
        return self._size

    @property
    def walls(self) -> int:
        return self._walls