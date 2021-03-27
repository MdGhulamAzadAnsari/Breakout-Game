import pygame as pg
from random import randint
BLACK = (0, 0, 0)


class Ball(pg.sprite.Sprite):
    def __init__(self, color, radius):
        super().__init__()

        self.image = pg.Surface([radius, radius])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        half_radius = radius/2
        # Draw the ball (a circlr!)
        pg.draw.circle(self.image, color,
                       (half_radius, half_radius), half_radius)

        self.velocity = [randint(4, 8), randint(-4, 4)]

        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-2, 2)
