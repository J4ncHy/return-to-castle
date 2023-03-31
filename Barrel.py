import pygame


class Barrel(pygame.sprite.Sprite):
    def __init__(self, pos, direction):
        super().__init__()
        self.image = None
        self.import_sprite()

        self.rect = self.image.get_rect(topleft=pos)
        self.mask = pygame.mask.from_surface(self.image)

        self.direction = pygame.math.Vector2(0, 0)
        self.direction.x = direction
        self.speed = 5
        self.starting_pos = pos
        self.angle = 0

    def import_sprite(self):
        path = "media/barrel.png"
        self.image = pygame.image.load(path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (64, 64))

    def move(self, srf):
        self.rect.x += self.direction.x * self.speed
        print(self.rect.x, self.starting_pos[0])
        if abs(self.starting_pos[0] - self.rect.x) > 500:
            self.kill()

        self.angle += 4

        rotated_image = pygame.transform.rotate(self.image, self.angle)
        new_rect = rotated_image.get_rect(center=self.image.get_rect(topleft=(self.rect.x, self.rect.y)).center)

        srf.blit(rotated_image, new_rect)

    def update(self, x_shift, srf):
        self.rect.x += x_shift
        self.move(srf)
