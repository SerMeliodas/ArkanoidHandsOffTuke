import pygame as pg
import config
from entities import Brick
from utils import parse_level


class Level:
    def __init__(self, level_file: str):
        self.level_data = parse_level(level_file)

        self.bricks: pg.sprite.Group = pg.sprite.Group()
        self.index = self.level_data['index']
        self.name = self.level_data['name']

    def _create_bricks(self):
        for row_index, row in enumerate(self.level_data['map']):
            for col_index, col in enumerate(row):
                brick = Brick(
                    pg.Vector2(
                        col_index * 32 + config.BRICK_MARGIN * (col_index + 1),
                        row_index * 16 + config.BRICK_MARGIN * (row_index + 1)
                    ),
                    col['hits'],
                    Brick.colors[col['color']]
                )

                self.bricks.add(brick)

    def setup(self):
        self._create_bricks()
