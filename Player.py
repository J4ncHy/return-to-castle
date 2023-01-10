import pygame
from support import import_enemy_spritesheet
from settings import screen_h


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, sound):
        super().__init__()
        self.dead = False
        self.animations = None
        self.import_character_assets()
        self.frame_index = 0
        self.animation_speed = 0.15
        self.image = self.animations["idle"][self.frame_index]
        self.rect = self.image.get_rect(topleft=pos)

        self.lives = 3

        # Player movement

        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 8
        self.default_speed = 8
        self.gravity = 0.8
        self.jump_speed = -16
        self.jump_count = 0

        self.sound = sound

    def import_character_assets(self):
        # character_path = "media/character/character.png"
        # self.animations = import_player_spritesheet(character_path, 64, 64)
        enemy_path = "media/thief.png"
        self.animations = import_enemy_spritesheet(enemy_path, 64, 64)

    def animate(self):
        animation = self.animations["idle"]

        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        self.image = animation[int(self.frame_index)]

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]:
            ...

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0

        if keys[pygame.K_UP] and self.jump_count == 0:
            self.jump()

    def check_death(self):
        return self.rect.centerx > screen_h

    def jump(self):
        self.direction.y = self.jump_speed
        self.jump_count += 1
        self.sound.play_jump()

    def update_speed(self, multiplier):
        self.default_speed *= multiplier

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def update(self):
        self.get_input()
        self.check_death()
        self.animate()
