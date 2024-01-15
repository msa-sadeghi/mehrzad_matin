from constants import *
from pygame.sprite import Sprite

class Lava(Sprite):
    def __init__(self,x,y):
        super().__init__()
        img = pygame.image.load("assets/img/lava.png")
        self.image = pygame.transform.scale(img, (img.get_width() * 2, img.get_height()*2))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        