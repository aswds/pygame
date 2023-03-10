import pygame


#Window options
WIDTH, HEIGHT = 600, 800

#Game options
BALL_RADIUS = 10
PADDLE_WIDTH, PADDLE_HEIGHT = 100, 20
BRICK_WIDTH, BRICK_HEIGHT = 50, 20
BRICK_ROWS, BRICK_COLS = 5, 10
BRICK_MARGIN = 10
FONT_SIZE = 40

# Set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


WIN = pygame.display.set_mode((WIDTH, HEIGHT))