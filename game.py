import pygame
import sys

from settings import *
from Level import Level
from Menu import Menu

if __name__ == "__main__":
    pygame.init()

    screen = pygame.display.set_mode((screen_w, screen_h))
    clock = pygame.time.Clock()
    level = Level(screen)
    menu = Menu(screen)

    while True:
        menu.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if level.check_game_end():
            break

        level.draw()
        menu.draw_score(level.score)

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    sys.exit()
