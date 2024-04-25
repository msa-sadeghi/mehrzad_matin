import pygame
from soldier import Soldier
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 640
bullet_group = pygame.sprite.Group()
moving_left = False
moving_right = False
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
s1 = Soldier('player',200, 200, 3,1,10)
s2 = Soldier('enemy',400, 200, 3,1,5)
shoot = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moving_left = True
            if event.key == pygame.K_RIGHT:
                moving_right = True
            if event.key == pygame.K_SPACE:
                shoot = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moving_left = False
            if event.key == pygame.K_RIGHT:
                moving_right = False
            if event.key == pygame.K_SPACE:
                shoot = False
    if s1.alive:
        if shoot:
            s1.shoot(bullet_group)
        
        if moving_left or moving_right:
            s1.update_action(1)
        else:
            s1.update_action(0)
    screen.fill((0,0,0))           
    s1.draw(screen) 
    s1.update()  
    s1.move(moving_left, moving_right)    
    s2.draw(screen) 
    s1.update()     
    bullet_group.update(s1,s2,bullet_group) 
    bullet_group.draw(screen)
    pygame.display.update()
    