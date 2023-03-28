import pygame


class Hearts(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = None
        self.import_sprite()

        self.rect = self.image.get_rect(topleft=pos)
        self.mask = pygame.mask.from_surface(self.image)

    def import_sprite(self):
        path = "media/heart.png"
        self.image = pygame.image.load(path).convert_alpha()
        # self.image = pygame.transform.scale(self.image, (64, 64))

    def update(self):
        ...