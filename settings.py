#tile_size = 64
#
#original_w = 1200
#original_h = 12 * tile_size
#
#screen_w = 1200
#screen_h = 12 * tile_size
#scale_w = 1.0
#scale_h = 1.0

class Settings:
    def __init__(self):
        self.tile_size = 64
        self.original_w = 1200
        self.original_h = 12 * self.tile_size
        self.screen_w = 1200
        self.screen_h = 12 * self.tile_size
        self.scale_w = 1.0
        self.scale_h = 1.0


s = Settings()