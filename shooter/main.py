import pygame
from soldier import Soldier
from grenade import Grenade
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 640
clock = pygame.time.Clock()
bullet_group = pygame.sprite.Group()
grenade_group = pygame.sprite.Group()
moving_left = False
moving_right = False
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
s1 = Soldier('player',200, 200, 3,1,10,10)
s2 = Soldier('enemy',400, 200, 3,1,5,0)
shoot = False
grenade = False
grenade_thrown = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_LEFT:
                moving_left = True
            if event.key == pygame.K_RIGHT:
                moving_right = True
            if event.key == pygame.K_SPACE:
                shoot = True
            if event.key == pygame.K_UP:
                s1.jump = True
            if event.key == pygame.K_g:
                grenade = True
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moving_left = False
            if event.key == pygame.K_RIGHT:
                moving_right = False
            if event.key == pygame.K_SPACE:
                shoot = False
            if event.key == pygame.K_UP:
                s1.jump = False
            if event.key == pygame.K_g:
                grenade = False
                grenade_thrown = False
    if s1.alive:
        if shoot:
            s1.shoot(bullet_group)  
        elif grenade and not grenade_thrown and s1.grenade > 0:
            grenade = Grenade(s1.rect.centerx + s1.rect.size[0] * s1.direction, s1.rect.top, s1.direction)
            grenade_group.add(grenade)
            grenade_thrown = True
            s1.grenade -= 1
        if s1.in_air:
            s1.update_action(2)  
        elif moving_left and moving_right:
            s1.update_action(0)
        elif moving_left or moving_right:
            s1.update_action(1)
        else:
            s1.update_action(0)
    screen.fill((0,0,0))  
    
    print(s2.health)
    
             
    s1.draw(screen) 
    s1.update()  
    s1.move(moving_left, moving_right)  
    s2.update()  
    s2.draw(screen) 
    bullet_group.update(s1,s2,bullet_group) 
    bullet_group.draw(screen)
    grenade_group.update()
    grenade_group.draw(screen)
    pygame.display.update()
    clock.tick(60)
    