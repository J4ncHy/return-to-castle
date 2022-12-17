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
        self.image = self.animations["idle"][0]  # pygame.Surface((32, 64))
        # self.image.fill("green")
        self.rect = self.image.get_rect(topleft=pos)

        self.dead = False

        # Movement

        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 8
        self.default_speed = 8
        self.gravity = 0.8
        self.jump_speed = -16

    def import_enemy_assets(self):
        character_path = "media/thief.png"
        self.animations = import_enemy_spritesheet(character_path, 64, 64)
        print(self.animations)

    def animate(self):
        animation = self.animations["idle"]

        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        self.image = animation[int(self.frame_index)]

    def check_death(self):
        return self.rect.centerx > screen_h

    def move(self):
        # TODO
        ...

    def attack(self):
        # TODO
        ...

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def update(self, x_shift):
        self.rect.x += x_shift
        self.check_death()
        self.animate()
