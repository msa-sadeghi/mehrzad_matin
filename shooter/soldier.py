from pygame.sprite import Sprite
import pygame
import os
from bullet import Bullet
class Soldier(Sprite):
    def __init__(self,char_type, x,y, scale, speed, ammo, grenade):
        super().__init__()
        
        self.direction = 1
        self.char_type = char_type
        self.speed = speed
        self.flip = False
        self.ammo = ammo
        self.grenade = grenade
        self.stat_ammo = ammo
        self.alive = True
        self.health = 100
        self.max_health = self.health
        self.direction = 1
        self.vel_y = 0
        self.jump = False
      
        self.in_air = False
       
        self.animation_list = []
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()
        animation_types = ("Idle", "Run", "Jump", "Death")
        for animation in animation_types:
            temp_list = []
            n = len(os.listdir(f"assets/images/{self.char_type}/{animation}"))
            for i in range(n):
                img = pygame.image.load(f"assets/images/{self.char_type}/{animation}/{i}.png")
                img_w = img.get_width()
                img_h = img.get_height()
                img = pygame.transform.scale(img, (img_w * 3, img_h * 3))
                temp_list.append(img)
            self.animation_list.append(temp_list)
        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect(center=(x,y))
        self.last_anim_update = pygame.time.get_ticks()
        self.shoot_cooldown = 20
        
    def update(self)    :
        self.update_animation()
        self.check_alive()
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1
    def check_alive(self)   :
        pass
    def update_animation(self):
        self.image = self.animation_list[self.action][self.frame_index]
        if pygame.time.get_ticks() - self.last_anim_update > 100:
            self.last_anim_update = pygame.time.get_ticks()
            self.frame_index += 1
            if self.frame_index >= len(self.animation_list[self.action]):
                self.frame_index = 0
    def update_action(self, action):
        if action != self.action:
            self.action = action
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()
    def shoot(self, bullet_group):
        if self.ammo > 0 and self.shoot_cooldown == 0:
            self.shoot_cooldown = 20
            bullet = Bullet(self.rect.centerx + self.direction *  0.6 *self.rect.size[0], self.rect.centery, self.direction)
            bullet_group.add(bullet)
            self.ammo -= 1
            
        
        
    def draw(self,screen):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)
        
    def move(self, moving_left, moving_right):
        dx = 0
        dy = 0 
        if moving_left:
            dx -= self.speed
            self.direction = -1
            self.flip = True
        if moving_right:
            dx += self.speed
            self.direction = 1
            self.flip = False
        
        if self.jump and not self.in_air:
            self.vel_y = -13
            self.jump = False
            self.in_air = True
        dy += self.vel_y
        self.vel_y += 1
        
        if self.rect.bottom + dy > 300:
            dy = 300 - self.rect.bottom
            self.in_air = False
        
        self.rect.x += dx
        self.rect.y += dy
        
        
    
    
    
   