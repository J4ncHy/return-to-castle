import pygame
from support import import_enemy_spritesheet
from settings import s


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

        self.status = "idle"
        self.facing_right = True

        # Movement

        self.direction = pygame.math.Vector2(0, 0)
        self.direction.x = -1
        self.speed = 1
        self.gravity = 0.8

    def import_enemy_assets(self):
        enemy_path = "media/boss.png"
        self.animations = import_enemy_spritesheet(enemy_path, 64, 64)

    def animate(self):
        animation = self.animations[self.status]

        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0
            if self.status == "dead":
                self.kill()

        image = animation[int(self.frame_index)]
        #w, h = image.get_size()
        #image = pygame.transform.scale(image, (w * s.scale_w, h * s.scale_h))
        #image.set_colorkey((0, 0, 0))
        if self.facing_right:
            self.image = image
        else:
            flipped_image = pygame.transform.flip(image, True, False)
            flipped_image.convert_alpha()
            flipped_image.set_colorkey((0, 0, 0))
            self.image = flipped_image
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.mask.get_rect(topleft=self.rect.topleft)

    def get_state(self):
        if self.status == "dead":
            self.speed = 0
            return
        if self.direction.x > 0:
            self.status = "run"
            self.facing_right = True
        elif self.direction.x < 0:
            self.status = "run"
            self.facing_right = False
        elif self.direction.x == 0:
            self.status = "idle"

    def attack(self):
        # TODO
        ...

    def update(self, x_shift):
        self.rect.x += x_shift
        self.starting_coords[0] += x_shift
        self.get_state()
        self.animate()
