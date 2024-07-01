from pygame.sprite import Sprite
import pygame
class ItemBox(Sprite):
    def __init__(self, type,item_boxes, x,y):
        super().__init__()
        self.type = type
        self.image = item_boxes[self.type]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        
    def update(self, player):
        if pygame.sprite.collide_rect(self, player):
            if self.type == "Health":
                player.health += 25
                if player.health > player.max_health:
                    player.health = player.max_health
            elif self.type == "Ammo":
                player.ammo += 20
                
            elif self.type == "Grenade":
                player.grenade += 4
                
            self.kill()
        