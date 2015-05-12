import pygame

# writes contents to the save file
def writeSaveFile(contents, file):
    file.seek(0,0)
    file.write(contents)

# physics vector, used for physics
class PVector:
    x = 0
    y = 0

    def set(self, x, y):
        self.x = x
        self.y = y

    def add(self, vector):
        self.x += vector.x
        self.y += vector.y

    def __init__(self, x, y):
        self.set(x, y)

# health bar on screen
class HPBar:
    # dimension configs
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0

    # current health
    hp = 0

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = y2
        self.y2 = y2

    # draws based on current hp
    def draw(self, surface):
        color1 = (255, 0, 0)# background color of HP bar
        color2 = (0, 255, 0) # bar color

        pygame.draw.rect(surface, color1, (self.x1, self.y1, self.x2, self.y2), 2)
        pygame.draw.rect(surface, color2, (self.x1, self.y1, (self.hp / 100) * (self.x2 - self.x1), self.y2), 0)