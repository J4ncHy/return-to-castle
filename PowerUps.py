import pygame


class Powerups(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = None
        self.import_sprite()

        self.rect = self.image.get_rect(topleft=pos)

    def import_sprite(self):
        path = "media/powerups/speedup.png"
        self.image = pygame.image.load(path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (64, 64))

    def update(self, x_shift):
        self.rect.x += x_shift
