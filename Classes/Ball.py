import pygame
from constans import WIN, BRICK_COLS, BRICK_ROWS, BRICK_HEIGHT, BRICK_WIDTH, WIDTH, HEIGHT


class Ball:
    def __init__(self, x, y, radius, color, speed, angle):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed = speed
        self.angle = angle
        self.dx = speed
        self.dy = -speed

    def draw(self):
        pygame.draw.circle(WIN, self.color, (int(self.x), int(self.y)), self.radius)

    def move(self):
        self.x += self.dx
        self.y += self.dy

    def check_wall_collision(self):
        if self.x - self.radius < 0 or self.x + self.radius > WIDTH:
            self.dx = -self.dx
        if self.y - self.radius < 0:
            self.dy = -self.dy

    def check_paddle_collision(self, paddle):
        if self.y + self.radius > paddle.y and self.x + self.radius > paddle.x and self.x - self.radius < paddle.x + paddle.width:
            self.dy = -self.dy

    def check_brick_collision(self, bricks):
        for i in range(BRICK_ROWS):
            for j in range(BRICK_COLS):
                brick = bricks[i][j]
                if brick is not None and self.y - self.radius < brick.y + BRICK_HEIGHT and self.x + self.radius > brick.x and self.x - self.radius < brick.x + BRICK_WIDTH:
                    self.dy = -self.dy
                    bricks[i][j] = None

    def check_bottom_collision(self):
        if self.y + self.radius > HEIGHT:
            return True
        return False
