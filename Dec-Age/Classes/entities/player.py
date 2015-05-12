import pygame
import helperfunctions

class Player(pygame.sprite.Sprite):
    location = helperfunctions.PVector(0, 0)
    velocity = helperfunctions.PVector(0,0)
    health = 0 # health
    w1 = '' # weapon 1
    w2 = '' # weapon 2
    wC = '' # weapon current
    image = '' # image to display
    timeSinceLastDamage = 1000 # ticks time since last damage taken
    healthRegenRate = 1.5 # rate at which player's health regens

    """
    list of weapons and corresponding names in code
    weapon     name
    sword      1
    knife      2
    revolver   3
    sniper     4
    MG         5
    RPG        6
    peacemaker 7
    guitar     8
    bass       9
    mic        a
    drum       b
    starfish   c
    staff      d
    lander     e
    """

    attackAnimationFrames = 0 # how long to play the attack animation before resetting sprite

    # constructor. Pass in the player's weapons and current health, as well as location
    def __init__(self, w1, w2, h, x, y):
        self.health = h
        self.w1 = w1
        self.w2 = w2
        wC = w1
        self.location.set(x, y)

        # call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

    # get the player's image based on current weapon
    def getImage(self):
        img = ''
        if self.wC == '1':
            if self.attackAnimationFrames > 0:
                img = 'images\\sprite-player-swordattack'
            else:
                img = 'images\\sprite-player-sword'
        elif self.wC == '2':
            if self.attackAnimationFrames > 0:
                img = 'images\\sprite-player-knifeattack'
            else:
                img = 'images\\sprite-player-knife'
        elif self.wC =='3':
            img = 'images\\sprite-player-revolver'
        elif self.wC == '4':
            img = ''
        self.image = pygame.image.load(img)
