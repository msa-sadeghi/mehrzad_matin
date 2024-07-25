from pygame.sprite import Sprite
import pygame
class Tower(Sprite):
    def __init__(self, x,y, group, health, bullet):
        super().__init__()
        self.all_images = []
        for i in ("25", "50", "100"):
            img = pygame.image.load(f"assets/tower/tower_{i}.png")
            imgw = img.get_width()
            imgh = img.get_height()
            img = pygame.transform.scale(img, (imgw * 0.3, imgh * 0.3))
            self.all_images.append(img)
            
        self.image = self.all_images[2]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        group.add(self)
        self.health = health
        self.bullet = bullet
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        