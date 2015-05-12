import pygame

class Hub:
    background = pygame.image.load('images.background-hub')
    levelsCleared = ''
    # constructor
    def __init__(self, levelsCleared):
        # create background, music, doors, and other objects
        self.levelsCleared = levelsCleared