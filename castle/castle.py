from constants import *

class Castle:
    def __init__(self,image100, x,y, scale):
        self.health = 1000
        self.max_health = self.health
        
        width = image100.get_width()
        height = image100.get_height()
        
        self.image100 = pygame.transform.scale(image100, (width * scale, height * scale))
        self.rect = self.image100.get_rect()
        self.rect.topleft = (x,y)
        
    def draw(self):
        self.image = self.image100
        screen.blit(self.image, self.rect)