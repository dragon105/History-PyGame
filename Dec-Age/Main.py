import sys
import pygame
from pygame.locals import *
from Helper_functions import filehandling
from Classes.entities import player

global room, doors, doorStates, gameFileText

"""
setup calls
"""
# globals
doors = [] # list of door objects
doorStates = [] # corresponds to doors. Contains a 0 for closed and a 1 for open

# pygame module related
pygame.init() # ready pygame module for use
DISPLAY = pygame.display.set_mode((1200,700)) # create game window
pygame.display.set_caption('DecAge - A Race for Space Against Time') # set game window caption

# ready game file
gameFileText = open('gameTextFile', 'a') # create a blank file if file does not exists
gameFileText.close()
gameFileText = filehandling.getFileLines()
if gameFileText[0] == '':
    filehandling.writeFile("Save file for DecAge\nPlayer Max Health: 100\nPlayer Weapons: s_\nRooms Beaten: ")
    gameFileText = filehandling.getFileLines()

# create player
px = 500
py = 500
phe = gameFileText[1][19:-1]
phem = phe
pw1 = gameFileText[2][16]
pw2 = gameFileText[2][17]
gamePlayer = player.Player(px, py, int(phe), int(phem), pw1, pw2)

# load up hub with unlocked levels TODO: create hub

"""
main game loop
"""
while True:
    # event handling
    for event in pygame.event.get():
        # handles go here

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # game stuff goes here
    if gamePlayer.statusFrames > 0: # update player's statusFrames variable if it's above 0
        gamePlayer.updateStatus()

    # nothing in the loop after this line
    pygame.display.update