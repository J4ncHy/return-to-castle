import pygame
from support import import_boss_spritesheet
from Barrel import Barrel

class Boss(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.heart = None
        self.animations = None
        self.import_boss_assets()
        self.frame_index = 0
        self.animation_speed = 0.12
        self.image = self.animations["idle"][self.frame_index]
        self.rect = self.image.get_rect(topleft=pos)
        self.mask = pygame.mask.from_surface(self.image)

        self.starting_coords = [pos[0], pos[1]]

        self.dead = False

        self.status = "idle"
        self.facing_right = True

        self.lives = 10

        self.prev_barrel_spawn = 0
        self.last_attack = 0
        self.last_hit = 0

        # Movement

        self.direction = pygame.math.Vector2(0, 0)
        self.direction.x = -1
        self.speed = 1

    def import_boss_assets(self):
        boss_path = "media/knight.png"
        self.animations = import_boss_spritesheet(boss_path, 77, 64)

    def animate(self):
        animation = self.animations[self.status]
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0
            if self.status == "dead":
                self.kill()

        image = animation[int(self.frame_index)]
        if self.facing_right:
            self.image = image
        else:
            flipped_image = pygame.transform.flip(image, True, False)
            flipped_image.convert_alpha()
            flipped_image.set_colorkey((0, 0, 255))
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

    def get_direction(self, player):
        if player.rect.x - self.rect.x < 0:
            self.facing_right = False
            self.direction.x = -1
            return
        self.facing_right = True
        self.direction.x = 1

    def set_last_hit(self, time):
        self.last_hit = time

    def set_prev_barrel_time(self, time):
        self.prev_barrel_spawn = time

    def set_last_attack(self, time):
        self.last_attack = time

    def player_barrel_detection(self, player):
        return 250 < abs(player.rect.x - self.rect.x) < 500

    def player_detection(self, player):
        return abs(player.rect.x - self.rect.x) < 250

    def player_in_proximity(self, player):
        return abs(player.rect.x - self.rect.x) < 100

    def update(self, x_shift, player):
        self.rect.x += x_shift
        # self.starting_coords[0] += x_shift
        # self.get_state()
        self.get_direction(player)
        self.animate()
