import pygame


class SoundHandler:
    def __init__(self):
        self.level_bg_music = pygame.mixer.Sound('media/audio/grasslands_theme.wav')
        self.level_bg_music.set_volume(0)
        self.level_bg_music.play(loops=-1)

        self.jump_sound = pygame.mixer.Sound("media/audio/jump.wav")
        self.coin_pickup = pygame.mixer.Sound("media/audio/coin.wav")
        self.speed = pygame.mixer.Sound("media/audio/run.wav")

    def set_background_music(self, volume):
        if 0 < volume < 1:
            self.level_bg_music.set_volume(volume)

    def play_jump(self):
        self.jump_sound.set_volume(0.1)
        self.jump_sound.play(loops=0)

    def play_coin(self):
        self.coin_pickup.set_volume(0.1)
        self.coin_pickup.play(loops=0)

    def play_speedup(self):
        self.speed.set_volume(0.1)
        self.speed.play(loops=0)
