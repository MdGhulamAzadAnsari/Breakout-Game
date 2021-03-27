import pygame as pg
BLACK = (0, 0, 0)


class Brick(pg.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()

        self.image = pg.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        # Draw the brick (a rectangle!)
        pg.draw.rect(self.image, color, [0, 0, width, height])

        self.rect = self.image.get_rect()
