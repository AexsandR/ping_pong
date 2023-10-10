from const import *


class Player:
    def __init__(self, sc, pygame, x, y):
        self.sc = sc
        self.pygame = pygame
        self.x = x
        self.y = y
        self.height = 150
        self.widht = 30

    def draw(self):
        self.pygame.draw.rect(self.sc, "white", (self.x, self.y, self.widht, self.height))

    def return_cord(self):
        if self.x < 100:
            return [self.x + self.widht, self.y, self.y + self.height]
        return [self.x, self.y, self.y + self.height]

    def movent(self, y):
        if HEIGHT - self.height >= self.y + y >= 0:
            self.y += y

    def move(self, y):
        self.y = y
