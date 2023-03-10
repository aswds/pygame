import pygame
from Classes.Ball import Ball
from Classes.Brick import Brick
from Classes.Paddle import Paddle
from constans import *

def main():
    ball = Ball(WIDTH / 2, HEIGHT - 200, BALL_RADIUS, BLUE, 0.2, -45)
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
