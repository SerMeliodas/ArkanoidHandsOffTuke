from ..state import State
from random import randint
import pygame as pg
from level import Level
from entities import Ball, Paddle
from spritesheet import SpriteSheet


class GameplayState(State):
    def __init__(self):
        super().__init__()

        self.balls = pg.sprite.Group()

        self.level: Level

        self.background = SpriteSheet(
            'assets/spritesheets/Backround_Tiles.png', (32, 100)
        ).get_frame(pg.Vector2(randint(0, 7), 0))
        self.background = pg.transform.scale_by(self.background, 11)

        self.back_rect = self.background.get_rect(center=(
            self.background.get_width() // 2,
            self.background.get_height() // 2
        ))

        self.back_rect.center = self.window_rect.center

        self.start_sound = pg.mixer.Sound('assets/sounds/round_start.mp3')
        self.ost = pg.mixer.Sound('assets/sounds/ost.mp3')
        self.ost.set_volume(0.1)

    def gen_persist(self):
        self.persist['level'] = self.level
        self.persist['balls'] = self.balls
        self.persist['ball'] = self.ball
        self.persist['ost'] = self.ost
        self.persist['paddle'] = self.paddle

    def setup(self):

        if self.persist.get('level'):
            self.level = self.persist['level']
            self.level.setup()

        if self.persist.get('ball') and self.persist.get('paddle') and self.persist.get('balls'):
            self.ball = self.persist['ball']
            self.balls = self.persist['balls']
            self.paddle = self.persist['paddle']
            self.level.setup()
            return

        self.start_sound.play()
        self.ost.play(loops=-1)

        self.paddle = Paddle(pg.Vector2(
            self.window_rect.width // 2, self.window_rect.height))

        self.ball = Ball(pg.Vector2(self.window_rect.width //
                         2, self.window_rect.height // 2))
        self.balls.add(self.ball)

    def get_event(self, event: pg.event.Event):
        if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            self.next_state = 'pause_menu'
            self.gen_persist()
            self.done = True

    def draw(self, surface: pg.Surface):
        surface.blit(self.background, self.back_rect)
        surface.blit(self.paddle.image, self.paddle.rect)

        self.balls.draw(surface)
        self.level.bricks.draw(surface)

    def update(self, dt: float):
        self.paddle.update(dt)
        self.ball.update(dt)
        self.level.bricks.update(dt)

        pg.sprite.spritecollide(
            self.ball, self.level.bricks, dokill=False, collided=Ball.collide_callback_with_bricks
        )

        if pg.sprite.collide_rect(self.paddle, self.ball):
            self.ball.bound_sound.play()
            self.ball.velocity = pg.Vector2(
                self.ball.velocity.x, -1)

        if len(self.level.bricks.sprites()) == 0:
            self.ost.stop()
            self.next_state = "win"
            self.gen_persist()
            self.quit = True

        if len(self.balls) == 0:
            self.ost.stop()
            self.next_state = "game_over"
            self.gen_persist()
            self.quit = True
