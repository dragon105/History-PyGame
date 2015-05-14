import pygame
import helperfunctions

class Player(pygame.sprite.Sprite):
    location = helperfunctions.PVector(0, 0)
    velocity = helperfunctions.PVector(0,0)
    health = 0 # health
    image = ''
    rect = pygame.rect.Rect((0,0,0,0))
    w1 = '' # weapon 1
    w2 = '' # weapon 2
    wC = '' # weapon current
    timeSinceLastDamage = 1000 # ticks time since last damage taken
    healthRegenRate = 1.5 # rate at which player's health regens
    attackAnimationFrames = 0 # how long to continue the attack animation before resetting sprite. 0 for not attacking

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

    # get the player's image based on current weapon TODO: update to use sprite
    def get_image(self):
        if self.wC == '1':
            if self.attackAnimationFrames > 0:
                return pygame.image.load('images\\sprite-player-swordattack.png')
            else:
                 return pygame.image.load('images\\sprite-player-sword.png')
        elif self.wC == '2':
            if self.attackAnimationFrames > 0:
                return pygame.image.load('images\\sprite-player-knifeattack.png')
            else:
                return pygame.image.load('images\\sprite-player-knife.png')
        elif self.wC =='3':
            return pygame.image.load('images\\sprite-player-revolver.png')
        elif self.wC == '4': #TODO: other player sprites
            return ''

    # constructor. Pass in the player's weapons and current health, as well as location
    def __init__(self, w1, w2, h, x, y):

        # call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        self.health = h
        self.w1 = w1
        self.w2 = w2
        wC = w1
        self.location.set(x, y)
        self.image = self.get_image()
        self.rect = self.image.get_rect()
