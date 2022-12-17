import pygame
from support import import_folder
from settings import screen_h


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.dead = False
        self.animations = None
        self.image = pygame.Surface((32, 64))  # self.animations["idle"][self.frame_index]
        self.image.fill("red")
        self.rect = self.image.get_rect(topleft=pos)
        self.frame_index = 0
        self.animation_speed = 0.15

        # Player movement

        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 8
        self.default_speed = 8
        self.gravity = 0.8
        self.jump_speed = -16
        self.jump_count = 0

    def import_character_assets(self):
        # character_path = "media/character/character.png"
        character_path = "media/thief.png"
        self.animations = {"idle": [], "run": [], "jump": [], "fall": []}
        # for animation in self.animations.keys():
        #     full_path = character_path + animation
        #     self.animations[animation] = import_folder(full_path)

        # TODO import character sprite sheet and feed it into self.animations

    def animate(self):
        animation = self.animations["run"]

        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        self.image = animation[int(self.frame_index)]

    def get_input(self):
        keys = pygame.key.get_pressed()

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

    def update_speed(self, multiplier):
        self.default_speed *= multiplier

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def update(self):
        self.get_input()
        self.check_death()
        # self.animate()
