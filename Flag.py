import pygame
from support import import_spritesheet


class Flag(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = None
        self.animations = None
        self.import_assets()

        self.frame_index = 0
        self.animation_speed = 0.15
        self.image = self.animations[self.frame_index]
        self.rect = self.image.get_rect(topleft=pos)
        self.mask = pygame.mask.from_surface(self.image)

    def import_assets(self):
        flag_image = "media/flag.png"
        self.animations = import_spritesheet(flag_image, 64, 64)

    def animate(self):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.animations):
            self.frame_index = 0

        self.image = self.animations[int(self.frame_index)]

    def update(self, x_shift):
        self.rect.x += x_shift
        self.animate()
