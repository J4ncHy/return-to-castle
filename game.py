from dis import dis
from math import floor
from turtle import window_height, window_width
import pygame as pg
import os.path

pg.init()

window = (1024, 768)
screen = pg.display.set_mode(window)

bg = []
bg.append(pg.image.load(os.path.join('media', 'background_forest',
          'parallax-forest-back-trees.png')).convert_alpha())
bg.append(pg.image.load(os.path.join('media', 'background_forest',
          'parallax-forest-lights.png')).convert_alpha())
bg.append(pg.image.load(os.path.join('media', 'background_forest',
          'parallax-forest-middle-trees.png')).convert_alpha())
bg.append(pg.image.load(os.path.join('media', 'background_forest',
          'parallax-forest-front-trees.png')).convert_alpha())

player = pg.image.load(os.path.join('media', 'player.png')).convert_alpha()
player = pg.transform.scale(player, (256, 128))
player.set_clip(pg.Rect(0, 0, 64, 64))
player_sprite = player.subsurface(player.get_clip())

boss = pg.image.load(os.path.join('media', 'boss.png')).convert_alpha()
boss = pg.transform.scale(boss, (640, 320))
boss.set_clip(pg.Rect(0, 0, 64, 64))
boss_sprite = boss.subsurface(boss.get_clip())

floor = pg.image.load(os.path.join('media', 'floor.png')).convert_alpha()
floor = pg.transform.scale(floor, (64, 128))
floor.set_clip(pg.Rect(0, 0, 64, 64))
floor_sprite = floor.subsurface(floor.get_clip())

PLAYER_X = 200
PLAYER_Y = 200
PLAYER_VELOCITY_X = 0
PLAYER_VELOCITY_Y = 0
ACCELERATION = 2
MAX_VELOCITY = 2

GRAVITATIONAL_CONSTANT = 1

for i in range(len(bg)):
    bg[i] = pg.transform.scale(bg[i], window)


def draw():
    for img in bg:
        screen.blit(img, (0, 0))

    screen.blit(player_sprite, (PLAYER_X, PLAYER_Y))
    screen.blit(boss_sprite, (300, 300))
    screen.blit(floor_sprite, (200, 200))

    pg.display.flip()


def updatePlayer():
    global PLAYER_VELOCITY_X
    global PLAYER_X
    global PLAYER_VELOCITY_Y
    global PLAYER_Y

    gravity = 0.02

    print(PLAYER_VELOCITY_Y)

    #PLAYER_X += PLAYER_VELOCITY_X
    # if PLAYER_VELOCITY_X > 0:
    #    PLAYER_VELOCITY_X -= ACCELERATION
    PLAYER_VELOCITY_Y += gravity
    if PLAYER_VELOCITY_Y > 0:
        PLAYER_Y += PLAYER_VELOCITY_Y


disableJump = False
running = True
while running:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    if PLAYER_Y >= 700:
        PLAYER_VELOCITY_Y = 0
        PLAYER_Y = 699

    keys = pg.key.get_pressed()

    if keys[pg.K_LEFT] and PLAYER_X > 0:
        player.set_clip(pg.Rect(64, 64, 64, 64))
        player_sprite = player.subsurface(player.get_clip())
        #PLAYER_VELOCITY_X -= 1
        PLAYER_X -= 2

    if keys[pg.K_RIGHT] and PLAYER_X < window[0] - 64:
        player.set_clip(pg.Rect(0, 0, 64, 64))
        player_sprite = player.subsurface(player.get_clip())
        #PLAYER_VELOCITY_X += 1
        PLAYER_X += 2

    if keys[pg.K_UP] and PLAYER_Y > 0 and abs(PLAYER_VELOCITY_Y) < MAX_VELOCITY:
        #PLAYER_VELOCITY_Y -= 5
        PLAYER_VELOCITY_Y -= 5
        #disableJump = True

    # if keys[pg.K_DOWN] and PLAYER_Y < window[1] - 64:
    #    PLAYER_VELOCITY_Y -= 5

    # if PLAYER_Y <= 700 and PLAYER_VELOCITY_Y <= MAX_VELOCITY:
    #    PLAYER_VELOCITY_Y += ACCELERATION

        #disableJump = False

    # if PLAYER_Y < 0:
    #    PLAYER_VELOCITY_Y = 0
    #    PLAYER_Y = 0

    #print(PLAYER_X, PLAYER_Y, PLAYER_VELOCITY_X, PLAYER_VELOCITY_Y)

    # print(pg.mouse.get_pressed())

    if pg.mouse.get_pressed() == (1, 0, 0):
        PLAYER_X, PLAYER_Y = pg.mouse.get_pos()

    updatePlayer()
    draw()
pg.quit()
