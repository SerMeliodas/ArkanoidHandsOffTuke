import pygame as pg
from spritesheet import SpriteSheet


class Brick(pg.sprite.Sprite):
    colors = {
        'gray': 0,
        'green': 1,
        'yellow': 2,
        'orange': 3,
        'red': 4,
        'purple': 5
    }

    def __init__(self, pos: pg.Vector2, max_hits: int = 3, color: int = 0):
        super().__init__()

        self.spritesheet = SpriteSheet(
            'assets/spritesheets/bricks32_16.png',
            (32, 16)
        )

        self.hits = 0
        self.max_hits = max_hits

        self.color = color

        self.image = self.spritesheet.get_frame(
            pg.Vector2(self.hits, self.color))

        self.rect = self.image.get_rect(center=(
            self.image.get_width() // 2,
            self.image.get_height() // 2
        ))

        self.rect.x = pos.x
        self.rect.y = pos.y

    def update_image(self):
        self.image = self.spritesheet.get_frame(
            pg.Vector2(self.hits, self.color))
