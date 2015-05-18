"""
Object that blocks the player's movement
"""
import pygame

class Wall(pygame.sprite.Sprite):
    width = 0
    height = 0
    # constructor
    def __init__(self, x_in, y_in, w_in, h_in, s_in, c_in):
        # parent constructor
        super().__init__()

        # set up image and rect
        self.image = pygame.Surface([w_in, h_in])
        self.image.fill(c_in)
        self.rect = self.image.get_rect()
        self.width = w_in
        self.height = h_in