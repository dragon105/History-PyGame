import sys
import pygame
from pygame.locals import *
from Classes.entities import player
from Classes.levels import hub
import helperfunctions

global room, doors, doorStates, gameFileText

"""
setup calls
"""
# globals
doors = [] # list of door objects
doorStates = [] # corresponds to doors. Contains a 0 for closed and a 1 for open
gameFileText = []

# pygame module related
pygame.init() # ready pygame module for use
DISPLAY = pygame.display.set_mode((1200,700)) # create game window
pygame.display.set_caption('DecAge - A Race for Space Against Time') # set game window caption

# ready game file
open('gameTextFile', 'a').close() # if file does not exist, create it.
file = open('gameTextFile', 'r+')
for line in file: # copy lines from file into array for easy reading
    gameFileText.append(line[:-1])
if file.readline() == '': # if file is blank, write the starting file content into it
    helperfunctions.writeSaveFile('__\n0\n', file)
    for line in file:
        gameFileText.append(line[:-1])
file.close() # we don't need the file open anymore, unless we want to write a save.

# create player
px = 0
py = 0
ph = 100
pw1 = gameFileText[0][0]
pw2 = gameFileText[0][1]
gamePlayer = player.Player(pw1, pw2, ph, px, py)

# create health bar object
HUD = helperfunctions.HPBar(10, 10, 100, 20).hp = 100

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
    if gamePlayer.spriteFrames > 0: # update player's statusFrames variable if it's above 0
        gamePlayer.updateStatus()

    # nothing in the loop after this line
    pygame.display.update