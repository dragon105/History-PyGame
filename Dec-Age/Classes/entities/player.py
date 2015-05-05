"""
Object controllable by the user by entering events
"""

class Player:
    x = '' # x coordinate
    y = '' # y coordinate
    width = '' # with in pixels
    height = '' # height in pixels
    health = '' # current health
    maxHealth = '' # maximum health
    sprite = '' # image to display over self
    weapon1 = '' # weapon 1
    weapon2 = '' # weapon 2
    weaponActive = '' # set to either 1 or 2 to tell which weapon is currently active

    def __init__(self, x_in, y_in, w_in, h_in, he_in, w1_in, w2_in):
        self.x = x_in
        self.y = y_in
        self.width = w_in
        self.height = h_in
        self.health = he_in
        self.weapon1 = w1_in
        self.weapon2 = w2_in
        self.weaponActive = '1'