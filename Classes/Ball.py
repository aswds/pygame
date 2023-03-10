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
