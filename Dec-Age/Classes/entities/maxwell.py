"""
BBEG of game.
"""

import pygame
import random
from Classes.entities import projectiles

class Maxwell(pygame.sprite.Sprite):
    health = 2500
    speed = 2 # move speed

    chargingFrames = 0 # frames to display charging animation for charged attacks
    chargingLaserFrames = 0 # like chargingFrames, but specifically for his Big Laser attacks

    queuedAttack = '' # attack to queue when chargingFrames is done. Attack is fired when chargingFrames = 1

    timeSinceLastAttack = 0 # time since last used an attack

    doing_bigLaserframes = 0 # frames to display firing his Big Laser attack
    doing_octaLaserFrames = 0 # frames to display firing his Octa Laser attack.

    # constructor
    def __init__(self):

        # parent class constructor
        super().__init__()
        self.image = pygame.image.load('images\\sprite-maxwell-highhealth.png').convert()
        self.rect = self.image.get_rect()
        self.rect.x = 1000
        self.rect.y = 400

    def update(self):
        # moves randomly
        speed = self.speed
        if ((self.chargingFrames + self.chargingLaserFrames + self.doing_bigLaserframes + self.doing_octaLaserFrames) == 0):
            speed /= 2
        direction = random.randint(0,3)
        if (direction == 0):
            self.rect.y -= speed
        elif (direction == 1):
            self.rect.x += speed
        elif (direction == 2):
            self.rect.y += speed
        else:
            self.rect.x -= speed

        # queues attacks once per 400 frames if high on health, 250 otherwise.
        lowHealth = False
        if ((self.health / 2500) <= 0.33):
            lowHealth = True

        if(self.timeSinceLastAttack >= 400 or (self.timeSinceLastAttack >= 250 and lowHealth == True)):
            self.timeSinceLastAttack = 0
            if (lowHealth == True):
                attack = random.randint(0,5)
                if (attack == 0):
                    self.queuedAttack = 'rocket'
                    self.chargingFrames = 15
                    self.image = pygame.image.load('images\\sprite-maxwell-lowhealth-charging').convert()
                elif (attack == 1):
                    self.queuedAttack = 'cone'
                    self.chargingFrames = 15
                    self.image = pygame.image.load('images\\sprite-maxwell-lowhealth-charging').convert()
                elif (attack == 2):
                    self.queuedAttack = 'biglaser'
                    self.chargingLaserFrames = 20
                    self.image = pygame.image.load('images\\sprite-maxwell-lowhealth-chargingbiglaser').convert()
                elif (attack == 3):
                    self.queuedAttack = 'trirocket'
                    self.chargingFrames = 15
                    self.image = pygame.image.load('images\\sprite-maxwell-lowhealth-charging').convert()
                elif (attack == 4):
                    self.queuedAttack = 'bigcone'
                    self.chargingFrames = 15
                    self.image = pygame.image.load('images\\sprite-maxwell-lowhealth-charging').convert()
                else:
                    self.queuedAttack = 'octalaser'
                    self.chargingLaserFrames = 20
                    self.image = pygame.image.load('images\\sprite-maxwell-lowhealth-chargingbiglaser').convert()

        # attack if charge time is complete and return created projectiles so that they can be added to their respective groups in Main
        # pass in gamePlayer Group object. returns projectile objects or groups
        def getAttackProjectiles(target):
            if ((self.chargingFrames + self.chargingLaserFrames) == 1): #TODO: add creation of projectiles
                if (self.queuedAttack == 'rocket'):
                    self.image = pygame.image.load('images\\sprite-maxwell-lowhealth').convert()
                    # get velocity based on player's location relative to maxwell's


                    rocket = projectiles.projectile()
                elif (self.queuedAttack == 'cone'):
                    self.image = pygame.image.load('images\\sprite-maxwell-lowhealth').convert()
                elif (self.queuedAttack == 'biglaser'):
                    self.image = pygame.image.load('images\\sprite-maxwell-lowhealth-shoop').convert()
                elif (self.queuedAttack == 'trirocket'):
                    self.image = pygame.image.load('images\\sprite-maxwell-lowhealth').convert()
                elif (self.queuedAttack == 'bigcone'):
                    self.image = pygame.image.load('images\\sprite-maxwell-lowhealth').convert()
                else:
                    self.image = pygame.image.load('images\\sprite-maxwell-lowhealth-octashoop').convert()

        # update time keeping variables
        self.chargingFrames -= 1
        self.chargingLaserFrames -= 1
        self.doing_bigLaserframes -= 1
        self.doing_bigLaserframes -= 1
        self.doing_octaLaserFrames -= 1
        self.timeSinceLastAttack += 1