from ..state import State
import sys
import pygame as pg
from spritesheet import SpriteSheet
from entities import Button


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
        self.game_over_sound = pg.mixer.Sound('assets/sounds/game_over.mp3')
        self._setup_buttons()

    def start_up(self, persist):
        super().start_up(persist)

        self.game_over_sound.play()

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
                    self.persist['ball'].kill()
                    self.persist['level'].bricks.empty()
                    del self.persist['ball']

                self.done = True

            if self.quit_button.rect.collidepoint(event.pos[0] - self.rect.x,
                                                  event.pos[1] - self.rect.y):
                sys.exit()

    def draw(self, surface: pg.Surface):
        surface.blit(self.surface, self.rect)
