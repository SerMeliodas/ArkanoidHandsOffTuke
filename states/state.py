import pygame as pg


class State:
    def __init__(self):
        self.done = False
        self.quit = False
        self.next_state = None

        self.window_rect = pg.display.get_surface().get_rect()

        self.persist = dict()

    def start_up(self, persistent: dict):

        self.persist = persistent

    def get_event(self, event: pg.event.Event): ...

    def update(self, dt: float): ...

    def draw(self, surface: pg.Surface): ...

    def setup(self): ...
