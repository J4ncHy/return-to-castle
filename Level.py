import pygame

from Enemy import Enemy
from Tiles import Tile
from settings import tile_size, screen_w, screen_h
from Player import Player
from PowerUps import Powerups
from Coin import Coin
from Bullet import Bullet


class Level:
    def __init__(self, level_data, surface):
        self.powerups = None
        self.tiles = None
        self.player = None
        self.enemies = None
        self.bullets = None
        self.coins = None
        self.background_image = None

        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = 0

        self.score = 0

    def import_assets(self):
        background_img = "media/background_cloud.png"
        self.background_image = pygame.image.load(background_img).convert_alpha()

    def setup_level(self, layout):
        self.import_assets()

        self.tiles = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.powerups = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()

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
                    powerup = Powerups((x, y))
                    self.powerups.add(powerup)
                if col == "E":
                    enemy = Enemy((x, y))
                    self.enemies.add(enemy)
                if col == "C":
                    coin = Coin((x, y))
                    self.coins.add(coin)

    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x
        speed = player.default_speed

        if player_x < 0.4 * screen_w and direction_x < 0:
            self.world_shift = speed
            player.speed = 0
        elif player_x > 0.6 * screen_w and direction_x > 0:
            self.world_shift = -speed
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = speed

    def horizontal_world_player_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for sprite in self.tiles:
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left

    def vertical_world_player_movement_collision(self):
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

    def horizontal_world_enemies_movement_collision(self):
        for enemy in self.enemies:
            enemy.rect.x += enemy.direction.x * enemy.speed
            for sprite in self.tiles:
                if sprite.rect.colliderect(enemy.rect):
                    if enemy.direction.x < 0:
                        enemy.rect.left = sprite.rect.right
                    elif enemy.direction.x > 0:
                        enemy.rect.right = sprite.rect.left
                    enemy.direction.x *= -1

    def player_enemy_collision(self):
        player = self.player.sprite
        for sprite in self.enemies:
            if sprite.rect.colliderect(player.rect):
                self.player.sprite.dead = True

    def player_powerups_collision(self):
        player = self.player.sprite
        for sprite in self.powerups:
            if sprite.rect.colliderect(player.rect):
                player.update_speed(1.25)
                sprite.kill()

    def player_coin_collisions(self):
        player = self.player.sprite
        for sprite in self.coins:
            if sprite.rect.colliderect(player.rect):
                self.score += 10
                sprite.kill()

    def check_game_end(self):
        player = self.player.sprite
        return player.rect.top > screen_h or self.player.sprite.dead

    def draw(self):

        # Background
        self.display_surface.blit(self.background_image, (0, 0))

        # Level tiles
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.scroll_x()

        # Level player
        self.player.update()
        self.horizontal_world_player_movement_collision()
        self.vertical_world_player_movement_collision()
        self.player.draw(self.display_surface)

        # Level powerups
        self.powerups.draw(self.display_surface)
        self.player_powerups_collision()
        self.powerups.update(self.world_shift)

        # Level enemies
        self.enemies.update(self.world_shift)
        self.enemies.draw(self.display_surface)
        self.player_enemy_collision()
        self.horizontal_world_enemies_movement_collision()

        # Level coins

        self.coins.update(self.world_shift)
        self.player_coin_collisions()
        self.coins.draw(self.display_surface)
