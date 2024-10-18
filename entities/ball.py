import config
from spritesheet import SpriteSheet
import pygame as pg


class Ball(pg.sprite.Sprite):
    pg.mixer.init()
    hit_sound = pg.mixer.Sound('assets/sounds/hit.wav')
    bound_sound = pg.mixer.Sound('assets/sounds/bound.wav')

    hit_sound.set_volume(0.5)
    bound_sound.set_volume(0.5)

    def __init__(self, pos: pg.Vector2):
        super().__init__()
        self.spritesheet = SpriteSheet(
            'assets/spritesheets/balls.png',
            (8, 8)
        )

        self.image = self.spritesheet.get_frame(pg.Vector2(1, 0))

        self.rect = self.image.get_rect(center=(self.image.get_width() // 2,
                                                self.image.get_height() // 2))

        self.rect.center = pos

        self._speed = 100
        self._velocity = pg.Vector2(1, -1)

    @property
    def velocity(self):
        return self._velocity

    @velocity.setter
    def velocity(self, value: pg.Vector2):
        if not isinstance(value, pg.Vector2):
            raise ValueError('velocity must be a Vector2')
        self._velocity = value

    @staticmethod
    def collide_callback_with_bricks(ball, brick):
        if pg.sprite.collide_rect(ball, brick):
            ball.hit_sound.play()
            ball.velocity = pg.Vector2(
                ball.velocity.x, 1)
            brick.hits += 1

            if brick.hits == brick.max_hits:
                brick.kill()

            brick.update_image()

    def update(self, dt: float):
        self.rect.x += self._velocity.x * self._speed * dt
        self.rect.y += self._velocity.y * self._speed * dt

        if self.rect.right >= config.SCREEN_WIDTH:
            self.bound_sound.play()
            self._velocity.x = -1

        if self.rect.left <= 0:
            self.bound_sound.play()
            self._velocity.x = 1

        if self.rect.bottom >= config.SCREEN_HEIGHT:
            self.kill()

        if self.rect.top <= 0:
            self.bound_sound.play()
            self._velocity.y = 1
