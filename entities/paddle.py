import pygame as pg
from spritesheet import SpriteSheet
import config


class Paddle(pg.sprite.Sprite):
    def __init__(self, pos: pg.Vector2):
        super().__init__()

        self.spritesheet = SpriteSheet(
            'assets/spritesheets/paddles.png',
            (32, 9)
        )
        self.image = self.spritesheet.get_frame(pg.Vector2(1, 0))

        self.rect = self.image.get_rect(center=(self.image.get_width() // 2,
                                                self.image.get_height() // 2))

        self.rect.x = pos.x - self.rect.width // 2
        self.rect.bottom = pos.y
        self._speed = 180
        self._velocity = pg.Vector2(0, 0)

    def input(self):
        keys = pg.key.get_pressed()

        if keys[eval(f'pg.K_{config.KEY_LEFT}')]:
            self._velocity.x = -1

        elif keys[eval(f'pg.K_{config.KEY_RIGHT}')]:
            self._velocity.x = 1

        else:
            self._velocity.x = 0

    def update(self, dt: float):
        self.input()

        self.rect.x += self._velocity.x * dt * self._speed

        if self.rect.right > config.SCREEN_WIDTH:
            self.rect.right = config.SCREEN_WIDTH

        if self.rect.left < 0:
            self.rect.left = 0
