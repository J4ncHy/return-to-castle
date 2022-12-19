import pygame

from support import import_bullet_spritesheet


class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.animations = None
        self.import_bullet_assets()
        self.frame_index = 0
        self.animation_speed = 0.15
        self.image = self.animations["idle"][self.frame_index]
        self.rect = self.image.get_rect(topleft=pos)

        self.destroyed = False

        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 1

    def import_bullet_assets(self):
        bullet_path = "media/bullet.png"
        self.animations = import_bullet_spritesheet(bullet_path, 64, 64)

    def animate(self):
        animation = self.animations["idle"]

        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        self.image = animation[int(self.frame_index)]

    def x_shift(self, x_shift):
        self.rect.x += x_shift

    def update(self, x_shift):
        self.x_shift(x_shift)
        self.animate()
