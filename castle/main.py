import random
from constants import *
from world import World
from castle import Castle
from enemy import Enemy
from crosshair import CrossHair
from button import Button
from tower import Tower
pygame.init()
enemy_animations = []
enemy_types = ['knight', 'goblin', 'purple_goblin', 'red_goblin']
enemy_health = [25, 25,25,25 ]
animation_types = ["walk", "attack", "death"]
for enemy in enemy_types:
    animation_list = []
    for animation in animation_types:
        temp_list = []
        for i in range(20):
            img = pygame.image.load(f"assets/enemies/{enemy}/{animation}/{i}.png")
            w = img.get_width()
            h = img.get_height()
            img = pygame.transform.scale(img, (w * 0.3, h * 0.3))
            temp_list.append(img)
        animation_list.append(temp_list)
    enemy_animations.append(animation_list)
    
    
enemy_group = pygame.sprite.Group()  

level = 1
level_difficulty = 0
target_difficulty = 100
ENEMY_TIMER = 1000
last_enemy_time = pygame.time.get_ticks()
level_reset_time = pygame.time.get_ticks()
enemies_alive = 0
next_level = False

bullet_group = pygame.sprite.Group()
game_world = World(background_image)
castle = Castle(castle_100,castle_50, castle_25, SCREEN_WIDTH - 250, SCREEN_HEIGHT - 300, 0.2)
clock = pygame.time.Clock()

crosshair = CrossHair(0.06)

repair_button = Button(SCREEN_WIDTH - 100, 30, repair_image, 0.5 )
tower_button = Button(SCREEN_WIDTH - 40, 30, tower_100, 0.1)

def draw_text(text,x,y, size, color, is_center):
    f = pygame.font.SysFont("arial", size)
    t = f.render(text, True, color)
    if is_center:
        r = t.get_rect(center = (x,y))
    else:
        r = t.get_rect(topleft = (x,y))
        
    
    screen.blit(t,r)

def game_over():
    global running, level_difficulty, target_difficulty
    game_world.draw()
    draw_text("Game Over Press Enter To Continue...", SCREEN_WIDTH/2 , SCREEN_HEIGHT/2,
              36, (194, 17, 89), True)
    pygame.display.update()
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                paused = False
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    paused = False
                    castle.score = 0
                    castle.health = 1000
                    castle.max_health = 1000
                    castle.money = 0
                    level_difficulty = 0
                    target_difficulty = 1000
                    enemy_group.empty()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    game_world.draw()
    repair_button.draw(screen)
    tower_button.draw(screen)
    draw_text(f"Score: {castle.score}", 70, 10, 22, (255,10,190), False)
    draw_text(f"Money: {castle.money}", 70, 40, 22, (255,190,10), False)
    draw_text(f"Lives: {castle.health}", 290, 10, 22, (205,10,10), False)
    draw_text(f"Max Health: {castle.max_health}", 290, 40, 22, (215,111,210), False)
    crosshair.draw(screen)
    castle.shoot(bullet_group)
    castle.draw()
    enemy_group.update(screen,castle, bullet_group)
    enemy_group.draw(screen)
    
    if level_difficulty < target_difficulty:
        if pygame.time.get_ticks() - last_enemy_time > 2000:
            last_enemy_time = pygame.time.get_ticks()
            h = random.randint(0, len(enemy_types)-1)
            enemy =Enemy(enemy_health[h], enemy_animations[h], -100, SCREEN_HEIGHT - 100, 1)
            enemy_group.add(enemy)
            level_difficulty += enemy_health[h]
            
    if level_difficulty >= target_difficulty:
        enemies_alive = 0
        for enemy in enemy_group:
            if enemy.alive:
                enemies_alive += 1
        if enemies_alive == 0 and next_level == False:
            next_level = True
            level_reset_time = pygame.time.get_ticks()
    if next_level:
        draw_text(f"LEVEL {level} COMPLETED", SCREEN_WIDTH/2, SCREEN_HEIGHT/2, 48, (255,10,10), True)
        if pygame.time.get_ticks() - level_reset_time > 1500:
            next_level = False
            level += 1
            target_difficulty *= 1.1 
            level_difficulty = 0
            enemy_group.empty()       
        
    if castle.health <= 0:
        game_over()
    
    bullet_group.update()
    bullet_group.draw(screen)
    pygame.display.update()
    clock.tick(FPS)