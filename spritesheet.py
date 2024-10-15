import pygame as pg


class SpriteSheet:
    def __init__(self, sheet: str, frame_size: tuple[int]):
        self.sheet = pg.image.load(sheet)
        self.frame_size = frame_size

    def get_frame(self, frame_cords: pg.Vector2):
        frame = pg.Surface(self.frame_size).convert_alpha()
        frame.set_colorkey('black')

        frame.blit(self.sheet, (0, 0), (frame_cords.x * self.frame_size[0],
                                        frame_cords.y * self.frame_size[1],
                                        self.frame_size[0], self.frame_size[1])
                   )

        return frame
