import pygame
import csv

from Enemy import Enemy
from Tiles import Tile
from settings import tile_size, screen_w, screen_h
from Player import Player
from PowerUps import Powerups
from Coin import Coin
from Cloud import Cloud
from Bullet import Bullet
from Flag import Flag
from SoundHandler import SoundHandler


class Level:
    def __init__(self, surface):
        self.level = 0
        self.cnt = 0
        self.ambience = [(135, 206, 235), (178, 227, 247), (255, 248, 219), (244, 128, 55), (0, 0, 0)]

        self.enemies_guns = None
        self.flag = None
        self.clouds = None
        self.powerups = None
        self.tiles = None
        self.player = None
        self.enemies_weak = None
        #self.bullets = None
        self.coins = None
        self.background_image = None

        self.sound = SoundHandler()

        self.display_surface = surface
        self.setup_level(self.import_level_from_tilemap())
        self.world_shift = 0

        self.score = 0

    def import_assets(self):
        # Function imports all required assets, and specifically the tile set is saved into an array for easier use
        background_img = "level/background/BG{}.png".format(self.level)  # "media/background_cloud.png"
        self.background_image = pygame.image.load(background_img).convert_alpha()

    def level_handler(self):
        self.score += 100
        self.level += 1
        del self.enemies_guns
        del self.flag
        del self.clouds
        del self.powerups
        del self.tiles
        del self.player
        del self.enemies_weak
        #del self.bullets
        del self.coins
        del self.background_image

        self.world_shift = 0
        self.setup_level(self.import_level_from_tilemap())

    def import_level_from_tilemap(self):
        level_arr = []
        with open("level/level{}.csv".format(self.level), newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in spamreader:
                # print(', '.join(row))
                level_arr.append(row)
            tmp = []
        return level_arr

    def setup_level(self, layout):
        self.import_assets()

        self.tiles = pygame.sprite.Group()
        self.enemies_weak = pygame.sprite.Group()
        self.enemies_guns = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.powerups = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()
        self.clouds = pygame.sprite.Group()
        self.flag = pygame.sprite.GroupSingle()

        for i, row in enumerate(layout):
            for j, col in enumerate(row):
                y = i * tile_size
                x = j * tile_size

                if col == "49":
                    playerSprite = Player((x, y))
                    self.player.add(playerSprite)
                elif col == "45":
                    powerup = Powerups((x, y))
                    self.powerups.add(powerup)
                elif col == "42":
                    enemy = Enemy((x, y))
                    self.enemies_weak.add(enemy)
                elif col == "50":
                    coin = Coin((x, y))
                    self.coins.add(coin)
                elif col == "48":
                    cloud = Cloud((x, y))
                    self.clouds.add(cloud)
                elif col == "43":
                    flag = Flag((x, y))
                    self.flag.add(flag)
                elif int(col) >= 0:
                    tile = Tile((x, y), tile_size, col)
                    self.tiles.add(tile)

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
        for enemy in self.enemies_weak:
            enemy.rect.x += enemy.direction.x * enemy.speed
            if enemy.rect.x < enemy.starting_coords[0] - 128 or enemy.rect.x > enemy.starting_coords[0] + 128:
                enemy.direction.x *= -1
            for sprite in self.tiles:
                if sprite.rect.colliderect(enemy.rect):
                    if enemy.direction.x < 0:
                        enemy.rect.left = sprite.rect.right
                    elif enemy.direction.x > 0:
                        enemy.rect.right = sprite.rect.left
                    enemy.direction.x *= -1

    def player_enemy_collision(self):
        player = self.player.sprite
        for sprite in self.enemies_weak:
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

    def player_flag_collisions(self):
        player = self.player.sprite
        if self.flag.sprite.rect.colliderect(player.rect):
            self.level_handler()

    def check_game_end(self):
        player = self.player.sprite
        return player.rect.top > screen_h or self.player.sprite.dead

    def draw(self):

        # Background
        self.display_surface.fill(self.ambience[self.level])
        self.display_surface.blit(self.background_image, (0, 0))

        # Level clouds

        self.clouds.update(self.world_shift)
        self.clouds.draw(self.display_surface)

        # Level flag

        self.flag.update(self.world_shift)
        self.flag.draw(self.display_surface)

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
        self.enemies_weak.update(self.world_shift)
        self.enemies_weak.draw(self.display_surface)
        self.player_enemy_collision()
        self.horizontal_world_enemies_movement_collision()

        # Level coins

        self.coins.update(self.world_shift)
        self.player_coin_collisions()
        self.coins.draw(self.display_surface)

        self.player_flag_collisions()
