import pygame
import sys

from settings import s
from Level import Level
from Menu_new import Menu
from StateEnum import StateEnum
from HighscoreHandler import write_score
import pygame_gui
import pygame_menu

def start_game():
    #menu.disable()
    #main_loop()
    #menu.mainloop(screen)
    ...

if __name__ == "__main__":

    pygame.init()
    display = pygame.display.set_mode((s.screen_w, s.screen_h), pygame.RESIZABLE)
    screen = pygame.surface.Surface((s.screen_w, s.screen_h))
    clock = pygame.time.Clock()
    menu1 = Menu(screen)
    level = Level(display, screen, menu1)

    while True:

        tmp = clock.tick(60) / 1000
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.VIDEORESIZE:
                display = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

                s.scale_w = event.w / s.original_w
                s.scale_h = event.h / s.original_h
                screen_w, screen_h = event.w, event.h
        #print(scale_w, scale_h)
            # menu.manager.process_events(event)
        if level.check_game_end():
            time = (pygame.time.get_ticks() - level.start_time) / 1000
            # write_score(player=level.player.name, level=level.level, score=level.score, time=round(time, 1))
            write_score(level=level.level, score=level.score, time=round(time, 1))
            pygame.quit()
            sys.exit()
        level.draw(tmp)
        pygame.display.update()

        #menu.update(events)
        #menu.draw(screen)

    #menu = pygame_menu.Menu('Return to Castle', screen_w, screen_h,
    #                        theme=pygame_menu.themes.THEME_DARK)
#
    #menu.add.text_input('Name :', default='Player')
    #menu.add.label("Tet")
#
    #menu.add.button('Play', main_loop())
    #menu.add.button('Quit', pygame_menu.events.EXIT)


    #menu.enable()
    #menu.mainloop(surface=screen)


