import pygame

class Door(pygame.sprite.Sprite):
    x = 0 # location x
    y = 0 # location y
    closed = False # closed or open?
    name = '' # used in Main. determines where the door will take the player when used.

    # constructor. Pass in location, closed state, and name
    def __init__(self, x, y, cstate, name):
        # parent class constructor (Sprite)
        pygame.sprite.Sprite.__init__(self)

        self.x = x
        self.y = y
        self.closed = cstate
        self.name = name

        if self.closed == False:
            self.image = pygame.image.load('images\\sprite-terrain-opendoor.png')
        else:
            self.image = pygame.image.load('images\\sprite-terrain-closeddoor.png')

    # opens the door and changes sprite to match
    def open(self):
        self.closed = False
        self.image = pygame.image.load('images\\sprite-terrain-opendoor.png')

    # closes the door and changes sprite to match
    def close(self):
        self.closed = True
        self.image = self.image = pygame.image.load('images\\sprite-terrain-closeddoor.png')