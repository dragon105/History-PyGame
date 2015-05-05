"""
Object that, when hit by the player's hitbox, moves the player to the gate's corresponding area.
"""

class AreaGate:
    x = "" # x coordinate
    y = "" # y coordinate
    width = "" # with in pixels
    height = "" # height in pixels
    target = "" # room to take player to
    sprite = "" # image to display over self
    px = "" # new player x coordinate
    py = "" # new player y coordinate

    # constructor
    def __init__(self, x_in, y_in, w_in, h_in, t_in, s_in):
        self.x = x_in
        self.y = y_in
        self.width = w_in
        self.height = h_in
        self.target = t_in
        self.sprite = s_in

    # transitions area to target when called
    def roomTransition(self):
        global room
        room = self.target
        # set player coordinates for new area
