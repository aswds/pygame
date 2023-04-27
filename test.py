import pytest
from Classes.Ball import Ball
from Classes.Brick import Brick
from Classes.Paddle import Paddle
from constans import *
import pygame
from main import main_menu as main

# Initialize Pygame
pygame.init()
pygame.font.init()


# Set up a fixture for the game objects
@pytest.fixture
def game_objects():
    ball = Ball(WIDTH / 2, HEIGHT - 200, BALL_RADIUS, BLUE, 5, -45)
    paddle = Paddle(WIDTH / 2 - PADDLE_WIDTH / 2, HEIGHT - PADDLE_HEIGHT, PADDLE_WIDTH, PADDLE_HEIGHT, GREEN, 50)
    bricks = [[Brick(j * (BRICK_WIDTH + BRICK_MARGIN) + BRICK_MARGIN, i * (BRICK_HEIGHT + BRICK_MARGIN) + BRICK_MARGIN,
                     BRICK_WIDTH, BRICK_HEIGHT, RED) for j in range(BRICK_COLS)] for i in range(BRICK_ROWS)]
    font = pygame.font.Font(None, FONT_SIZE)
    return ball, paddle, bricks, font


# Test the ball's move() method
def test_ball_move(game_objects):
    ball, _, _, _ = game_objects
    start_x = ball.x
    start_y = ball.y
    ball.move()
    assert ball.x != start_x or ball.y != start_y


# Test the paddle's move_left() method
def test_paddle_move_left(game_objects):
    _, paddle, _, _ = game_objects
    start_x = paddle.x
    paddle.move_left()
    assert paddle.x < start_x


# Test the paddle's move_right() method
def test_paddle_move_right(game_objects):
    _, paddle, _, _ = game_objects
    start_x = paddle.x
    paddle.move_right()
    assert paddle.x > start_x


# Test the ball's check_wall_collision() method
def test_ball_check_wall_collision(game_objects):
    ball, _, _, _ = game_objects
    ball.x = WIDTH + 10
    ball.check_wall_collision()
    assert ball.dx < 0 and ball.x == WIDTH + ball.radius


# Test the ball's check_paddle_collision() method
def test_ball_check_paddle_collision(game_objects):
    ball, paddle, _, _ = game_objects
    ball.y = HEIGHT - PADDLE_HEIGHT - ball.radius
    ball.check_paddle_collision(paddle)
    assert ball.dy < 0 and ball.y == HEIGHT - PADDLE_HEIGHT - ball.radius


# Test the ball's check_brick_collision() method
def test_ball_check_brick_collision(game_objects):
    ball, _, bricks, _ = game_objects
    for i in range(BRICK_ROWS):
        for j in range(BRICK_COLS):
            if bricks[i][j] is not None:
                brick = bricks[i][j]
                ball.x = brick.x + brick.width / 2
                ball.y = brick.y + brick.height / 2
                ball.dx = 5
                ball.dy = -5
                ball.check_brick_collision(bricks)
                assert bricks[i][j] is None


# Test the ball's check_bottom_collision() method
def test_ball_check_bottom_collision(game_objects):
    ball, _, _, _ = game_objects
    ball.y = HEIGHT + ball.radius
    assert ball.check_bottom_collision()


# Test the main function
def test_main():
    main()
    # Check that Pygame quit without errors
    assert pygame.get_init() == False