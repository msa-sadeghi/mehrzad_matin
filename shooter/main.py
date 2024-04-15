import pygame
from soldier import Soldier
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 640
moving_left = False
moving_right = False
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
s1 = Soldier('player',200, 200, 3,1,10)
s2 = Soldier('enemy',400, 200, 3,1,5)
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
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moving_left = False
            if event.key == pygame.K_RIGHT:
                moving_right = False
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
    pygame.display.update()
    