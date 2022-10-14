import pygame


class Text:

    def __init__(self, text, x_pos, y_pos, font_size):

        self.font = pygame.font.Font('assets/sans.otf', font_size)

        self.text = text
        self.x_pos = x_pos
        self.y_pos = y_pos

        self.name = self.font.render(self.text, True, (0, 0, 0))
        self.rect = self.name.get_rect()
        self.rect.center = (self.x_pos, self.y_pos)  # 150 25
