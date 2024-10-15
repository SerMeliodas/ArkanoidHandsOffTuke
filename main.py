from game import Game
import pygame as pg
from states import GameplayState, GameOverState, MainMenuState, PauseMenuState
import config


if __name__ == "__main__":
    pg.init()
    window = pg.display.set_mode((config.SCREEN_WIDTH,
                                  config.SCREEN_HEIGHT,),
                                 flags=pg.SCALED)
    states = {
        "gameplay": GameplayState(),
        "game_over": GameOverState(),
        "main_menu": MainMenuState(),
        "pause_menu": PauseMenuState(),
    }
    game = Game(window,
                states, "main_menu")

    game.run()
