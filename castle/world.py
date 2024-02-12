from constants import *
class World:
    def __init__(self, image):
        self.image = image
        
    def draw(self):
        screen.blit(self.image, (0,0))