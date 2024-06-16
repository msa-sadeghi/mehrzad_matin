from pygame.sprite import Sprite

import pygame

class Explosion(Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.images = []
        for i in range(1,6):
            img = pygame.image.load(f"assets/images/explosion/exp{i}.png")
            img_w = img.get_width()
            img_h = img.get_height()
            img = pygame.transform.scale(img, (img_w * 0.3, img_h * 0.3))
            self.images.append(img)
            
        self.image_number = 0
        self.image = self.images[self.image_number]
        self.rect = self.image.get_rect(center=(x,y))
        self.animation_time = pygame.time.get_ticks()
        
    def update(self):
        if pygame.time.get_ticks() - self.animation_time > 100:
            self.animation_time = pygame.time.get_ticks()
            self.image_number += 1
            if self.image_number >= len(self.images):
                self.kill()
            else:
                self.image = self.images[self.image_number]
        
        