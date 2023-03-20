import pygame
from settings import s

class Cloud(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = None
        self.import_assets()

        self.rect = self.image.get_rect(topleft=pos)

    def import_assets(self):
        cloud_image = "media/cloud.png"
        self.image = pygame.image.load(cloud_image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (96, 96))

    def update(self, x_shift):
        self.rect.x += x_shift
