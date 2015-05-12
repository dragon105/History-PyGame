import pygame
import helperfunctions

class Player(pygame.sprite.Sprite):
    location = helperfunctions.PVector(0, 0)
    velocity = helperfunctions.PVector(0,0)
    health = 0 # health
    image = ''
    rect = ''
    w1 = '' # weapon 1
    w2 = '' # weapon 2
    wC = '' # weapon current
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

    # get the player's image based on current weapon
    def getImage(self):
        img = ''
        if self.wC == '1':
            if self.attackAnimationFrames > 0:
                img = 'images\\sprite-player-swordattack.png'
            else:
                img = 'images\\sprite-player-sword.png'
        elif self.wC == '2':
            if self.attackAnimationFrames > 0:
                img = 'images\\sprite-player-knifeattack.png'
            else:
                img = 'images\\sprite-player-knife.png'
        elif self.wC =='3':
            img = 'images\\sprite-player-revolver.png'
        elif self.wC == '4':
            img = ''
        self.image = pygame.image.load(img, ".png")
        self.rect = (self.location.x, self.location.y, self.image.get_width(), self.image.get_height())

    # constructor. Pass in the player's weapons and current health, as well as location
    def __init__(self, w1, w2, h, x, y):
        self.health = h
        self.w1 = w1
        self.w2 = w2
        wC = w1
        self.location.set(x, y)

        # call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        # call previous functions to avoid crashes when game logic section of main loop asks for player's image and rect to draw player
        self.getImage()