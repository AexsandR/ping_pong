from const import WIDHT
class Particle:
    def __init__(self, sc, pygame, x, y, size):
        self.SIZE = size
        self.X = x
        self.size = size
        self.sc = sc
        self.pygame = pygame
        self.x = x
        self.y = y
        self.last = [[x, y, size, size]]
        self.speed = 0.16
    def movent(self, x, y):
        if self.size > 0:
            self.x += x
            self.y += y

    def draw(self):

        if self.size > 0:
            self.pygame.draw.rect(self.sc, "white", (self.x, self.y, self.size, self.size))
            self.size -= self.speed
            if self.x > WIDHT // 2:
                self.movent(-0.5, 0)
            else:
                self.movent(0.5,0)
        else:
            self.size = self.SIZE
            self.x = self.X
            self.pygame.draw.rect(self.sc, "white", (self.x, self.y, self.size, self.size))
