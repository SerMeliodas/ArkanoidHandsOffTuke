import pygame as pg
import config


class Button(pg.sprite.Sprite):
    def __init__(self, image: pg.Surface, pos: pg.Vector2, text: str):
        super().__init__()

        self.image = image
        self.rect = self.image.get_rect(center=(
            self.image.get_width() // 2,
            self.image.get_height() // 2
        ))

        self.text = config.FONT.render(text, False, 'white')
        self.text_rect = self.text.get_rect(center=(
            self.text.get_width() // 2,
            self.text.get_height() // 2
        ))

        self.text_rect.center = pg.Vector2(
            self.rect.center[0], self.rect.center[1] - 2)

        self.image.blit(self.text, self.text_rect)

        self.rect.x = pos.x
        self.rect.y = pos.y


class LevelButton(Button):
    def __init__(self, image: pg.Surface, pos: pg.Vector2, text: str, level_index: int):
        super().__init__(image, pos, text)

        self.level_index = level_index
