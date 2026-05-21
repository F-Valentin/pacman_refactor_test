import arcade
from cell import Cell
from pacgum import Pacgum
from typing import Optional


class Maze:
    def __init__(self, width: int, height: int,
                 top_left_pos: arcade.Vec2, cell_size: int) -> None:
        self._grid: list[list[Cell]] = []
        self._width = width
        self._height = height
        self._top_left_pos = top_left_pos
        self._cell_size = cell_size
        self.__wall_points: Optional[list[tuple[float, float]]] = None 
    

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
    
    def setup(self) -> None:
        self.__setup_cells()
        self.__wall_points = self.__build_wall_points()
    
    def __build_wall_points(self) -> list[tuple[float, float]]:
        wall_points: list[tuple[float, float]] = []
        cell_size: int = self._cell_size

        for cells in self.grid:
            for cell in cells:
                point_x = cell.grid_x * cell_size + self.top_left_pos.x

                point_y = (
                    (self.height - 1 - cell.grid_y) * cell_size +
                    self.top_left_pos.y
                )

                top_left = (point_x, point_y + cell_size)
                top_right = (point_x + cell_size, point_y + cell_size)
                bottom_left = (point_x, point_y)
                bottom_right = (point_x + cell_size, point_y)

                north, east, south, west = 0b0001, 0b0010, 0b0100, 0b1000
                
                if cell.walls & north:
                    wall_points += [top_left, top_right]
                if cell.walls & east:
                    wall_points += [top_right, bottom_right]
                if cell.walls & south:
                    wall_points += [bottom_left, bottom_right] 
                if cell.walls & west:
                    wall_points += [top_left, bottom_left]
        
        return wall_points


    def __setup_cells(self) -> None:
        cell_size: int = self._cell_size

        for cells in self.grid:
            for cell in cells:
                center_x = int(
                    cell.grid_x * cell_size +
                    self.top_left_pos.x + cell_size // 2
                )

                center_y = int(
                    (self.height - 1 - cell.grid_y) * cell_size +
                    self.top_left_pos.y + cell_size // 2
                )

                cell.center = arcade.Vec2(center_x, center_y)

                blocked: int = 0x0F
                pacgum_radius: float = 3.0
                pacgum_color: tuple[int, int, int, int] = arcade.color.WHITE
                pacgum_point: int = 10

                if cell.walls != blocked:
                    pacgum = Pacgum(
                        True, pacgum_radius, pacgum_point, pacgum_color
                    )

                    cell.add_pacgum(pacgum)
