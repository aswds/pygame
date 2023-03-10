import pygame
from constans import WIN
class Brick:
    def init(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self):
        pygame.draw.rect(WIN, self.color, (self.x, self.y, self.width, self.height))