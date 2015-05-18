import pygame
class projectile (pygame.sprite.Sprite):
    velocity = [0,0] # contains speed in x direction and y direction, respectively

    # constructor. pass in velocity and location, as well as sprite image
    def __init__(self, vel_in, x, y, img):
        # call the parent class (Sprite) constructor
        super().__init__()
        self.velocity[0] = vel_in[0]
        self.velocity[1] = vel_in[1]

        # set up sprite and rect
        self.image = pygame.image.load(img).convert()
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]