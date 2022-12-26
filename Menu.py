import pygame
from StateEnum import StateEnum
from settings import screen_w, screen_h


class Menu:
    def __init__(self, surface):
        self.state = StateEnum.PLAYING
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

    def state_router(self):
        if self.state == StateEnum.PAUSE_MENU:
            self.pause()

    def draw_score(self, score):
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("SCORE: " + str(score), True, (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = (screen_w // 13, screen_h // 20)
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

    def update(self):

        self.state_router()
        self.get_input()
