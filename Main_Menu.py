import pygame
from StateEnum import StateEnum
from settings import s
from HighscoreHandler import read_score
from Button import Button
from support import get_font
import pygame_gui

class Main_Menu:
    def __init__(self, display, surface, manager):
        self.state = StateEnum.MAIN_MENU
        self.stack_state = [StateEnum.MAIN_MENU]

        self.pause_between_presses = False
        self.display = display
        self.surface = surface

        self.manager = manager

        self.mouse_pressed = True

        self.text_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(0, 0, 100, 100), manager=self.manager)
        self.name = ""

        self.buttons = {
            "menu": [
                Button(pos=(s.screen_w / 2, 450), image=None, font=get_font(40),
                       hover_color="#3d4b4d", base_color="#181c1c", text_input="PLAY"),
                Button(pos=(s.screen_w / 2, 500), image=None, font=get_font(40),
                       hover_color="#3d4b4d",
                       base_color="#181c1c", text_input="LEVEL SELECT"),
                Button(pos=(s.screen_w / 2, 550), image=None, font=get_font(40),
                       hover_color="#3d4b4d",
                       base_color="#181c1c", text_input="QUIT")
            ],
            "scoreboard": [
                Button(pos=((s.screen_w / 6)*1, 350), image=pygame.image.load("media/level_bg.png"), font=get_font(70),
                       hover_color="#AAAAAA",
                       base_color="white", text_input="1"),
                Button(pos=((s.screen_w / 6)*2, 350), image=pygame.image.load("media/level_bg.png"), font=get_font(70),
                       hover_color="#AAAAAA",
                       base_color="white", text_input="2"),
                Button(pos=((s.screen_w / 6)*3, 350), image=pygame.image.load("media/level_bg.png"), font=get_font(70),
                       hover_color="#AAAAAA",
                       base_color="white", text_input="3"),
                Button(pos=((s.screen_w / 6)*4, 350), image=pygame.image.load("media/level_bg.png"), font=get_font(70),
                       hover_color="#AAAAAA",
                       base_color="white", text_input="4"),
                Button(pos=((s.screen_w / 6)*5, 350), image=pygame.image.load("media/level_bg.png"), font=get_font(70),
                       hover_color="#AAAAAA",
                       base_color="white", text_input="5"),
                Button(pos=((s.screen_w / 6) * 1, 500), image=pygame.image.load("media/level_bg.png"),
                       font=get_font(70),
                       hover_color="#AAAAAA",
                       base_color="white", text_input="6"),
                Button(pos=((s.screen_w / 6) * 2, 500), image=pygame.image.load("media/level_bg.png"),
                       font=get_font(70),
                       hover_color="#AAAAAA",
                       base_color="white", text_input="7"),
                Button(pos=((s.screen_w / 6) * 3, 500), image=pygame.image.load("media/level_bg.png"),
                       font=get_font(70),
                       hover_color="#AAAAAA",
                       base_color="white", text_input="8"),
                Button(pos=((s.screen_w / 6) * 4, 500), image=pygame.image.load("media/level_bg.png"),
                       font=get_font(70),
                       hover_color="#AAAAAA",
                       base_color="white", text_input="9"),
                Button(pos=((s.screen_w / 6) * 5, 500), image=pygame.image.load("media/level_bg.png"),
                       font=get_font(70),
                       hover_color="#AAAAAA",
                       base_color="white", text_input="10"),

                Button(pos=(s.screen_w / 2, 700), image=None, font=get_font(40),
                       hover_color="#3d4b4d",
                       base_color="#181c1c", text_input="BACK")
            ],
            "pause": [
                Button(pos=(s.screen_w / 2, 450), image=None, font=get_font(40),
                       hover_color="#3d4b4d",
                       base_color="#181c1c", text_input="RESUME"),
                Button(pos=(s.screen_w / 2, 500), image=None, font=get_font(40),
                       hover_color="#3d4b4d",
                       base_color="#181c1c", text_input="MAIN MENU")
            ],
            "dead": [
                Button(pos=(s.screen_w / 2, 500), image=None, font=get_font(40),
                       hover_color="#3d4b4d",
                       base_color="#181c1c", text_input="MAIN MENU")
            ],
            "win": [
                Button(pos=(s.screen_w / 2, 500), image=None, font=get_font(40),
                       hover_color="#3d4b4d",
                       base_color="#181c1c", text_input="MAIN MENU")
            ]
        }

    def set_state(self, state):
        self.state = state

    def state_router(self, level):
        match self.state:
            case StateEnum.MAIN_MENU:
                self.main_menu(level)
            case StateEnum.SCOREBOARD:
                self.scoreboard(level)
            case StateEnum.PAUSE_MENU:
                self.pause_menu()
            case StateEnum.DEAD_MENU:
                self.dead_menu()
            case StateEnum.WIN:
                self.win_menu()

    def main_menu(self, level):
        while self.state == StateEnum.MAIN_MENU:

            clock = pygame.time.Clock()

            self.surface.fill((135, 206, 235))
            bg_img = "./level/background/BG0.png"
            background_image = pygame.image.load(bg_img).convert_alpha()
            self.surface.blit(background_image, (0, 0))

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
                self.manager.process_events(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.VIDEORESIZE:
                    self.display = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                    s.scale_w = event.w / s.original_w
                    s.scale_h = event.h / s.original_h
                if event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
                        if event.ui_element == self.text_input:
                            self.name = event.text
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouse_pressed = True
                    level.level_handler(1)
                    for button in self.buttons["menu"]:
                        if button.check_for_input(MOUSE_POS):
                            if button.text_input == "PLAY":
                                self.set_state(StateEnum.PLAYING)
                                level.level_handler(0)
                            elif button.text_input == "LEVEL SELECT":
                                self.set_state(StateEnum.SCOREBOARD)
                            elif button.text_input == "QUIT":
                                pygame.quit()
                if event.type == pygame.MOUSEBUTTONUP:
                    self.mouse_pressed = False

            time_delta = clock.tick(60) / 1000.0
            self.manager.update(time_delta)

            self.manager.draw_ui(self.surface)

            pygame.display.update()

    def scoreboard(self, level):
        while self.state == StateEnum.SCOREBOARD:

            self.surface.fill((135, 206, 235))
            bg_img = "./level/background/BG0.png"
            background_image = pygame.image.load(bg_img).convert_alpha()
            self.surface.blit(background_image, (0, 0))

            MOUSE_POS = pygame.mouse.get_pos()
            text = get_font(50).render("LEVEL SELECT", True, (255, 255, 255))
            textRect = text.get_rect()
            textRect.center = (s.screen_w / 2, 150)
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
                    self.mouse_pressed = False
                if event.type == pygame.MOUSEBUTTONDOWN and self.mouse_pressed == False:
                    self.mouse_pressed = True
                    for button in self.buttons["scoreboard"]:
                        if button.check_for_input(MOUSE_POS):
                            match button.text_input:
                                case "1":
                                    self.set_state(StateEnum.PLAYING)
                                    level.level_handler(0)
                                case "2":
                                    self.set_state(StateEnum.PLAYING)
                                    level.level_handler(1)
                                case "3":
                                    self.set_state(StateEnum.PLAYING)
                                    level.level_handler(2)
                                case "4":
                                    self.set_state(StateEnum.PLAYING)
                                    level.level_handler(3)
                                case "5":
                                    self.set_state(StateEnum.PLAYING)
                                    level.level_handler(4)
                                case "6":
                                    self.set_state(StateEnum.PLAYING)
                                    level.level_handler(5)
                                case "7":
                                    self.set_state(StateEnum.PLAYING)
                                    level.level_handler(6)
                                case "8":
                                    self.set_state(StateEnum.PLAYING)
                                    level.level_handler(7)
                                case "9":
                                    self.set_state(StateEnum.PLAYING)
                                    level.level_handler(8)
                                case "10":
                                    self.set_state(StateEnum.PLAYING)
                                    level.level_handler(9)
                                case "BACK":
                                    self.set_state(StateEnum.MAIN_MENU)


            pygame.display.update()
            pygame.time.Clock().tick(60)

    def pause_menu(self):
        while self.state == StateEnum.PAUSE_MENU:

            self.surface.fill((135, 206, 235))
            bg_img = "./level/background/BG0.png"
            background_image = pygame.image.load(bg_img).convert_alpha()
            self.surface.blit(background_image, (0, 0))

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
                    self.mouse_pressed = False
                if event.type == pygame.MOUSEBUTTONDOWN and self.mouse_pressed == False:
                    self.mouse_pressed = True
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

            self.surface.fill((135, 206, 235))
            bg_img = "./level/background/BG0.png"
            background_image = pygame.image.load(bg_img).convert_alpha()
            self.surface.blit(background_image, (0, 0))

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
                    self.mouse_pressed = False
                if event.type == pygame.MOUSEBUTTONDOWN and self.mouse_pressed == False:
                    self.mouse_pressed = True
                    for button in self.buttons["dead"]:
                        if button.check_for_input(MOUSE_POS):
                            if button.text_input == "MAIN MENU":
                                self.set_state(StateEnum.MAIN_MENU)

            pygame.display.update()
            pygame.time.Clock().tick(60)

    def win_menu(self):
        while self.state == StateEnum.WIN:

            self.surface.fill((135, 206, 235))
            bg_img = "./level/background/BG0.png"
            background_image = pygame.image.load(bg_img).convert_alpha()
            self.surface.blit(background_image, (0, 0))

            MOUSE_POS = pygame.mouse.get_pos()
            text = get_font(50).render("YOU SAVED YOUR PRINCESS", True, (255, 255, 255))
            textRect = text.get_rect()
            textRect.center = (s.screen_w / 2, 200)
            self.surface.blit(text, textRect)

            for button in self.buttons["win"]:
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
                    self.mouse_pressed = False
                if event.type == pygame.MOUSEBUTTONDOWN and self.mouse_pressed == False:
                    self.mouse_pressed = True
                    for button in self.buttons["win"]:
                        if button.check_for_input(MOUSE_POS):
                            if button.text_input == "MAIN MENU":
                                self.set_state(StateEnum.MAIN_MENU)

            pygame.display.update()
            pygame.time.Clock().tick(60)

    def draw_time(self, time):

        bg_img = "./media/button_bg.png"
        background_image = pygame.image.load(bg_img).convert_alpha()
        self.surface.blit(background_image, (15, 19))

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
