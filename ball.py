import math
import random
from const import *
from particle import Particle


class Ball:
    def __init__(self, pygame, sc, x, y):
        self.pygame = pygame
        self.sc = sc
        self.x = x
        self.y = y
        self.size = 20
        self.direction_x = random.choice(["right", "left"])
        self.direction_y = random.choice(["up", "down"])
        self.angle = random.randint(25, 75) / 180 * math.pi
        self.speed = 2
        self.particls_right = self.generation_particals(1240)
        self.particls_left = self.generation_particals(0)

    def generation_particals(self, x):
        y = 0
        x = x
        size = 40
        particls = []
        for i in range(60):
            particls.append(Particle(self.sc, self.pygame, x, y, size))
            y += 2 + size
        return particls

    def reflection(self, player, player1):
        if self.y <= 0:
            self.angle = random.randint(20, 46) * math.pi / 180
            self.direction_y = "down"
        elif self.y >= HEIGHT - self.size:
            self.direction_y = "up"
            self.angle = random.randint(20, 46) * math.pi / 180

        if player1[0] + 5 >= self.x >= player1[0] and player1[1] <= self.y <= player1[2]:
            self.angle = random.randint(20, 46) * math.pi / 180
            self.direction_x = "left"
        elif player[0] - 5 <= self.x <= player[0] and player[1] <= self.y <= player[2]:
            self.direction_x = "right"
            self.angle = random.randint(20, 46) * math.pi / 180
        if self.x < 0:
            for el in self.particls_left:
                el.draw()

        if self.x > WIDHT - self.size:
            for el in self.particls_right:
                el.draw()

    def reset_ball(self):
        if self.x < 0 or self.x > WIDHT:
            self.x = WIDHT / 2 - self.size / 2
            self.y = random.randint(200, HEIGHT - 200)
            self.direction_y = random.choice(["up", "down"])

    def movent(self):
        if self.direction_x == "right":
            self.x += math.cos(self.angle) * self.speed
        elif self.direction_x == "left":
            self.x -= math.cos(self.angle) * self.speed
        if self.direction_y == "up":
            self.y -= math.sin(self.angle) * self.speed
        elif self.direction_y == "down":
            self.y += math.sin(self.angle) * self.speed

    def draw(self):
        self.movent()
        self.pygame.draw.rect(self.sc, "white", (self.x - self.size / 2, self.y, self.size, self.size))

    def rerurn_cord(self):
        return f"{WIDHT - round(self.x, 2)} {round(self.y, 2)}"

    def move(self, x, y):
        self.x = x
        self.y = y
