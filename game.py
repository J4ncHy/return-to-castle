import pygame
import sys

from settings import *
from Level import Level
from Menu_new import Menu
from HighscoreHandler import write_score
import pygame_gui

if __name__ == "__main__":
    pygame.init()

    screen = pygame.display.set_mode((screen_w, screen_h))
    clock = pygame.time.Clock()
    menu = Menu(screen)
    level = Level(screen, menu)

    while True:
        tmp = clock.tick(60) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            menu.manager.process_events(event)

        if level.check_game_end():
            time = (pygame.time.get_ticks() - level.start_time) / 1000
            #write_score(player=level.player.name, level=level.level, score=level.score, time=round(time, 1))
            write_score(level=level.level, score=level.score, time=round(time, 1))
            break

        level.draw(tmp)

        pygame.display.update()



    pygame.quit()
    sys.exit()
