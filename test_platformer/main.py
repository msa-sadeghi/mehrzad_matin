import pygame
from constants import *
from world import World
from button import Button
import os
import pickle
pygame.init()

restart_button = Button(RESTART_IMAGE, SCREEN_WIDTH/2, SCREEN_HEIGHT/2)


clock = pygame.time.Clock()

pygame.mixer.music.load("assets/img/music.wav")

pygame.mixer.music.play(-1)

player_group = pygame.sprite.Group()  

level = 1


def change_level():
    enemy_group.empty()
    lava_group.empty()
    door_group.empty()
    player_group.empty()
    if os.path.exists(f"levels/level{level}"):
        f = open(f"levels/level{level}", "rb")
        world_data = pickle.load(f)
        game_world = World(world_data, player_group, enemy_group, lava_group,door_group)
    return game_world
    


enemy_group = pygame.sprite.Group()  
lava_group = pygame.sprite.Group()  
door_group = pygame.sprite.Group()  
if os.path.exists("levels/level1"):
    f = open("levels/level1", "rb")
    world_data = pickle.load(f)
    
game_world = World(world_data, player_group, enemy_group, lava_group,door_group)  

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    game_world.draw(screen)
    player_group.update(screen, game_world.tile_list, enemy_group, door_group)
    player_group.draw(screen) 
    door_group.draw(screen)  
    if player_group.sprites()[0].alive:
        enemy_group.update()
    elif not player_group.sprites()[0].alive:
        restart_button.draw()
        if restart_button.clicked:
            player_group.sprites()[0].alive = True
            player_group.sprites()[0].reset(100,600)
    if player_group.sprites()[0].next_level:
        print("next level")
    enemy_group.draw(screen)
    lava_group.draw(screen)
    pygame.display.update()
    clock.tick(FPS)
 

