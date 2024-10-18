from ..state import State
import sys
import pygame as pg
from entities import Button
from spritesheet import SpriteSheet
import config


class WinMenuState(State):
    def __init__(self):
        super().__init__()

        self.spritesheet = SpriteSheet(
            'assets/spritesheets/buttons.png',
            (64, 16)
        )

        self.text = config.FONT.render('You passed this level', False, 'white')
        self.text_rect = self.text.get_rect()

        self.buttons_surface = pg.Surface((64 + 2 * 2, 16*2 + 2 * 3))
        self.rect = self.buttons_surface.get_rect(center=(
            self.buttons_surface.get_width() // 2,
            self.buttons_surface.get_height() // 2
        ))

        self.rect.center = self.window_rect.center

        self.text_rect.centerx = self.window_rect.centerx
        self.text_rect.centery = self.window_rect.centery - \
            self.buttons_surface.get_height() - 20

        self.next_state = 'level_menu'
        self._setup_buttons()

    def _setup_buttons(self):
        self.continue_button = Button(self.spritesheet.get_frame(
            pg.Vector2(1, 0)
        ), pg.Vector2(2, 2), 'Levels')

        self.quit_button = Button(self.spritesheet.get_frame(
            pg.Vector2(2, 0)
        ), pg.Vector2(2, 18), 'Quit')

        self.buttons_surface.blit(self.continue_button.image,
                                  self.continue_button.rect)
        self.buttons_surface.blit(
            self.quit_button.image, self.quit_button.rect)

    def get_event(self, event: pg.event.Event):
        if event.type == pg.KEYDOWN and event.key == pg.K_RETURN:
            self.done = True

        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            if self.continue_button.rect.collidepoint(event.pos[0] - self.rect.x,
                                                      event.pos[1] - self.rect.y):
                self.done = True

            if self.quit_button.rect.collidepoint(event.pos[0] - self.rect.x,
                                                  event.pos[1] - self.rect.y):
                sys.exit()

    def draw(self, surface):
        surface.blit(self.buttons_surface, self.rect)
        surface.blit(self.text, self.text_rect)
