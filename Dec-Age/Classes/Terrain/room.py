import pygame
class Room:
    doors = [] # list of doors (AreaGate objects)
    doorStates = [] # corresponds to doors with 0 open, 1 closed

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)