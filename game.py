import sys
import pygame as pg

import config

from states import State


class Game:
    def __init__(self, window: pg.Surface, states: dict, start_state: str):
        self.window = window

        self.clock = pg.time.Clock()

        self.states: dict = states
        self.state_name: str = start_state
        self.state: State = self.states[self.state_name]

    def event_loop(self):
        for event in pg.event.get():
            if event.type is pg.QUIT:
                sys.exit()

            self.state.get_event(event)

    def flip_state(self):
        next = self.state.next_state
        self.state.done = False
        self.state.quit = False
        self.state_name = next
        persistent = self.state.persist
        self.state = self.states[self.state_name]
        self.state.start_up(persistent)
        self.state.setup()

    def update(self, dt: float):

        if self.state.quit:
            self.state.done = True

        if self.state.done:
            self.flip_state()

        self.state.update(dt)

    def run(self):
        while True:
            dt = self.clock.tick(config.FPS) / 1000
            self.event_loop()
            self.window.fill('black')
            self.state.draw(self.window)

            self.update(dt)

            pg.display.update()
