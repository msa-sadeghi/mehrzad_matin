import pygame
from soldier import Soldier
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 640

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
s1 = Soldier('player',200, 200, 3,1,10)
s2 = Soldier('enemy',400, 200, 3,1,5)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    s1.draw(screen) 
    s1.update()      
    s2.draw(screen) 
    s1.update()      
    pygame.display.update()
    