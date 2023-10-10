import pygame
from players import Player
from ball import *
import random


def draw_line():
    x = WIDHT / 2 - 27 // 2
    y = 0
    for i in range(18):
        pygame.draw.rect(sc, "white", (x, y, 27, 27))
        y += 27 + 27 // 2


pygame.init()
sc = pygame.display.set_mode((WIDHT, HEIGHT), pygame.FULLSCREEN)
pygame.mouse.set_visible(False)
exit = False
start = False
obj = None
clock = pygame.time.Clock()
status_connect = False
type_user = None
res = None
player = Player(sc, pygame, 0, 0)
player1 = Player(sc, pygame, 1250, 0)
ball = Ball(pygame, sc, WIDHT / 2, random.randint(200, HEIGHT - 200))
clock = pygame.time.Clock()
speed = 2

while exit is False:
    sc.fill("black")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        if event.type == pygame.KEYUP:
            start = True
            if event.key == pygame.K_ESCAPE:
                exit = True
            if event.key == 13:
                ball.reset_ball()
    keystate = pygame.key.get_pressed()
    if keystate[pygame.K_w]:
        player.movent(-speed)
    if keystate[pygame.K_s]:
        player.movent(speed)
    if keystate[pygame.K_UP]:
        player1.movent(-speed)
    if keystate[pygame.K_DOWN]:
        player1.movent(speed)

    if start:
        ball.draw()
    player.draw()
    player1.draw()
    ball.reflection(player.return_cord(), player1.return_cord())
    draw_line()
    pygame.display.flip()
    clock.tick(500)
pygame.quit()
