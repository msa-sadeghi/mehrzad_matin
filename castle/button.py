import pygame

class Button:
    def __init__(self, x, y, image, scale):
        w = image.get_width()
        h = image.get_height()
        self.image = pygame.transform.scale(image, (w * scale, h * scale))
        self.rect = self.image.get_rect(topleft = (x,y))
        
        self.clicked = False
        
    def draw(self, screen):
        action = False
        mouse_position = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_position):
            if pygame.mouse.get_pressed()[0] and not self.clicked:
                self.clicked = True
                action = True
                
        if not pygame.mouse.get_pressed()[0]:
            self.clicked = False
        screen.blit(self.image, self.rect)
        return action