import pygame
from Tiles import Tile
from settings import tile_size, screen_w, screen_h
from Player import Player
from PowerUps import Powerups


class Level:
    def __init__(self, level_data, surface):
        self.powerups = None
        self.tiles = None
        self.player = None

        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = 0

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.powerups = pygame.sprite.GroupSingle()

        for i, row in enumerate(layout):
            for j, col in enumerate(row):
                y = i * tile_size
                x = j * tile_size

                if col == "X":
                    tile = Tile((x, y), tile_size)
                    self.tiles.add(tile)
                if col == "P":
                    playerSprite = Player((x, y))
                    self.player.add(playerSprite)
                if col == "S":
                    powerup = Powerups((x, y), tile_size)
                    self.powerups.add(powerup)

    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x
        speed = player.default_speed

        if player_x < 0.2 * screen_w and direction_x < 0:
            self.world_shift = speed
            player.speed = 0
        elif player_x > 0.8 * screen_w and direction_x > 0:
            self.world_shift = -speed
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = speed

    def horizonal_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for sprite in self.tiles:
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left

    def vertical_movement_collison(self):
        player = self.player.sprite
        player.apply_gravity()

        for sprite in self.tiles:
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.jump_count = 0
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0

    def powerups_collision(self):
        player = self.player.sprite
        for sprite in self.powerups:
            if sprite.rect.colliderect(player.rect):
                player.update_speed(2)
                sprite.kill()

    def check_game_end(self):
        player = self.player.sprite
        return player.rect.top > screen_h

    def draw(self):

        # Level tiles
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.scroll_x()

        # Level player
        self.player.update()
        self.horizonal_movement_collision()
        self.vertical_movement_collison()
        self.player.draw(self.display_surface)

        # Level powerups
        self.powerups.draw(self.display_surface)
        self.powerups_collision()
        self.powerups.update(self.world_shift)
