import pygame as pg
from utils import parse_level


class Level:
    def __init__(self, level_file: str):
        self.level_data = parse_level(level_file)

        self.background: pg.Surface = pg.image.load(
            self.level_data['background']
        )

        self.bricks: pg.sprite.Group

    def setup(self):
        ...

    def draw(self):
        ...

    def update(self, dt: float):
        ...
