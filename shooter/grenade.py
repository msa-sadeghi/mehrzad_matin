from pygame.sprite import Sprite
import pygame
from explosion import Explosion
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
        
    def update(self, explosion_group, player, enemy):
        self.vel_y += 1
        dx = self.direction * self.speed
        dy = self.vel_y
        
        if self.rect.bottom + dy > 300:
            dy = 300 - self.rect.bottom
            self.speed = 0
        if self.rect.left < 0 or self.rect.right > 800:
            self.direction *=  -1
            dx = self.direction * self.speed
            
        self.rect.x += dx
        self.rect.y += dy
        self.timer -= 1
        if self.timer <= 0:
            self.kill()
            explosion = Explosion(self.rect.x, self.rect.y)
            explosion_group.add(explosion)
            if self.rect.centerx - player.rect.centerx < 100 and self.rect.centery - player.rect.centery < 100:
                player.health -= 50
            if self.rect.centerx - enemy.rect.centerx < 100 and self.rect.centery - enemy.rect.centery < 100:
                enemy.health -= 50