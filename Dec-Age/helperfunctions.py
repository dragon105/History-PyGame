import pygame

# writes contents to the save file
def writeSaveFile(contents, file):
    file.seek(0,0)
    file.write(contents)

# health bar on screen
class HPBar(pygame.sprite.Sprite):

    # constructor, pass in location and dimensions
    def __init__(self, x1, y1, health, height):
        # call the parent class (Sprite) constructor
        super.__init__()

        self.image = pygame.Surface([health, height])
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
