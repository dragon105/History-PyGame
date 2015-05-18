"""
Invisible sprite used to check collisions with explosions and apply damage.
"""

import pygame

class damageField(pygame.sprite.Sprite):
    # constructor. Pass in location, side length, group to check collisions with, and damage
    def __init__(self, x, y, len, targets, damage):
        # call the parent class (Sprite) constructor
        super().__init__()

        self.image = pygame.Surface([len, len])
        self.rect = self.image.get_rect()

        targetsHit = pygame.sprite.spritecollide(self, targets, False)
        for target in targetsHit:
            target.hp -= damage
        self.kill()