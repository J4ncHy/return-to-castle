import pygame


def import_enemy_spritesheet(path, width, height):
    animation_library = {"idle": [], "attack1": [], "attack2": [], "run": [], "dead": []}

    sprite_sheet = pygame.image.load(path).convert_alpha()
    wid = sprite_sheet.get_width()

    for i in range(int(wid / width)):
        # Idle
        line = pygame.Surface((sprite_sheet.get_width(), height)).convert_alpha()
        line.blit(sprite_sheet, (0, 0), ((i * width), 0, width, height))
        line.set_colorkey((0, 0, 0))
        # surface_list.append(line)
        animation_library["idle"].append(line)

        # Attack 1
        line = pygame.Surface((sprite_sheet.get_width(), height)).convert_alpha()
        line.blit(sprite_sheet, (height, 0), ((i * width), height, width, height))
        line.set_colorkey((0, 0, 0))
        animation_library["attack1"].append(line)

        # Run
        line = pygame.Surface((sprite_sheet.get_width(), height)).convert_alpha()
        line.blit(sprite_sheet, (height, 0), ((i * width), 2 * height, width, height))
        line.set_colorkey((0, 0, 0))
        animation_library["run"].append(line)

        # Attack 2
        line = pygame.Surface((sprite_sheet.get_width(), height)).convert_alpha()
        line.blit(sprite_sheet, (height, 0), ((i * width), 3 * height, width, height))
        line.set_colorkey((0, 0, 0))
        animation_library["attack2"].append(line)

        # Dead
        line = pygame.Surface((sprite_sheet.get_width(), height)).convert_alpha()
        line.blit(sprite_sheet, (height, 0), ((i * width), 4 * height, width, height))
        line.set_colorkey((0, 0, 0))
        animation_library["dead"].append(line)

    return animation_library
