import pygame
from StateEnum import StateEnum
from settings import s
from HighscoreHandler import read_score
from Button import Button
from support import get_font


class Main_Menu:
    def __init__(self, display, surface):
        self.state = StateEnum.MAIN_MENU
        self.stack_state = [StateEnum.MAIN_MENU]

        self.pause_between_presses = False
        self.display = display
        self.surface = surface

        self.buttons = {
            "menu": [
                Button(pos=(s.screen_w / 2, 450), image=None, font=get_font(40),
                       hover_color="#d7fcd4", base_color="White", text_input="PLAY"),
                Button(pos=(s.screen_w / 2, 500), image=None, font=get_font(40),
                       hover_color="#d7fcd4",
                       base_color="White", text_input="SCOREBOARD"),
                Button(pos=(s.screen_w / 2, 550), image=None, font=get_font(40),
                       hover_color="#d7fcd4",
                       base_color="White", text_input="QUIT")
            ],
            "scoreboard": [
                Button(pos=(s.screen_w / 2, 700), image=None, font=get_font(40),
                       hover_color="#d7fcd4",
                       base_color="White", text_input="BACK")
            ],
            "levels": [],
            "pause": [
                Button(pos=(s.screen_w / 2, 450), image=None, font=get_font(40),
                       hover_color="#d7fcd4",
                       base_color="White", text_input="RESUME"),
                Button(pos=(s.screen_w / 2, 500), image=None, font=get_font(40),
                       hover_color="#d7fcd4",
                       base_color="White", text_input="MAIN MENU")
            ],
            "dead": [
                Button(pos=(s.screen_w / 2, 500), image=None, font=get_font(40),
                       hover_color="#d7fcd4",
                       base_color="White", text_input="MAIN MENU")
            ]
        }

    def set_state(self, state):
        self.state = state

    def state_router(self, level):
        match self.state:
            case StateEnum.MAIN_MENU:
                self.main_menu(level)
            case StateEnum.SCOREBOARD:
                self.scoreboard()
            case StateEnum.PAUSE_MENU:
                self.pause_menu()
            case StateEnum.DEAD_MENU:
                self.dead_menu()

    def main_menu(self, level):
        while self.state == StateEnum.MAIN_MENU:

            self.surface.fill("black")
            MOUSE_POS = pygame.mouse.get_pos()
            text = get_font(72).render("RETURN TO CASTLE", True, (255, 255, 255))
            textRect = text.get_rect()
            textRect.center = (s.screen_w / 2, 300)
            self.surface.blit(text, textRect)

            for button in self.buttons["menu"]:
                button.change_color(MOUSE_POS)
                button.update(self.surface)

            self.display.blit(
                pygame.transform.scale(self.surface, (s.original_w * s.scale_w, s.original_h * s.scale_h)), (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.VIDEORESIZE:
                    self.display = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                    s.scale_w = event.w / s.original_w
                    s.scale_h = event.h / s.original_h
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for button in self.buttons["menu"]:
                        if button.check_for_input(MOUSE_POS):
                            if button.text_input == "PLAY":
                                level.level_handler(0)
                                self.set_state(StateEnum.PLAYING)
                            elif button.text_input == "SCOREBOARD":
                                self.set_state(StateEnum.SCOREBOARD)
                            elif button.text_input == "QUIT":
                                pygame.quit()

            pygame.display.update()
            pygame.time.Clock().tick(60)

    def scoreboard(self):
        while self.state == StateEnum.SCOREBOARD:

            self.surface.fill("black")

            MOUSE_POS = pygame.mouse.get_pos()
            text = get_font(50).render("SCOREBOARD", True, (255, 255, 255))
            textRect = text.get_rect()
            textRect.center = (s.screen_w / 2, 200)
            self.surface.blit(text, textRect)

            for button in self.buttons["scoreboard"]:
                button.change_color(MOUSE_POS)
                button.update(self.surface)

            self.display.blit(
                pygame.transform.scale(self.surface, (s.original_w * s.scale_w, s.original_h * s.scale_h)), (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.VIDEORESIZE:
                    self.display = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                    s.scale_w = event.w / s.original_w
                    s.scale_h = event.h / s.original_h
                if event.type == pygame.MOUSEBUTTONUP:
                    for button in self.buttons["scoreboard"]:
                        if button.check_for_input(MOUSE_POS):
                            if button.text_input == "BACK":
                                self.set_state(StateEnum.MAIN_MENU)

            pygame.display.update()
            pygame.time.Clock().tick(60)

    def pause_menu(self):
        while self.state == StateEnum.PAUSE_MENU:

            #self.surface.fill("black")

            MOUSE_POS = pygame.mouse.get_pos()
            text = get_font(50).render("PAUSE", True, (255, 255, 255))
            textRect = text.get_rect()

            textRect.center = (s.screen_w / 2, 200)
            self.surface.blit(text, textRect)

            text = get_font(40).render("You are currently paused.", True, (255, 255, 255))
            textRect = text.get_rect()

            textRect.center = (s.screen_w / 2, 300)
            self.surface.blit(text, textRect)

            for button in self.buttons["pause"]:
                button.change_color(MOUSE_POS)
                button.update(self.surface)

            self.display.blit(
                pygame.transform.scale(self.surface, (s.original_w * s.scale_w, s.original_h * s.scale_h)), (0, 0))

            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.VIDEORESIZE:
                    self.display = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                    s.scale_w = event.w / s.original_w
                    s.scale_h = event.h / s.original_h
                #if keys[pygame.K_ESCAPE]:
                #    self.set_state(StateEnum.PLAYING)
                if event.type == pygame.MOUSEBUTTONUP:
                    for button in self.buttons["pause"]:
                        if button.check_for_input(MOUSE_POS):
                            if button.text_input == "RESUME":
                                self.set_state(StateEnum.PLAYING)
                            if button.text_input == "MAIN MENU":
                                self.set_state(StateEnum.MAIN_MENU)

            pygame.display.update()
            pygame.time.Clock().tick(60)

    def dead_menu(self):
        while self.state == StateEnum.DEAD_MENU:

            self.surface.fill("black")

            MOUSE_POS = pygame.mouse.get_pos()
            text = get_font(50).render("YOU DIED", True, (255, 255, 255))
            textRect = text.get_rect()
            textRect.center = (s.screen_w / 2, 200)
            self.surface.blit(text, textRect)

            for button in self.buttons["dead"]:
                button.change_color(MOUSE_POS)
                button.update(self.surface)

            self.display.blit(
                pygame.transform.scale(self.surface, (s.original_w * s.scale_w, s.original_h * s.scale_h)), (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.VIDEORESIZE:
                    self.display = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                    s.scale_w = event.w / s.original_w
                    s.scale_h = event.h / s.original_h
                if event.type == pygame.MOUSEBUTTONUP:
                    for button in self.buttons["dead"]:
                        if button.check_for_input(MOUSE_POS):
                            if button.text_input == "MAIN MENU":
                                self.set_state(StateEnum.MAIN_MENU)

            pygame.display.update()
            pygame.time.Clock().tick(60)

    def draw_time(self, time):
        text = get_font(32).render("TIME: {:<.1f}".format(time), True, (255, 255, 255))
        textRect = text.get_rect()
        textRect.topleft = (20, 20)
        self.surface.blit(text, textRect)

    def draw_score(self, score):
        text = get_font(32).render("SCORE: " + str(score), True, (255, 255, 255))
        textRect = text.get_rect()
        textRect.topleft = (20, 60)
        self.surface.blit(text, textRect)

    def update(self, level):
        self.state_router(level)
