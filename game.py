import pygame
import sys

from settings import *
from Level import Level
from Menu import Menu
from HighscoreHandler import write_score

if __name__ == "__main__":
    pygame.init()

    screen = pygame.display.set_mode((screen_w, screen_h))
    clock = pygame.time.Clock()
    menu = Menu(screen)
    level = Level(screen, menu)


    while True:
        menu.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if level.check_game_end():
            time = (pygame.time.get_ticks() - level.start_time) / 1000
            write_score(level=level.level, score=level.score, time=round(time, 1))
            break

        level.draw()

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    sys.exit()
