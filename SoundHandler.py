import pygame


class SoundHandler:
    def __init__(self):
        self.level_bg_music = pygame.mixer.Sound('media/audio/grasslands_theme.wav')
        self.level_bg_music.set_volume(0.1)
        self.level_bg_music.play(loops=-1)

    def set_background_music(self, volume):
        if 0 < volume < 1:
            self.level_bg_music.set_volume(volume)
