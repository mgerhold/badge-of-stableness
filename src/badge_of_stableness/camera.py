from typing import Final
from typing import final

import pygame

from badge_of_stableness.point import Point


@final
class Camera:
    def __init__(self) -> None:
        self._center = Point(0.0, 0.0)
        self._zoom = 1.0

    def world_to_screen(self, point: Point, screen: pygame.Surface) -> Point:
        screen_size: Final = Point(screen.get_width(), screen.get_height())
        screen_center: Final = screen_size / 2
        screen_offset: Final = (point - self._center) * self._zoom
        return Point(
            screen_center.x + screen_offset.x,
            screen_center.y - screen_offset.y,
        )

    def move(self, delta: Point) -> None:
        self._center += delta

    def zoom(self, zoom_factor: float) -> None:
        self._zoom *= zoom_factor
