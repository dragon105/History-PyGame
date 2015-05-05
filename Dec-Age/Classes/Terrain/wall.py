"""
Object that blocks the player's movement
"""

class Wall:
    x = "" # x coordinate
    y = "" # y coordinate
    width = "" # width in pixels
    height = "" # height in pixels
    sprite = "" # height in pixels

    # constructor
    def __init__(self, x_in, y_in, w_in, h_in, s_in):
        self.x = x_in
        self.y = y_in
        self.width = w_in
        self.height = h_in
        self.sprite = s_in