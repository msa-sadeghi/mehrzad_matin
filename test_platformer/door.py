from constants import *
from pygame.sprite import Sprite

class Door(Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load("assets/img/exit.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        