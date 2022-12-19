import pygame

class Powerups(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        #powerups = import_folder("media/powerups/")
        self.image = pygame.image.load("media/powerups/speedup.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift
