from typing import Final

import pygame

from badge_of_stableness.asset_manager import AssetManager
from badge_of_stableness.asset_manager import TileGraphic
from badge_of_stableness.camera import Camera
from badge_of_stableness.int_point import IntPoint
from badge_of_stableness.models import Map
from badge_of_stableness.models import RiverSetting
from badge_of_stableness.models import TileType
from badge_of_stableness.point import Point
from badge_of_stableness.pygame import create_pygame_context


def tile_type_to_graphic(map_: Map, position: IntPoint, assets: AssetManager) -> pygame.Surface:
    tile_type: Final = map_.tiles[position.y][position.x]

    def _get_or_default(pos: IntPoint, default: TileType) -> TileType:
        if 0 <= pos.x < map_.width and 0 <= pos.y < map_.height:
            return map_.tiles[pos.y][pos.x]
        return default

    match tile_type:
        case TileType.GRASS:
            return assets.get_tile_graphic(TileGraphic.GRASS)
        case TileType.WATER:
            top_left = _get_or_default(IntPoint(position.x - 1, position.y - 1), TileType.WATER)
            top = _get_or_default(IntPoint(position.x, position.y - 1), TileType.WATER)
            top_right = _get_or_default(IntPoint(position.x + 1, position.y - 1), TileType.WATER)
            left = _get_or_default(IntPoint(position.x - 1, position.y), TileType.WATER)
            right = _get_or_default(IntPoint(position.x + 1, position.y), TileType.WATER)
            bottom_left = _get_or_default(IntPoint(position.x - 1, position.y + 1), TileType.WATER)
            bottom = _get_or_default(IntPoint(position.x, position.y + 1), TileType.WATER)
            bottom_right = _get_or_default(IntPoint(position.x + 1, position.y + 1), TileType.WATER)

            match top_left, top, top_right, left, right, bottom_left, bottom, bottom_right:
                case (
                    TileType.GRASS,  # top left
                    TileType.GRASS,  # top
                    _,  # top right
                    TileType.GRASS,  # left
                    TileType.WATER,  # right
                    _,  # bottom left
                    TileType.WATER,  # bottom
                    TileType.WATER,  # bottom right
                ):
                    return assets.get_tile_graphic(TileGraphic.COAST_CORNER_TOP_LEFT)
                case (
                    _,  # top left
                    TileType.GRASS,  # top
                    TileType.GRASS,  # top right
                    TileType.WATER,  # left
                    TileType.GRASS,  # right
                    TileType.WATER,  # bottom left
                    TileType.WATER,  # bottom
                    _,  # bottom right
                ):
                    return assets.get_tile_graphic(TileGraphic.COAST_CORNER_TOP_RIGHT)
                case (
                    _,  # top left
                    TileType.WATER,  # top
                    TileType.WATER,  # top right
                    TileType.GRASS,  # left
                    TileType.WATER,  # right
                    TileType.GRASS,  # bottom left
                    TileType.GRASS,  # bottom
                    _,  # bottom right
                ):
                    return assets.get_tile_graphic(TileGraphic.COAST_CORNER_BOTTOM_LEFT)
                case (
                    _,  # top left
                    TileType.WATER,  # top
                    TileType.WATER,  # top right
                    TileType.WATER,  # left
                    TileType.GRASS,  # right
                    _,  # bottom left
                    TileType.GRASS,  # bottom
                    TileType.GRASS,  # bottom right
                ):
                    return assets.get_tile_graphic(TileGraphic.COAST_CORNER_BOTTOM_RIGHT)
                case (
                    TileType.GRASS,  # top left
                    TileType.WATER,  # top
                    TileType.WATER,  # top right
                    TileType.WATER,  # left
                    TileType.WATER,  # right
                    TileType.WATER,  # bottom left
                    TileType.WATER,  # bottom
                    TileType.WATER,  # bottom right
                ):
                    return assets.get_tile_graphic(TileGraphic.COAST_TIP_TOP_LEFT)
                case (
                    TileType.WATER,  # top left
                    TileType.WATER,  # top
                    TileType.WATER,  # top right
                    TileType.WATER,  # left
                    TileType.WATER,  # right
                    TileType.WATER,  # bottom left
                    TileType.WATER,  # bottom
                    TileType.GRASS,  # bottom right
                ):
                    return assets.get_tile_graphic(TileGraphic.COAST_TIP_BOTTOM_RIGHT)
                case (
                    TileType.WATER,  # top left
                    TileType.WATER,  # top
                    TileType.GRASS,  # top right
                    TileType.WATER,  # left
                    TileType.WATER,  # right
                    TileType.WATER,  # bottom left
                    TileType.WATER,  # bottom
                    TileType.WATER,  # bottom right
                ):
                    return assets.get_tile_graphic(TileGraphic.COAST_TIP_TOP_RIGHT)
                case (
                    TileType.WATER,  # top left
                    TileType.WATER,  # top
                    TileType.WATER,  # top right
                    TileType.WATER,  # left
                    TileType.WATER,  # right
                    TileType.GRASS,  # bottom left
                    TileType.WATER,  # bottom
                    TileType.WATER,  # bottom right
                ):
                    return assets.get_tile_graphic(TileGraphic.COAST_TIP_BOTTOM_LEFT)
                case (
                    _,  # top left
                    TileType.GRASS,  # top
                    _,  # top right
                    _,  # left
                    _,  # right
                    _,  # bottom left
                    _,  # bottom
                    _,  # bottom right
                ):
                    return assets.get_tile_graphic(TileGraphic.COAST_TOP)
                case (
                    _,  # top left
                    _,  # top
                    _,  # top right
                    _,  # left
                    _,  # right
                    _,  # bottom left
                    TileType.GRASS,  # bottom
                    _,  # bottom right
                ):
                    return assets.get_tile_graphic(TileGraphic.COAST_BOTTOM)
                case (
                    _,  # top left
                    _,  # top
                    _,  # top right
                    TileType.GRASS,  # left
                    _,  # right
                    _,  # bottom left
                    _,  # bottom
                    _,  # bottom right
                ):
                    return assets.get_tile_graphic(TileGraphic.COAST_LEFT)
                case (
                    _,  # top left
                    _,  # top
                    _,  # top right
                    _,  # left
                    TileType.GRASS,  # right
                    _,  # bottom left
                    _,  # bottom
                    _,  # bottom right
                ):
                    return assets.get_tile_graphic(TileGraphic.COAST_RIGHT)

            return assets.get_tile_graphic(TileGraphic.WATER)


def render_map(map_: Map, camera: Camera, screen: pygame.Surface, assets: AssetManager) -> None:
    position = Point(0.0, 0.0)
    tile_size: Final = Point(25.0, 25.0)
    for row in range(map_.height):
        for column in range(map_.width):
            top_left = camera.world_to_screen(position, screen)
            bottom_right = camera.world_to_screen(
                position + Point(tile_size.x, -tile_size.y),
                screen,
            )
            position += Point(tile_size.x, 0.0)
            if (
                top_left.x >= screen.get_width()
                or top_left.y >= screen.get_height()
                or bottom_right.x < 0.0
                or bottom_right.y < 0.0
            ):
                continue

            graphic = tile_type_to_graphic(map_, IntPoint(column, row), assets)
            width_in_screen_space = abs(bottom_right.x - top_left.x)
            height_in_screen_space = abs(bottom_right.y - top_left.y)

            scaled_graphic = pygame.transform.scale(
                graphic,
                (width_in_screen_space + 1.0, height_in_screen_space + 1.0),
            )
            screen.blit(scaled_graphic, (top_left.x, top_left.y))
        position = Point(0.0, position.y - tile_size.y)


def main() -> None:
    running = True
    camera: Final = Camera()
    delta_time = 1.0 / 60.0
    map_ = Map.generate(
        "Test Map",
        50,
        40,
        river_setting=RiverSetting.YES,
    )
    with create_pygame_context() as context:
        assets: Final = AssetManager()
        while running:
            for event in context.get_events():
                if event.type == pygame.QUIT:
                    running = False
            pressed_keys = context.get_pressed_keys()
            move_speed = 300.0
            zoom_factor = 1.1
            if pressed_keys[pygame.K_w]:
                camera.move(Point(0.0, move_speed) * delta_time)
            if pressed_keys[pygame.K_s]:
                camera.move(Point(0.0, -move_speed) * delta_time)
            if pressed_keys[pygame.K_a]:
                camera.move(Point(-move_speed, 0.0) * delta_time)
            if pressed_keys[pygame.K_d]:
                camera.move(Point(move_speed, 0.0) * delta_time)
            if pressed_keys[pygame.K_q]:
                camera.zoom(1.0 / zoom_factor)
            if pressed_keys[pygame.K_e]:
                camera.zoom(zoom_factor)
            if pressed_keys[pygame.K_ESCAPE]:
                running = False

            context.screen.fill("black")

            render_map(map_, camera, context.screen, assets)

            context.flip()
            delta_time = context.clock.tick(60) / 1000.0


if __name__ == "__main__":
    main()
