import pygame
import sys

from settings import *
from Level import Level
from Player import Player

pygame.init()

screen = pygame.display.set_mode((screen_w, screen_h))
clock = pygame.time.Clock()
level = Level(level_map, screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if level.check_game_end():
        pygame.quit()
        sys.exit()

    screen.fill("black")

    level.draw()

    pygame.display.update()
    clock.tick(60)
