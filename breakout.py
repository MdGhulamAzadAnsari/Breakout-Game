import pygame as pg
from paddle import Paddle
from ball import Ball
from brick import Brick

# ---------------------------- CONSTANTS ------------------------------- #
WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
DARKBLUE = (36, 90, 190)
LIGHTBLUE = (0, 176, 240)
RED = (255, 0, 0)
ORANGE = (255, 100, 0)
YELLOW = (255, 255, 0)

# Initialise the game engine
pg.init()


score = 0
lives = 3

# Create the screen
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('Breakout')

# This will be a list that will contain all the sprites we intend to use in our game.
all_sprites_list = pg.sprite.Group()

# Create the Paddle
paddle = Paddle(LIGHTBLUE, 100, 10)
paddle.rect.x = 350
paddle.rect.y = 560

# Create the ball sprite
ball = Ball(WHITE, 16)
ball.rect.x = 345
ball.rect.y = 195

# Create the bricks
all_bricks = pg.sprite.Group()
for i in range(7):
    brick = Brick(RED, 80, 30)
    brick.rect.x = 60 + i * 100
    brick.rect.y = 60
    all_sprites_list.add(brick)
    all_bricks.add(brick)
for i in range(7):
    brick = Brick(ORANGE, 80, 30)
    brick.rect.x = 60 + i * 100
    brick.rect.y = 100
    all_sprites_list.add(brick)
    all_bricks.add(brick)
for i in range(7):
    brick = Brick(YELLOW, 80, 30)
    brick.rect.x = 60 + i * 100
    brick.rect.y = 140
    all_sprites_list.add(brick)
    all_bricks.add(brick)

# Add the paddle to the list of sprites
all_sprites_list.add(paddle)
all_sprites_list.add(ball)

# The clock will be used to control how fast the screen updates
clock = pg.time.Clock()

# The loop will carry on until the user exit the game
isGameOver = False

# -------- Main Game Loop ----------- #
while not isGameOver:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            isGameOver = True
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_x:
                isGameOver = True
    # Moving the paddle when the use uses the arrow keys
    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT]:
        paddle.moveLeft(5)
    if keys[pg.K_RIGHT]:
        paddle.moveRight(5)

    # --- Game logic should go here
    all_sprites_list.update()

    # Check if the ball is bouncing against any of the 4 walls:
    if ball.rect.x >= 790:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x <= 0:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y > 590:
        ball.velocity[1] = -ball.velocity[1]
        lives -= 1
        if lives == 0:
            font = pg.font.Font(None, 74)
            text = font.render("GAME OVER", 1, WHITE)
            screen.blit(text, (250, 300))
            pg.display.flip()
            pg.time.wait(3000)

            # Stop the Game
            isGameOver = True
    if ball.rect.y < 40:
        ball.velocity[1] = -ball.velocity[1]

    # Detect collisions between the ball and the paddles
    if pg.sprite.collide_mask(ball, paddle):
        ball.rect.x -= ball.velocity[0]
        ball.rect.y -= ball.velocity[1]
        ball.bounce()

    # Check if there is the ball collides with any of bricks
    brick_collision_list = pg.sprite.spritecollide(ball, all_bricks, False)
    for brick in brick_collision_list:
        ball.bounce()
        score += 1
        brick.kill()
        if len(all_bricks) == 0:
            # Display Level Complete Message for 3 seconds
            font = pg.font.Font(None, 74)
            text = font.render("LEVEL COMPLETE", 1, WHITE)
            screen.blit(text, (200, 300))
            pg.display.flip()
            pg.time.wait(3000)

            # Stop the Game
            isGameOver = True

    # Fill The background color
    screen.fill(DARKBLUE)
    pg.draw.line(screen, WHITE, [0, 38], [800, 38], 2)

    # Display the score and the number of lives at the top of the screen
    font = pg.font.Font(None, 34)
    text = font.render(f"Score: {score}", 1, WHITE)
    screen.blit(text, (20, 10))
    text = font.render(f"Lives: {lives}", 1, WHITE)
    screen.blit(text, (650, 10))

    # Now let's draw all the sprites in one go.
    all_sprites_list.draw(screen)

    # --- Go ahead and update the screen with what we've drawn.
    pg.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Once we have exited the main program loop we can stop the game engine:
pg.quit()
