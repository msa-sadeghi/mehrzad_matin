from constants import *
from world import World
from castle import Castle
from enemy import Enemy
enemy_animations = []
enemy_types = ['knight']
enemy_health = [75]
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
enemy_1 = Enemy(enemy_health[0], enemy_animations[0], 100, SCREEN_HEIGHT - 100, 1)
enemy_group.add(enemy_1)



bullet_group = pygame.sprite.Group()
game_world = World(background_image)
castle = Castle(castle_100,castle_50, castle_25, SCREEN_WIDTH - 250, SCREEN_HEIGHT - 300, 0.2)
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    game_world.draw()
    castle.shoot(bullet_group)
    castle.draw()
    enemy_group.update(screen,castle, bullet_group)
    enemy_group.draw(screen)
    bullet_group.update()
    bullet_group.draw(screen)
    pygame.display.update()
    clock.tick(FPS)