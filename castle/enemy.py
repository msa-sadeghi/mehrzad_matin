from pygame.sprite import Sprite
import pygame
class Enemy(Sprite):
    def __init__(self, health, animation_list, x,y, speed):
        super().__init__()
        self.alive = True
        self.speed = speed
        self.health = health
        self.frame_index = 0
        self.action = 0
        self.animation_list = animation_list
        
        
        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect(center=(x,y))
        self.update_time = pygame.time.get_ticks()
        
    def update(self,screen,target, bullet_group):
        if self.alive:
            if pygame.sprite.spritecollide(self, bullet_group, True):
                self.health -= 25

            if self.rect.right > target.rect.left:
                self.update_action(1)
            
            if self.action == 0:
                self.rect.x += self.speed
                
        self.update_animation()
        screen.blit(self.image, self.rect)
        
    def update_animation(self): 
        self.image = self.animation_list[self.action][self.frame_index] 
        if pygame.time.get_ticks() - self.update_time > 80:
            self.frame_index += 1
            self.update_time = pygame.time.get_ticks()
        if self.frame_index >= 20:
            self.frame_index = 0
            
    def update_action(self, new_action):
        if new_action != self.action:
            self.action = new_action
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()
        
        