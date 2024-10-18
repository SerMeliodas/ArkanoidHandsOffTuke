from ..state import State
import pygame as pg
import sys
from entities import Button
from spritesheet import SpriteSheet


class PauseMenuState(State):
    def __init__(self):
        super().__init__()

        self.spritesheet = SpriteSheet(
            'assets/spritesheets/buttons.png',
            (64, 16)
        )

        self.buttons_surface = pg.Surface((64 + 2 * 2, 16*3 + 2 * 4))
        self.rect = self.buttons_surface.get_rect(center=(
            self.buttons_surface.get_width() // 2,
            self.buttons_surface.get_height() // 2
        ))

        self.rect.center = self.window_rect.center
        self.next_state = 'gameplay'
        self._setup_buttons()

    def _setup_buttons(self):
        self.continue_button = Button(self.spritesheet.get_frame(
            pg.Vector2(1, 0)
        ), pg.Vector2(2, 2), 'Continue')

        self.restart_button = Button(self.spritesheet.get_frame(
            pg.Vector2(3, 0)
        ), pg.Vector2(2, 18), 'Restart')

        self.quit_button = Button(self.spritesheet.get_frame(
            pg.Vector2(2, 0)
        ), pg.Vector2(2, 36), 'Quit')

        self.buttons_surface.blit(self.continue_button.image,
                                  self.continue_button.rect)
        self.buttons_surface.blit(
            self.quit_button.image, self.quit_button.rect)
        self.buttons_surface.blit(
            self.restart_button.image, self.restart_button.rect)

    def get_event(self, event: pg.event.Event):
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            if self.continue_button.rect.collidepoint(event.pos[0] - self.rect.x,
                                                      event.pos[1] - self.rect.y):
                self.done = True

            if self.quit_button.rect.collidepoint(event.pos[0] - self.rect.x,
                                                  event.pos[1] - self.rect.y):
                sys.exit()

            if self.restart_button.rect.collidepoint(event.pos[0] - self.rect.x,
                                                     event.pos[1] - self.rect.y):
                self.persist['ost'].stop()
                self.persist['ball'].kill()
                self.persist['level'].bricks.empty()
                self.done = True

    def draw(self, surface):
        surface.blit(self.buttons_surface, self.rect)
