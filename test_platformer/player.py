import pygame
from pygame.sprite import Sprite
from constants import *


class Player(Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.run_right_images = []
        self.run_left_images = []
        self.idle_right_images = []
        self.idle_left_images = []
        for i in range(1, 9):
            image = pygame.image.load(f"assets/boy/Run ({i}).png")
            image = pygame.transform.scale(image, (image.get_width() * 0.2, image.get_height() * 0.2))
            self.run_right_images.append(image)
            image = pygame.transform.flip(image, True, False)
            self.run_left_images.append(image)

        for i in range(1, 10):
            image = pygame.image.load(f"assets/boy/Idle ({i}).png")
            image = pygame.transform.scale(image, (image.get_width() * 0.2, image.get_height() * 0.2))
            self.idle_right_images.append(image)
            image = pygame.transform.flip(image, True, False)
            self.idle_left_images.append(image)
        self.jump_sound = pygame.mixer.Sound("assets/img/jump.wav")
        self.dead_image = pygame.image.load("assets/img/ghost.png")
        self.reset(x,y)

    
    def reset(self, x,y):
        self.vel_y = 0
        self.speed = 5
        self.jumped = False
        self.in_air = False
        self.direction = 1
        self.idle = True
        self.alive = True
        self.frame_index = 0
        self.counter = 0
        self.image = self.idle_right_images[self.frame_index]
        self.rect = self.image.get_rect(topleft=(x, y))
        self.next_level = False
        
    
    def update(self, screen, tiles, enemy_group, door_group):
        self.move(tiles, enemy_group,door_group)

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

    def move(self, tiles, enemy_group, door_group):

        dx = 0
        dy = 0
        if self.alive:
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
                self.jump_sound.play()
                self.vel_y = -15
                self.jumped = True
                self.in_air = True
            if not keys[pygame.K_SPACE]:
                self.jumped = False

            self.vel_y += 1
            if self.vel_y > 10:
                self.vel_y = 10
            if self.vel_y < -15:
                self.vel_y = -15

            dy += self.vel_y
            if self.direction == 1:
                rect = pygame.Rect(self.rect.x + 50, self.rect.y + 10, self.image.get_width() - 70,
                                   self.image.get_height() - 20)
            elif self.direction == -1:
                rect = pygame.Rect(self.rect.x + 20, self.rect.y + 10, self.image.get_width() - 70,
                                   self.image.get_height() - 20)
            # pygame.draw.rect(screen,(0,0,0), rect,4)
            for tile in tiles:

                if tile[1].colliderect(rect.x + dx, rect.y, self.image.get_width() - 70, self.image.get_height() - 20):
                    dx = 0

                if tile[1].colliderect(rect.x, rect.y + dy, self.image.get_width() - 70, self.image.get_height() - 20):

                    if self.vel_y < 0:
                        self.vel_y = 0
                        dy = tile[1].bottom - rect.top
                    else:
                        self.vel_y = 0
                        dy = tile[1].top - rect.bottom
                        self.in_air = False

            if pygame.sprite.spritecollide(self, enemy_group, False):
                self.alive = False

            if pygame.sprite.spritecollide(self, door_group, False):
                self.next_level = True

            self.rect.x += dx
            self.rect.y += dy
            self.animation()



        elif not self.alive:
            self.image = self.dead_image
            if self.rect.y > 200:
                self.rect.y -= 5
