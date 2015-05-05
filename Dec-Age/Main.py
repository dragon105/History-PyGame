import pygame, sys

from pygame.locals import *

global room, doors, doorStates
room = 'hub' # start game in History Hub
doors = [] # list of doors
doorStates = [] # corresponds to doors. Contains a 0 for closed and a 1 for open

pygame.init()
DISPLAY = pygame.display.set_mode((1200,700))
pygame.display.set_caption('DecAge')

# main game loop
while True:
    # event handling
    for event in pygame.event.get():
        # handles go here

        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    # game stuff goes here


    pygame.display.update

# load level 'hub'
def loadHub:
    