import pygame
class Room(pygame.sprite.Sprite):
    doors = [] # list of doors (AreaGate objects)
    doorStates = [] # corresponds to doors with 0 open, 1 closed

    # constructor. pass in room name to initialize
    def __init__(self):
        print() # TODO