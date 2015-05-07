"""
Object controllable by the user by entering events
"""

class Player:
    x = '' # x coordinate
    y = '' # y coordinate
    width = 0  # with in pixels
    height = 0  # height in pixels
    health = ''  # current health
    maxHealth = ''  # maximum health
    sprite = ''  # image to display over self TODO: create and add sprite
    weapon1 = ''  # weapon 1
    weapon1CD = 0  # weapon 1 cooldown
    weapon2 = ''  # weapon 2
    weapon2CD = 0  # weapon 2 cooldown
    weaponActive = 1  # set to either 1 or 2 to tell which weapon is currently active
    statusFrames = 0  # number of frames left before player should revert to normal sprite again.

    def __init__(self, x_in, y_in, he_in, hem_in,  w1_in, w2_in):
        self.x = x_in
        self.y = y_in
        self.health = he_in
        self.maxHealth = hem_in
        self.weapon1 = w1_in
        self.weapon2 = w2_in

    def applyStatus(self, frames, sprite):
        self.statusFrames = frames
        self.sprite = sprite

    def updateStatus(self):
        self.statusFrames -= 1
        if self.statusFrames == 0:
            self.sprite = '' # reset sprite to default # TODO

    def swordAttack(self):
        cd = 20 # CONFIG: sword cooldown
        if self.weaponActive == 1:
            self.weapon1CD = cd
        else:
            self.weapon2CD = cd
        self.statusFrames = 15
        sprite = '' # set sprite to sword attack # TODO: create and add sprite

        # TODO: create sword hitbox and apply damage to enemies struck