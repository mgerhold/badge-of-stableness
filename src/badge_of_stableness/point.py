from typing import Final
from typing import Self
from typing import final


@final
class Point:
    def __init__(self, x: float, y: float) -> None:
        self._x: Final = x
        self._y: Final = y

    @property
    def x(self) -> float:
        return self._x

    @property
    def y(self) -> float:
        return self._y

    def __add__(self, other: Self) -> "Point":
        return Point(self._x + other._x, self._y + other._y)

    def __sub__(self, other: Self) -> "Point":
        return Point(self._x - other._x, self._y - other._y)

    def __mul__(self, other: float) -> "Point":
        return Point(self._x * other, self._y * other)

    def __truediv__(self, other: float) -> "Point":
        return Point(self._x / other, self._y / other)

    def __str__(self) -> str:
        return f"({self._x}, {self._y})"

    def __repr__(self) -> str:
        return f"Point({self._x}, {self._y})"
