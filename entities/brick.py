import pygame as pg
from spritesheet import SpriteSheet


class Brick(pg.sprite.Sprite):
    def __init__(self, pos: pg.Vector2 = pg.Vector2(0, 0)):
        super().__init__()
        self.spritesheet = SpriteSheet(
            'assets/spritesheets/bricks32_16.png',
            (32, 16)
        )
        self.hits = 0
        self.image = self.spritesheet.get_frame(pg.Vector2(self.hits, 1))
        self.rect = self.image.get_rect(center=(
            self.image.get_width() // 2,
            self.image.get_height() // 2
        ))

        self.rect.x = pos.x
        self.rect.y = pos.y

    def update_image(self):
        self.image = self.spritesheet.get_frame(pg.Vector2(self.hits, 1))
