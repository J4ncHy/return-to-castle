import pygame
import csv

from Enemy import Enemy
from StateEnum import StateEnum
from Tiles import Tiles
from settings import s
from Player import Player
from PowerUps import Powerups
from Coin import Coin
from Cloud import Cloud
from Bullet import Bullet
from Flag import Flag
from SoundHandler import SoundHandler
from HighscoreHandler import write_score
from Spikes import Spike


class Level:
    def __init__(self, display, surface, menu, main_menu):
        self.main_menu = main_menu
        self.level = 0
        self.cnt = 0
        self.ambience = [(135, 206, 235), (135, 206, 235), (178, 227, 247), (255, 248, 219), (244, 128, 55), (0, 0, 0)]

        self.menu = menu

        self.start_time = None

        self.enemies_guns = None
        self.flag = None
        self.clouds = None
        self.powerups = None
        self.tiles = None
        self.player = None
        self.enemies_weak = None
        # self.bullets = None
        self.spikes = None
        self.coins = None
        self.background_image = None

        self.sound = SoundHandler()

        self.display_surface = display
        self.srf = surface
        self.setup_level(self.import_level_from_tilemap())
        self.world_shift = 0

        self.score = 0

    def import_assets(self):
        # Function imports all required assets, and specifically the tile set is saved into an array for easier use
        background_img = "level/background/BG{}.png".format(self.level)  # "media/background_cloud.png"
        self.background_image = pygame.image.load(background_img).convert_alpha()

    def level_handler(self, level):
        self.score = 0
        self.level = level

        self.menu.deleteTextBox()
        self.menu.text_arr = []
        del self.start_time
        del self.enemies_guns
        del self.flag
        del self.clouds
        del self.powerups
        del self.tiles
        del self.player
        del self.enemies_weak
        del self.coins
        del self.background_image
        del self.spikes

        self.world_shift = 0
        self.setup_level(self.import_level_from_tilemap())

    def import_level_from_tilemap(self):
        level_arr = []
        with open("level/level{}.csv".format(self.level), newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in spamreader:
                level_arr.append(row)
        return level_arr

    def setup_level(self, layout):
        coords = {"coin": 0, "player": 0, "enemy": 0}
        self.import_assets()

        self.start_time = pygame.time.get_ticks()

        self.tiles = pygame.sprite.Group()
        self.enemies_weak = pygame.sprite.Group()
        self.enemies_guns = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.powerups = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()
        self.clouds = pygame.sprite.Group()
        self.flag = pygame.sprite.GroupSingle()
        self.spikes = pygame.sprite.Group()

        for i, row in enumerate(layout):
            for j, col in enumerate(row):
                y = i * s.tile_size
                x = j * s.tile_size

                if col == "49":
                    playerSprite = Player((x, y), self.sound, self.main_menu)
                    self.player.add(playerSprite)
                    if coords["player"] == 0:
                        coords["player"] = x
                elif col == "45":
                    powerup = Powerups((x, y))
                    self.powerups.add(powerup)
                elif col == "42":
                    enemy = Enemy((x, y))
                    self.enemies_weak.add(enemy)
                elif col == "50":
                    coin = Coin((x, y))
                    self.coins.add(coin)
                    if coords["coin"] == 0:
                        coords["coin"] = x
                elif col == "48":
                    cloud = Cloud((x, y))
                    self.clouds.add(cloud)
                elif col == "43":
                    flag = Flag((x, y))
                    self.flag.add(flag)
                elif col == "52":
                    spike = Spike((x, y))
                    self.spikes.add(spike)
                elif int(col) >= 0:
                    tile = Tiles((x, y), s.tile_size, col)
                    self.tiles.add(tile)

        if self.level == 0:
            self.menu.createText(pygame.Rect(coords["player"], 200, 250, 180), "Use the arrow keys to move and jump")
            self.menu.createText(pygame.Rect(coords["coin"], 200, 120, 180), "Pick up coins")
            self.menu.createText(pygame.Rect(1400, 200, 260, 180), "Robbers have taken your castle and they hold your princess hostage")
            self.menu.createText(pygame.Rect(1900, 200, 270, 180), "You need to save her")

    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x
        speed = player.default_speed

        if player_x < 0.4 * s.screen_w and direction_x < 0:
            self.world_shift = speed
            player.speed = 0
        elif player_x > 0.6 * s.screen_w and direction_x > 0:
            self.world_shift = -speed
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = speed

    def horizontal_world_player_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for tile in self.tiles:
            if tile.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = tile.rect.right
                elif player.direction.x > 0:
                    player.rect.right = tile.rect.left

    def vertical_world_player_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()

        for tile in self.tiles:
            if tile.rect.colliderect(player.rect):
                # if pygame.sprite.collide_mask(player, tile):
                if player.direction.y > 0:
                    player.rect.bottom = tile.rect.top
                    player.direction.y = 0
                    player.jump_count = 0
                elif player.direction.y < 0:
                    player.rect.top = tile.rect.bottom
                    player.direction.y = 0

    def horizontal_world_enemies_movement_collision(self):
        for enemy in self.enemies_weak:
            enemy.rect.x += enemy.direction.x * enemy.speed
            if enemy.rect.x < enemy.starting_coords[0] - (128 * s.scale_w) or enemy.rect.x > enemy.starting_coords[0] + (128 * s.scale_w):
                enemy.direction.x *= -1
            for tile in self.tiles:
                if tile.rect.colliderect(enemy.rect):
                    # if pygame.sprite.collide_mask(enemy, tile):
                    if enemy.direction.x < 0:
                        enemy.rect.left = tile.rect.right
                    elif enemy.direction.x > 0:
                        enemy.rect.right = tile.rect.left
                    enemy.direction.x *= -1

    def player_enemy_collision(self):
        player = self.player.sprite
        for enemy in self.enemies_weak:
            if pygame.sprite.collide_mask(player, enemy) and enemy.status != "dead":
                if player.attack:
                    enemy.status = "dead"
                    enemy.animation_speed = 0.10
                else:
                    player.dead = True
                    self.main_menu.set_state(StateEnum.DEAD_MENU)

    def player_powerups_collision(self):
        player = self.player.sprite
        for powerup in self.powerups:
            if pygame.sprite.collide_mask(player, powerup):
                player.update_speed(1.25)
                powerup.kill()
                self.sound.play_speedup()

    def player_coin_collisions(self):
        player = self.player.sprite
        for coin in self.coins:
            if pygame.sprite.collide_mask(player, coin):
                self.score += 10
                coin.kill()
                self.sound.play_coin()

    def player_flag_collisions(self):
        player = self.player.sprite
        if pygame.sprite.collide_mask(player, self.flag.sprite):
            time = (pygame.time.get_ticks() - self.start_time) / 1000
            write_score(level=self.level, score=self.score, time=round(time, 1))
            self.level_handler(self.level+1)

    def player_spikes_collisions(self):
        player = self.player.sprite
        for spike in self.spikes:
            if pygame.sprite.collide_mask(player, spike):
                self.main_menu.set_state(StateEnum.DEAD_MENU)
                player.dead = True

    def check_game_end(self):
        player = self.player.sprite
        return player.rect.top > s.screen_h or self.player.sprite.dead

    def draw(self, ticks):

        # Background

        self.srf.fill(self.ambience[self.level])
        self.srf.blit(self.background_image, (0, 0))

        # Level clouds

        self.clouds.update(self.world_shift)
        self.clouds.draw(self.srf)

        # Level flag

        self.flag.update(self.world_shift)
        self.flag.draw(self.srf)

        # Level tiles
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.srf)
        self.scroll_x()

        # Level player
        self.player.update()
        self.horizontal_world_player_movement_collision()
        self.vertical_world_player_movement_collision()
        self.player.draw(self.srf)

        # Level powerups
        self.powerups.draw(self.srf)
        self.player_powerups_collision()
        self.powerups.update(self.world_shift)

        # Level enemies
        self.enemies_weak.update(self.world_shift)
        self.enemies_weak.draw(self.srf)
        self.player_enemy_collision()
        self.horizontal_world_enemies_movement_collision()

        # Level coins

        self.coins.update(self.world_shift)
        self.player_coin_collisions()
        self.coins.draw(self.srf)

        # Level spikes

        self.spikes.update(self.world_shift)
        self.player_spikes_collisions()
        self.spikes.draw(self.srf)

        # Draw menu items

        self.main_menu.draw_score(self.score)
        time = (pygame.time.get_ticks() - self.start_time) / 1000
        self.main_menu.draw_time(round(time, 1))

        self.main_menu.update(self)

        self.menu.update(ticks, self.world_shift, self.player.sprite.rect.x)

        # Level player collision

        self.player_flag_collisions()

        # Resize

        self.display_surface.blit(pygame.transform.scale(self.srf, (s.original_w * s.scale_w, s.original_h * s.scale_h)), (0, 0))
