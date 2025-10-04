from typing import Final
from typing import Self
from typing import final


@final
class IntPoint:
    def __init__(self, x: int, y: int) -> None:
        self._x: Final = x
        self._y: Final = y

    @property
    def x(self) -> int:
        return self._x

    @property
    def y(self) -> int:
        return self._y

    def __add__(self, other: Self) -> "IntPoint":
        return IntPoint(self._x + other._x, self._y + other._y)

    def __sub__(self, other: Self) -> "IntPoint":
        return IntPoint(self._x - other._x, self._y - other._y)

    def __mul__(self, other: int) -> "IntPoint":
        return IntPoint(self._x * other, self._y * other)

    def __floordiv__(self, other: int) -> "IntPoint":
        return IntPoint(self._x // other, self._y // other)

    def __str__(self) -> str:
        return f"({self._x}, {self._y})"

    def __repr__(self) -> str:
        return f"Point({self._x}, {self._y})"
