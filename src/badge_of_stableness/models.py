import random
from enum import Enum
from enum import StrEnum
from enum import auto
from typing import Final
from typing import Optional
from typing import Self
from typing import final

from pydantic import BaseModel

from badge_of_stableness.utils import clamp


@final
class TileType(StrEnum):
    GRASS = "grass"
    WATER = "water"


@final
class RiverSetting(Enum):
    YES = auto()
    NO = auto()
    RANDOM = auto()


@final
class Map(BaseModel):
    name: str
    seed: int
    tiles: list[list[TileType]]

    @property
    def width(self) -> int:
        return len(self.tiles[0])

    @property
    def height(self) -> int:
        return len(self.tiles)

    @classmethod
    def generate(
        cls,
        name: str,
        width: int,
        height: int,
        river_setting: RiverSetting = RiverSetting.RANDOM,
        seed: Optional[int] = None,
    ) -> Self:
        if seed is None:
            seed = random.randint(0, 2**32 - 1)
        random.seed(seed)

        match river_setting:
            case RiverSetting.YES:
                has_river = True
            case RiverSetting.NO:
                has_river = False
            case RiverSetting.RANDOM:
                has_river = random.choice((True, False))

        tiles: Final = [[TileType.GRASS for _ in range(width)] for _ in range(height)]

        if has_river:
            did_jitter_last = False
            river_y: Final = height // 2 + random.randint(-height // 8, height // 8)
            river_height: Final = random.randint(2, 5)
            max_river_jitter: Final = random.randint(2, 5)
            river_center_y = river_y
            for x in range(width):
                random_float = random.random()
                old_river_center_y = river_center_y
                if not did_jitter_last and random_float <= 0.25:
                    river_center_y -= 1
                elif not did_jitter_last and random_float <= 0.5:
                    river_center_y += 1
                river_center_y = clamp(river_center_y, river_y - max_river_jitter, river_y + max_river_jitter)
                did_jitter_last = old_river_center_y != river_center_y
                lower_y = river_center_y - river_height // 2
                higher_y = lower_y + river_height
                for y in range(lower_y, higher_y + 1):
                    tiles[y][x] = TileType.WATER

        return cls(
            name=name,
            seed=seed,
            tiles=tiles,
        )
