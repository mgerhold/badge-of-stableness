from enum import Enum
from pathlib import Path
from typing import Final
from typing import final

import pygame

_ASSETS_PATH = Path(__file__).parent.parent.parent / "assets"
_TILES_PATH = _ASSETS_PATH / "tiles"


@final
class TileGraphic(Enum):
    GRASS = "grass.bmp"
    WATER = "water.bmp"
    COAST_TOP = "coast1.bmp"
    COAST_RIGHT = "coast2.bmp"
    COAST_BOTTOM = "coast3.bmp"
    COAST_LEFT = "coast4.bmp"
    COAST_CORNER_TOP_LEFT = "coast5.bmp"
    COAST_CORNER_TOP_RIGHT = "coast6.bmp"
    COAST_CORNER_BOTTOM_LEFT = "coast7.bmp"
    COAST_CORNER_BOTTOM_RIGHT = "coast8.bmp"
    COAST_TIP_TOP_LEFT = "coast9.bmp"
    COAST_TIP_TOP_RIGHT = "coast10.bmp"
    COAST_TIP_BOTTOM_LEFT = "coast11.bmp"
    COAST_TIP_BOTTOM_RIGHT = "coast12.bmp"


@final
class AssetManager:
    def __init__(self) -> None:
        self._tile_graphics: Final = AssetManager._load_tile_graphics()

    def get_tile_graphic(self, tile: TileGraphic) -> pygame.Surface:
        return self._tile_graphics[tile]

    @staticmethod
    def _load_tile_graphics() -> dict[TileGraphic, pygame.Surface]:
        return {
            tile_graphic: pygame.image.load(_TILES_PATH / tile_graphic.value).convert_alpha()
            for tile_graphic in TileGraphic
        }
