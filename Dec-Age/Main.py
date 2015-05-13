import sys
import pygame
from pygame.locals import *
from Classes.entities import player
from Classes.Terrain import room
import helperfunctions

global room, gameFileText, enemies, projectiles, walls, gamePlayer, gravity

"""
setup calls
"""
# globals
gameFileText = [] # array containing important information
room = pygame.sprite.Group() # current room
enemies = pygame.sprite.Group() # group for dealing with enemies
projectiles = pygame.sprite.Group() # group for dealing with projectiles
walls = pygame.sprite.Group() # group for dealing with walls
gamePlayer = pygame.sprite.Group()
gravity = helperfunctions.PVector(0, -1)

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

# pygame module related
pygame.init() # ready pygame module for use
GAMESURFACE = pygame.display.set_mode((1200,700)) # create game window
pygame.display.set_caption('DecAge - A Race for Space Against Time') # set game window caption

# create player
px = 0
py = 0
ph = 100
pw1 = gameFileText[0][0]
pw2 = gameFileText[0][1]
player.Player(pw1, pw2, ph, px, py).add(gamePlayer)

# create health bar object
healthbar = helperfunctions.HPBar(10, 10, 100, 20).hp = 100

# load up hub with unlocked levels TODO: create hub


"""
main game loop
"""
ticks = 0
titleImage = pygame.image.load('images\\Title.png')
while True:
    """
    event handles
    """
    for event in pygame.event.get():
        ### handles go here. Use if \n elif format
        # game controls --
        # pause          p
        # use weapon     lclick
        # switch weapon  e
        # use Device     j
        # move           wasd
        # pick up weapon q
        if event.type == KEYUP:
            # key controls
            keyStates = pygame.key.get_pressed()


        elif event.type == QUIT:
            pygame.quit()
            sys.exit()

    """
    game logic, etc
    """

    # first, draw everything in its current state.
    # image layering is as follows:
    # background (room sprite variable 'image')
    # walls
    # doors
    # enemies
    # player
    # projectiles
    #room.draw(GAMESURFACE) # TODO: fix image displays
    #walls.draw(GAMESURFACE)
    #enemies.draw(GAMESURFACE)
    #gamePlayer.draw(GAMESURFACE)
    #projectiles.draw(GAMESURFACE)


    # first few seconds, display the title image for a bit over everything else
    if ticks < 500:
        GAMESURFACE.blit(titleImage, (0,0))

    """
    pygame.update and tick update. DO NOT WRITE GAME LOGIC AFTER THIS LINE
    """
    ticks += 1
    pygame.display.update