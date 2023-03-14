from Classes.Ball import Ball
from Classes.Brick import Brick
from Classes.Paddle import Paddle
from constans import *
import pygame

# Initialize Pygame
pygame.init()
pygame.font.init()


def main(ball_speed):
    ball = Ball(WIDTH / 2, HEIGHT - 200, BALL_RADIUS, BLUE, ball_speed, -45)
    paddle = Paddle(WIDTH / 2 - PADDLE_WIDTH / 2, HEIGHT - PADDLE_HEIGHT, PADDLE_WIDTH, PADDLE_HEIGHT, GREEN, 50)
    bricks = [[Brick(j * (BRICK_WIDTH + BRICK_MARGIN) + BRICK_MARGIN, i * (BRICK_HEIGHT + BRICK_MARGIN) + BRICK_MARGIN,
                     BRICK_WIDTH, BRICK_HEIGHT, RED) for j in range(BRICK_COLS)] for i in range(BRICK_ROWS)]
    # Set up the font
    font = pygame.font.Font(None, FONT_SIZE)
    running = True
    game_over = False
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    paddle.move_left()
                if event.key == pygame.K_RIGHT:
                    paddle.move_right()
        # Move the ball
        ball.move()

        # Check for collisions
        ball.check_wall_collision()
        ball.check_paddle_collision(paddle)
        ball.check_brick_collision(bricks)
        if ball.check_bottom_collision():
            game_over = True
        # Clear the screen
        WIN.fill(BLACK)

        # Draw the objects
        ball.draw()
        paddle.draw()
        for i in range(BRICK_ROWS):
            for j in range(BRICK_COLS):
                if bricks[i][j] is not None:
                    bricks[i][j].draw()
        # Draw the score
        score_text = font.render(f"Score: {ball.score}", True, WHITE)
        WIN.blit(score_text, (10, 10))

        # Update the screen
        pygame.display.update()

        # Check game over
        if game_over:
            game_over_text = font.render(f"Game Over", True, WHITE)
            score_text = font.render(f"Score: {ball.score}", True, RED)
            WIN.blit(game_over_text, (WIDTH / 2 - FONT_SIZE * 3, HEIGHT / 2 - FONT_SIZE))
            WIN.blit(score_text, (WIDTH / 2 - FONT_SIZE * 3, HEIGHT / 2 + FONT_SIZE))
            pygame.display.update()
            pygame.time.delay(1000)
            running = False
        # Quit Pygame
    pygame.quit()

