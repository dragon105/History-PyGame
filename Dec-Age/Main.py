import sys
import pygame

from pygame.locals import *
from Classes.entities import player
from Classes.Terrain import wall
from Classes.entities import damageField
from Classes.entities import damageField
import helperfunctions

global gameFileText, gravity, paused

"""
setup calls
"""
pygame.init()

# initial variable sets and pygame groups
gameFileText = [] # array containing important information
enemies = pygame.sprite.Group() # group for dealing with enemies
walls = pygame.sprite.Group() # group for dealing with walls
doors = pygame.sprite.Group()
gamePlayer = pygame.sprite.Group() # group for dealing with player
explosions = pygame.sprite.Group() # group for dealing with explosion animations
flowers = pygame.sprite.Group () # group for dealing with flower puff animations
gravity = -1 # gravity affecting player's and enemies' velocity
paused = False
# groups for dealing with each kind of projectile
bbegrocket_group = pygame.sprite.Group()
biglaser_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
fireball_group = pygame.sprite.Group()
laser_group = pygame.sprite.Group()
lightning_group = pygame.sprite.Group()
peace_group = pygame.sprite.Group()
rocket_group = pygame.sprite.Group()
starfish_group = pygame.sprite.Group()
lander_group = pygame.sprite.Group()

# ready game file
open('gameTextFile', 'a').close() # if file does not exist, create it.
file = open('gameTextFile', 'r+')
if file.readline() == '': # if file is blank, write the starting file content into it
    file.seek(0,0)
    file.write('__\n0\n')
    gameFileText.append('__\n0\n')
else:
    file.seek(0,0)
    for line in file: # copy lines from file into array for easy reading
        gameFileText.append(line[:-1])

file.close() # we don't need the file open anymore, unless we want to write a save.

# create game window
SCREEN = pygame.display.set_mode((1200,700)) # create game window
pygame.display.set_caption('DecAge - A Race for Space Against Time') # set game window caption

# create player
px = 100
py = 350
ph = 100
pw1 = gameFileText[0][0]
pw2 = gameFileText[0][1]
p = player.Player(pw1, pw2, ph, px, py)
p.add(gamePlayer)

# create health bar object
healthbar = helperfunctions.HPBar(10, 10, 100, 20).hp = 100

# load up hub with unlocked levels TODO: create hub



def Main():
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
            # move           wad
            # pick up weapon q
            if event.type == KEYDOWN:
                # key controls
                keyStates = pygame.key.get_pressed() # TODO: bind actions to keys.
                if keyStates[112] == True: # p
                    paused = True
                elif keyStates[101] == True: # e
                    gamePlayer.sprites.swapweapon()
                elif keyStates[106] == True: # j
                    #use Device
                    print()
                elif keyStates[119] == True: # w
                    #jump
                    gamePlayer.sprites.jump()
                elif keyStates[97] == True: # a
                    # left
                    print()
                elif keyStates[115] == True: # d
                    # right
                    print()
                elif keyStates[113] == True: # q
                    # swap weapons
                    gamePlayer.spites.grabWeapon()

            elif event.type == MOUSEBUTTONUP:
                gamePlayer.sprites.attack()

            elif event.type == QUIT:
                pygame.quit()
                sys.exit()

        """
        game logic, etc
        """
        ##### player relating to walls
        # first, get a list of all walls the player has collided with.
        walls_hit = pygame.sprite.groupcollide(gamePlayer, walls, False, False)

        # player's falling velocity increases according to gravity. This is undone if player hits a wall from above
        gamePlayer.sprites.fallingVelocity += gravity
        for wall in walls_hit:
            # if player is standing on a wall, player's falling velocity is zero
            if ((wall.rect.y - wall.height) >= gamePlayer.sprites.rect.y):
                gamePlayer.sprites.fallingVelocity = 0

            # if player is hitting a wall from the left side or right side, player does not move through wall
            if (wall.rect.x < (gamePlayer.spites.rect.x + 50)):
                gamePlayer.sprites.rect.x -= gamePlayer.sprites.speed
            if ((wall.rect.x + wall.width) > gamePlayer.sprites.rect.x):
                gamePlayer.sprites.rect.x += gamePlayer.sprites.speed

        ##### player relating to physics
        # player should fall according to fallingVelocity
        gamePlayer.sprites.rect.y += gamePlayer.sprites.fallingVelocity

        ##### enemies relating to walls

        ##### enemies relating to physics

        ##### projectiles relating to walls
        ### bbegrocket
        projectiles_hit = pygame.sprite.spritecollide(walls, bbegrocket_group, True)
        for rocket in projectiles_hit:
            print()
            #TODO: spawn explosion animation

        ### biglaser
        pygame.sprite.spritecollide(walls, biglaser_group, True)

        ### bullet
        pygame.sprite.spritecollide(walls, bullet_group, True)

        ### fireball
        projectiles_hit = pygame.sprite.spritecollide(walls, fireball_group, True)
        for fireball in projectiles_hit:
            print()
            #TODO: spawn explosion animation, damage enemies in radius

        ### laser
        pygame.sprite.spritecollide(walls, laser_group, True)

        ### lightning
        pygame.sprite.spritecollide(walls, lightning_group, True)

        ### peace
        pygame.sprite.spritecollide(walls, peace_group, True)

        ### rocket
        projectiles_hit = pygame.sprite.spritecollide(walls, rocket_group, True)
        for rocket in projectiles_hit:
            print()
            #TODO: spawn explosion animation and damage enemies

        ### starfish
        projectiles_hit = pygame.spritecollide(walls, starfish_group, True)
        for star in projectiles_hit:
            print()
            #TODO: spawn explosion animation and damage enemies


        ##### projectiles relating to player

        ### BBEG rocket
        projectiles_hit = pygame.spritecollide(gamePlayer, bbegrocket_group, True)
        for rocket in projectiles_hit:
            gamePlayer.sprites.health -= 30
            #TODO: spawn explosion animation

        ### biglaser
        projectiles_hit = pygame.spritecollide(gamePlayer, biglaser_group, True)
        for laser in projectiles_hit:
            gamePlayer.sprites.health -= 7.5

        ### laser
        projectiles_hit = pygame.spritecollide(gamePlayer, laser_group, True)
        for laser in projectiles_hit:
            gamePlayer.sprites.health -= 10


        # first, draw everything in its current state.
        # image layering is as follows:
        # background
        # walls
        # doors
        # enemies
        # player
        # projectiles

        #TODO: draws


        # first few seconds, display the title image for a bit over everything else
        if ticks < 500:
            SCREEN.blit(titleImage, (0,0))

        """
        End of loop things
        """
        # clear the screen
        SCREEN.fill(255, 255, 255)

# calls
Main()