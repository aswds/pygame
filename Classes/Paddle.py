import pygame

from constans import WIDTH, WIN


class Paddle:
    # INITIALIZATION
    def __init__(self, x, y, width, height, color, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.speed = speed

    # DISPLAY THE PADDLE
    def draw(self):
        pygame.draw.rect(WIN, self.color, (self.x, self.y, self.width, self.height))

    # MOVE PADDLE LEFT
    def move_left(self):
        self.x = max(0, self.x - self.speed)

    # MOVE PADDLE RIGHT
    def move_right(self):
        self.x = min(WIDTH - self.width, self.x + self.speed)
