from collections.abc import Generator
from contextlib import contextmanager
from typing import Final
from typing import NamedTuple
from typing import final

import pygame
from pygame.key import ScancodeWrapper


@final
class PygameContext(NamedTuple):
    screen: pygame.Surface
    clock: pygame.time.Clock

    def flip(self) -> None:
        pygame.display.flip()

    def get_events(self) -> list[pygame.event.Event]:
        return pygame.event.get()

    def get_pressed_keys(self) -> ScancodeWrapper:
        return pygame.key.get_pressed()


@contextmanager
def create_pygame_context() -> Generator[PygameContext]:
    try:
        pygame.init()
        screen: Final = pygame.display.set_mode((1280, 720))
        clock: Final = pygame.time.Clock()
        yield PygameContext(
            screen=screen,
            clock=clock,
        )
    finally:
        pygame.quit()
