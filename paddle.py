import pygame as pg

BLACK = (0, 0, 0)


class Paddle(pg.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()

        # Create an image of the block, and fill it with a color.
        # Set the background color and set it to be transparent
        self.image = pg.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        # Draw the paddle
        pg.draw.rect(self.image, color, [0, 0, width, height])

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

    def moveLeft(self, pixels):
        self.rect.x -= pixels
        # Check that you are not going too far (off the screen)
        if self.rect.x < 0:
            self.rect.x = 0

    def moveRight(self, pixels):
        self.rect.x += pixels
        # Check that you are not going too far (off the screen)
        if self.rect.x > 700:
            self.rect.x = 700
