from settings import s

class Button:
    def __init__(self, pos, image, font, base_color,hover_color, text_input):
        self.x, self.y = pos

        self.image = image
        self.font = font
        self.base_color, self.hover_color = base_color, hover_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.text_rect = self.text.get_rect(center=(self.x, self.y))

    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def check_for_input(self, pos):
        if self.rect.left * s.scale_w < pos[0] < self.rect.right*s.scale_w and \
                self.rect.top*s.scale_h < pos[1] < self.rect.bottom*s.scale_h:
            return True
        return False

    def change_color(self, pos):
        if self.rect.left * s.scale_w < pos[0] < self.rect.right * s.scale_w and \
                self.rect.top * s.scale_h < pos[1] < self.rect.bottom * s.scale_h:
            self.text = self.font.render(self.text_input, True, self.hover_color)
            return
        self.text = self.font.render(self.text_input, True, self.base_color)
