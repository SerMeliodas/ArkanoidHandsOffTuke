from .state import State
from random import randint
import pygame as pg
import config
import sys
from entities import Ball, Paddle, Brick, Button
from spritesheet import SpriteSheet


class GameplayState(State):
    def __init__(self):
        super().__init__()

        self.balls = pg.sprite.Group()
        self.bricks = pg.sprite.Group()
        self.background = SpriteSheet(
            'assets/spritesheets/Backround_Tiles.png', (32, 100)
        ).get_frame(pg.Vector2(randint(1, 8), 0))
        self.background = pg.transform.scale_by(self.background, 11)

        self.back_rect = self.background.get_rect(center=(
            self.background.get_width() // 2,
            self.background.get_height() // 2
        ))
        self.back_rect.center = self.window_rect.center

    def setup(self):
        if self.persist.get('level'):
            self.bricks = self.persist['level']['bricks']
            self.paddle = self.persist['level']['paddle']
            self.balls = self.persist['level']['balls']
            return

        self.paddle = Paddle(pg.Vector2(
            self.window_rect.width // 2, self.window_rect.height))

        self.ball = Ball(pg.Vector2(self.window_rect.width //
                         2, self.window_rect.height // 2))
        self.balls.add(self.ball)
        self._setup_bricks()

    def _setup_bricks(self):
        for col in range(10):
            for row in range(5):
                brick = Brick(pg.Vector2(
                    col * 32 + config.BRICK_MARGIN * col + config.BRICK_MARGIN,
                    row * 16 + config.BRICK_MARGIN * row + config.BRICK_MARGIN
                ))

                self.bricks.add(brick)

    def get_event(self, event: pg.event.Event):
        if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            self.next_state = 'pause_menu'
            self.persist['level'] = {
                'bricks': self.bricks,
                'paddle': self.paddle,
                'balls': self.balls,
                'ball': self.ball,
            }
            self.done = True

    def draw(self, surface: pg.Surface):
        surface.blit(self.background, self.back_rect)
        surface.blit(self.paddle.image, self.paddle.rect)

        self.balls.draw(surface)
        self.bricks.draw(surface)

    def update(self, dt: float):
        self.paddle.update(dt)
        self.ball.update(dt)
        self.bricks.update(dt)

        pg.sprite.spritecollide(
            self.ball, self.bricks, dokill=False, collided=Ball.collide_callback_with_bricks
        )

        if pg.sprite.collide_rect(self.paddle, self.ball):
            self.ball.velocity = pg.Vector2(
                self.ball.velocity.x, -1)

        if len(self.balls) == 0:
            self.next_state = "game_over"
            self.quit = True


class GameOverState(State):
    def __init__(self):
        super().__init__()

        self.spritesheet = SpriteSheet(
            'assets/spritesheets/buttons.png',
            (64, 16)
        )

        self.surface = pg.Surface((64 + 2 * 2, 16*2 + 2 * 3))
        self.rect = self.surface.get_rect(center=(
            self.surface.get_width() // 2,
            self.surface.get_height() // 2
        ))

        self.rect.center = self.window_rect.center
        self.next_state = 'gameplay'
        self._setup_buttons()

    def _setup_buttons(self):
        self.restart_button = Button(self.spritesheet.get_frame(
            pg.Vector2(1, 0)
        ), pg.Vector2(2, 2), 'Restart')

        self.quit_button = Button(self.spritesheet.get_frame(
            pg.Vector2(2, 0)
        ), pg.Vector2(2, 18), 'Quit')

        self.surface.blit(self.restart_button.image, self.restart_button.rect)
        self.surface.blit(self.quit_button.image, self.quit_button.rect)

    def get_event(self, event: pg.event.Event):
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            if self.restart_button.rect.collidepoint(event.pos[0] - self.rect.x,
                                                     event.pos[1] - self.rect.y):
                if self.persist.get('level'):
                    self.persist['level']['ball'].kill()
                    self.persist['level']['bricks'].empty()
                    del self.persist['level']

                self.done = True

            if self.quit_button.rect.collidepoint(event.pos[0] - self.rect.x,
                                                  event.pos[1] - self.rect.y):
                sys.exit()

    def draw(self, surface: pg.Surface):
        surface.blit(self.surface, self.rect)
