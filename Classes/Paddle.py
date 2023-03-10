import pygame

from constans import WIDTH, WIN
class Paddle:
    def __init__(self, x, y, width, height, color, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.speed = speed

    def draw(self):
        pygame.draw.rect(WIN, self.color, (self.x, self.y, self.width, self.height))

    def move_left(self):
        self.x = max(0, self.x - self.speed)

    def move_right(self):
        self.x = min(WIDTH - self.width, self.x + self.speed)