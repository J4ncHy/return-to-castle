import pygame
import sys

from settings import s
from Level import Level
from Menu_new import Menu
from Main_Menu import Main_Menu
from StateEnum import StateEnum
from HighscoreHandler import write_score
import pygame_gui

if __name__ == "__main__":

    pygame.init()
    display = pygame.display.set_mode((s.screen_w, s.screen_h), pygame.RESIZABLE)
    screen = pygame.surface.Surface((s.screen_w, s.screen_h))
    clock = pygame.time.Clock()
    menu1 = Menu(screen)
    manager = pygame_gui.UIManager((s.screen_w, s.screen_h))
    main_menu = Main_Menu(display, screen, manager)
    level = Level(display, screen, menu1, main_menu)


    while True:

        tmp = clock.tick(60) / 1000

        main_menu.state_router(level)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                main_menu.mouse_pressed = False
            if event.type == pygame.VIDEORESIZE:
                display = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                s.scale_w = event.w / s.original_w
                s.scale_h = event.h / s.original_h
        if level.check_game_end():
            time = (pygame.time.get_ticks() - level.start_time) / 1000
            # write_score(player=level.player.name, level=level.level, score=level.score, time=round(time, 1))
            write_score(level=level.level, score=level.score, time=round(time, 1))
            level.level_handler(1)
            main_menu.set_state(StateEnum.DEAD_MENU)
        if main_menu.state == StateEnum.PLAYING:
            level.draw(tmp)
        pygame.display.update()


