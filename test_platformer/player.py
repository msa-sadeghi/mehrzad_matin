import pygame
from pygame.sprite import Sprite
from constants import *
class Player(Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.run_right_images = []
        self.run_left_images = []
        self.idle_right_images = []
        self.idle_left_images = []
        for i in range(1,9):
            image = pygame.image.load(f"assets/boy/Run ({i}).png")
            image = pygame.transform.scale(image,(image.get_width()* 0.2,image.get_height()* 0.2))
            self.run_right_images.append(image)
            image = pygame.transform.flip(image, True, False)
            self.run_left_images.append(image)

        for i in range(1, 10):
            image = pygame.image.load(f"assets/boy/Idle ({i}).png")
            image = pygame.transform.scale(image, (image.get_width() * 0.2, image.get_height() * 0.2))
            self.idle_right_images.append(image)
            image = pygame.transform.flip(image, True, False)
            self.idle_left_images.append(image)

        self.frame_index = 0
        self.counter = 0
        self.image = self.idle_right_images[self.frame_index]
        self.rect = self.image.get_rect(topleft = (x,y))
        self.vel_y = 0
        self.speed = 5
        self.jumped = False
        self.in_air = False
        self.direction = 1
        self.idle = True

    def update(self,screen, tiles):
        self.move(tiles)
        self.animation()
  
        pygame.draw.rect(screen, (10,230,210), self.rect,4)

  

        

    
    
    
    def animation(self):
        self.counter += 1
        if self.counter > 2:
            self.frame_index += 1
            self.counter = 0
        if self.frame_index >= len(self.run_right_images) - 1:
            self.frame_index = 0
        if not self.idle:
            if self.direction == 1:
                self.image = self.run_right_images[self.frame_index]
            if self.direction == -1:
                self.image = self.run_left_images[self.frame_index]
        else:
            if self.direction == 1:
                self.image = self.idle_right_images[self.frame_index]
            if self.direction == -1:
                self.image = self.idle_left_images[self.frame_index]




    
    def move(self, tiles):
        dx = 0
        dy = 0

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.idle = False
            dx -= self.speed
            self.direction = -1
        if keys[pygame.K_RIGHT]:
            self.idle = False
            dx += self.speed
            self.direction = 1


        if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
            self.idle = True

        if keys[pygame.K_SPACE] and not self.jumped and not self.in_air:
            self.vel_y = -10
            self.jumped = True
            self.in_air = True
        if not keys[pygame.K_SPACE]:
            self.jumped = False

        self.vel_y += 1
        dy += self.vel_y
        
        for tile in tiles:

            # if tile[1].colliderect(self.rect.x + dx, self.rect.y , self.image.get_width(), self.image.get_height()):
            #     dx = 0

            if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.image.get_width(), self.image.get_height()):
            
                print("self.inair", self.in_air)
                self.vel_y = 0
                dy = tile[1].top - self.rect.bottom
                self.in_air = False
            
        
        
        self.rect.x += dx
        self.rect.y += dy
        # if self.rect.bottom > SCREEN_HEIGHT:
        #     self.rect.bottom = SCREEN_HEIGHT
            # self.in_air = False



