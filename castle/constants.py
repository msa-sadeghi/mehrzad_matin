import pygame
from pygame.locals import *

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background_image = pygame.image.load("assets/bg.png")
armour_image = pygame.image.load("assets/armour.png")
bullet_image = pygame.image.load("assets/bullet.png")
crosshair_image = pygame.image.load("assets/crosshair.png")
repair_image = pygame.image.load("assets/repair.png")
tower_25 = pygame.image.load("assets/tower/tower_25.png")
tower_50 = pygame.image.load("assets/tower/tower_50.png")
tower_100 = pygame.image.load("assets/tower/tower_100.png")
castle_25 = pygame.image.load("assets/castle/castle_25.png")
castle_50 = pygame.image.load("assets/castle/castle_50.png")
castle_100 = pygame.image.load("assets/castle/castle_100.png")