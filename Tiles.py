import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size, tile_index):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.tile_index = int(tile_index)
        self.import_assets()
        self.rect = self.image.get_rect(topleft=pos)

    def import_assets(self):
        tile = "level/tiles/sprite_" + f"{self.tile_index:02}" + ".png"
        self.image = pygame.image.load(tile).convert_alpha()

    def update(self, x_shift):
        self.rect.x += x_shift
