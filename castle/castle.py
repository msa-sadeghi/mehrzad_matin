from constants import *
from bullet import Bullet
import math
class Castle:
    def __init__(self,image100, x,y, scale):
        self.health = 1000
        self.max_health = self.health
        
        width = image100.get_width()
        height = image100.get_height()
        
        self.image100 = pygame.transform.scale(image100, (width * scale, height * scale))
        self.rect = self.image100.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False
        self.last_shoot_time = pygame.time.get_ticks()
        
    def draw(self):
        self.image = self.image100
        screen.blit(self.image, self.rect)
        
    def shoot(self, bullet_group):
        mouse_position = pygame.mouse.get_pos()
        x_dist = mouse_position[0] - self.rect.midleft[0]
        y_dist = -(mouse_position[1] - self.rect.midleft[1])
        self.angle = math.atan2(y_dist, x_dist)
        if pygame.mouse.get_pressed()[0] and not self.clicked and pygame.time.get_ticks() - self.last_shoot_time > 1000:
            bullet = Bullet(bullet_image, self.rect.midleft[0], self.rect.midleft[1], self.angle)
            bullet_group.add(bullet)
            self.clicked = True
            self.last_shoot_time = pygame.time.get_ticks()
        if not pygame.mouse.get_pressed()[0]:
            self.clicked = False
        
        