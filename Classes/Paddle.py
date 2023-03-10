import pygame


class Paddle:
    def __init__(self, x, y, width, height, color, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.speed = speed

    def draw(self):
        pygame.draw.rect(None, self.color, (self.x, self.y, self.width, self.height))
