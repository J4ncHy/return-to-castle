import pygame
from StateEnum import StateEnum
from settings import screen_w, screen_h
from HighscoreHandler import read_score

class Menu2:
    def __init__(self, surface):
        self.state = StateEnum.MAIN_MENU
        self.stack_state = [StateEnum.MAIN_MENU]

        self.pause_between_presses = False
        self.surface = surface

    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            if self.pause_between_presses:
                self.pause_between_presses = False
                if self.state == StateEnum.PLAYING:
                    self.state = StateEnum.PAUSE_MENU
                elif self.state == StateEnum.PAUSE_MENU:
                    self.state = StateEnum.PLAYING
        else:
            self.pause_between_presses = True
        if keys[pygame.K_s] and self.state == StateEnum.MAIN_MENU:
            self.state = StateEnum.PLAYING

    def state_router(self):
        match self.state:
            case StateEnum.PAUSE_MENU:
                self.pause()
            case StateEnum.MAIN_MENU:
                self.main_menu()

    def draw_time(self, time):
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("TIME: {:<.1f}".format(time), True, (255, 255, 255))
        textRect = text.get_rect()
        textRect.topleft = (20, 20)
        self.surface.blit(text, textRect)

    def draw_score(self, score):
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("SCORE: " + str(score), True, (255, 255, 255))
        textRect = text.get_rect()
        textRect.topleft = (20, 60)
        self.surface.blit(text, textRect)

    def draw_highscore(self):
        arr = read_score()
        max_score = []
        arr = sorted(arr, key=lambda x: (x["level"], -x["score"], x["time"]))
        last_lvl = 0
        for i in arr:
            if last_lvl != i["level"]:
                max_score.append((i["level"],i["score"], i["time"]))
                last_lvl = i["level"]

        font = pygame.font.Font('freesansbold.ttf', 16)

        text1 = "Highscore:"
        text = font.render(text1, True, (255, 255, 255))
        textRect = text.get_rect()
        textRect.topleft = (20, 60)
        self.surface.blit(text, textRect)
        for i in max_score:
            text1 = "Level {level:d}: {score:d} points in {time:.1f} seconds".format(level=i[0], score=i[1], time=i[2])
            text = font.render(text1, True, (255, 255, 255))
            textRect = text.get_rect()
            textRect.topleft = (20, 60 + (i[0] * 20))
            self.surface.blit(text, textRect)

    def pause(self):
        while self.state == StateEnum.PAUSE_MENU:
            self.get_input()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    break

            pygame.display.update()
            pygame.time.Clock().tick(60)
            self.draw_pause_screen()

    def draw_pause_screen(self):
        # TODO add image for pause screen

        font = pygame.font.Font('freesansbold.ttf', 64)
        text = font.render("GAME PAUSED", True, (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = (screen_w // 2, screen_h // 2)

        surf_temp = pygame.Surface((screen_w, screen_h), pygame.SRCALPHA)
        surf_temp.fill((0, 0, 0, 128))
        self.surface.blit(surf_temp, (0, 0))
        self.surface.blit(text, textRect)

        font = pygame.font.Font('freesansbold.ttf', 48)
        text = font.render("Press ESC to resume", True, (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = (screen_w // 2, screen_h // 2 + 70)
        self.surface.blit(text, textRect)

    def main_menu(self):
        while self.state == StateEnum.MAIN_MENU:
            self.get_input()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    break

            pygame.display.update()
            pygame.time.Clock().tick(60)
            self.draw_main_menu()

    def draw_main_menu(self):
        # TODO fix main menu to use buttons - placeholder function
        self.surface.fill((0, 0, 0))

        font = pygame.font.Font('freesansbold.ttf', 60)

        # Play button

        play_square = pygame.Rect(0, 0, 300, 75)
        play_square.center = (screen_w / 2, screen_h / 2 - 100)
        pygame.draw.rect(self.surface, (255, 0, 0), play_square, 2)

        text = font.render("play", True, (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = play_square.center
        self.surface.blit(text, textRect)

        # Settings button

        settings_button = pygame.Rect(0, 0, 300, 75)
        settings_button.center = (screen_w / 2, screen_h / 2)
        pygame.draw.rect(self.surface, (255, 0, 0), settings_button, 2)

        text = font.render("settings", True, (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = settings_button.center
        self.surface.blit(text, textRect)

        # Exit button

        exit_button = pygame.Rect(0, 0, 300, 75)
        exit_button.center = (screen_w / 2, 3 * (screen_h / 4))
        pygame.draw.rect(self.surface, (255, 0, 0), exit_button, 2)

        text = font.render("exit", True, (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = exit_button.center
        self.surface.blit(text, textRect)

        self.draw_highscore()

    def update(self):
        self.get_input()
        self.state_router()
