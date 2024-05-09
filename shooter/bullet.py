from pygame.sprite import Sprite
import pygame
class Bullet(Sprite):
    def __init__(self, x,y, direction):
        super().__init__()
        self.speed = 4
        self.image = pygame.image.load("assets/images/icons/bullet.png")
        self.rect = self.image.get_rect(center=(x,y))
        self.direction = direction
        
    def update(self, player, enemy, bullet_group):
        self.rect.x += self.direction * self.speed
        if self.rect.right < 0 or self.rect.left > 800:
            self.kill()
            
        if pygame.sprite.spritecollide(player, bullet_group, False):
            if player.alive:
                player.health -= 20
                self.kill()
        if pygame.sprite.spritecollide(enemy, bullet_group, False):
            if enemy.alive:
                enemy.health -= 20
                self.kill()
            
            
            