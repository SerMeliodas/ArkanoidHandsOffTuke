import pygame as pg
from effects import Effect


class Powerup(pg.sprite.Sprite):
    def __init__(self, image: str, pos: pg.Vector2):
        super().__init__()

        self.image = pg.image.load('')
        self.rect = self.image.get_rect(center=(
            self.image.get_width() // 2,
            self.image.get_height() // 2
        ))

        self.effect: Effect

    @staticmethod
    def collide_callback_with_paddle(paddle, boost):
        if pg.sprite.collide_rect(paddle, boost):
            boost.kill()

    def update(self):
        ...

    def kill(self):
        self.effect.start()
        super().kill()
