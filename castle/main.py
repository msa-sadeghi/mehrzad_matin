from constants import *
from world import World
from castle import Castle

bullet_group = pygame.sprite.Group()
game_world = World(background_image)
castle = Castle(castle_100, SCREEN_WIDTH - 250, SCREEN_HEIGHT - 300, 0.2)
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    game_world.draw()
    castle.shoot(bullet_group)
    castle.draw()
    bullet_group.update()
    bullet_group.draw(screen)
    pygame.display.update()
    clock.tick(FPS)