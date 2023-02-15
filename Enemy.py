import pygame
from settings import screen_h
from support import import_enemy_spritesheet


class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.animations = None
        self.import_enemy_assets()
        self.frame_index = 0
        self.animation_speed = 0.15
        self.image = self.animations["idle"][self.frame_index]
        self.rect = self.image.get_rect(topleft=pos)
        self.mask = pygame.mask.from_surface(self.image)

        self.starting_coords = [pos[0], pos[1]]

        self.dead = False

        # Movement

        self.direction = pygame.math.Vector2(0, 0)
        self.direction.x = -1
        self.speed = 1
        self.gravity = 0.8

    def import_enemy_assets(self):
        enemy_path = "media/boss.png"
        self.animations = import_enemy_spritesheet(enemy_path, 64, 64)

    def animate(self):
        animation = self.animations["idle"]

        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        self.image = animation[int(self.frame_index)]

    def attack(self):
        # TODO
        ...

    def update(self, x_shift):
        self.rect.x += x_shift
        self.starting_coords[0] += x_shift
        self.animate()
