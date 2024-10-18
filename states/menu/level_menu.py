from ..state import State
import pygame as pg
from level import Level
import pathlib
from entities import LevelButton
from spritesheet import SpriteSheet


class LevelMenuState(State):
    def __init__(self):
        super().__init__()
        self.levels = []

        self.button_spritesheet = SpriteSheet(
            'assets/spritesheets/buttons.png',
            (64, 16)
        )

        self.image = self.button_spritesheet.get_frame(
            pg.Vector2(0, 0)
        )

        self._buttons_margin = 2

        self.button_group = pg.sprite.Group()

        self.next_state = 'gameplay'

        self._load_all_levels()
        self._setup_buttons()

    def _load_all_levels(self):
        directory = pathlib.Path('levels/')
        files = [
            entry if entry.is_file() else ... for entry in directory.iterdir()
        ]

        for file in files:
            self.levels.append(Level(file))

    def _setup_buttons(self):
        for index, level in enumerate(self.levels):
            btn = LevelButton(
                self.image,
                pg.Vector2(
                    index * self.image.get_width() + (index + 1) * self._buttons_margin,
                    index // (self.window_rect.width // self.image.get_width())
                ),
                level.name,
                index
            )

            self.button_group.add(btn)

    def draw(self, surface: pg.Surface):
        self.button_group.draw(surface)

    def get_event(self, event: pg.event.Event):
        if event.type == pg.MOUSEBUTTONUP and event.button == 1:
            for btn in self.button_group.sprites():
                if btn.rect.collidepoint(event.pos[0], event.pos[1]):
                    self.persist['level'] = self.levels[btn.level_index]
                    self.done = True
