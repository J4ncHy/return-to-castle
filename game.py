import pygame
import sys

from settings import *
from Level import Level
from Menu_new import Menu
from StateEnum import StateEnum
from HighscoreHandler import write_score
import pygame_gui
import pygame_menu

def main_loop():
    #menu.mainloop(surface=screen, fps_limit=60)
    while True:

        tmp = clock.tick(60) / 1000
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # menu.manager.process_events(event)
        if level.check_game_end():
            time = (pygame.time.get_ticks() - level.start_time) / 1000
            # write_score(player=level.player.name, level=level.level, score=level.score, time=round(time, 1))
            write_score(level=level.level, score=level.score, time=round(time, 1))
            pygame.quit()
            sys.exit()
        level.draw(tmp)
        pygame.display.update()

        menu.update(events)
        menu.draw(screen)


def start_game():
    #menu.disable()
    #main_loop()
    #menu.mainloop(screen)
    ...

if __name__ == "__main__":

    pygame.init()
    screen = pygame.display.set_mode((screen_w, screen_h))
    clock = pygame.time.Clock()
    menu1 = Menu(screen)
    level = Level(screen, menu1)

    menu = pygame_menu.Menu('Return to Castle', screen_w, screen_h,
                            theme=pygame_menu.themes.THEME_DARK)

    menu.add.text_input('Name :', default='Player')
    menu.add.label("Tet")

    menu.add.button('Play', main_loop())
    menu.add.button('Quit', pygame_menu.events.EXIT)


    menu.enable()
    #menu.mainloop(surface=screen)


