from pygame.sprite import Sprite
import pygame

class Grenade(Sprite):
    def __init__(self, x, y, direction):
        super().__init__()
        self.timer = 100
        self.vel_y = -11
        self.speed = 7
        self.image = pygame.image.load("assets/images/icons/grenade.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.direction = direction
        
    def update(self):
        self.vel_y += 1
        dx = self.direction * self.speed
        dy = self.vel_y
        
        self.rect.x += dx
        self.rect.y += dy