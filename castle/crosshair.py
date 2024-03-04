import pygame
class CrossHair:
    def __init__(self, scale):
        image = pygame.image.load("assets/crosshair.png")
        w = image.get_width()
        h = image.get_height()
        
        self.image = pygame.transform.scale(image, (w * scale, h * scale))
        self.rect = self.image.get_rect()
        pygame.mouse.set_visible(False)
        
    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()
        self.rect.center = mouse_pos
        screen.blit(self.image, self.rect)
        