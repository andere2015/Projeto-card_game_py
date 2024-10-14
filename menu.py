import pygame
import sys
from constants import WHITE, BLACK

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect(center=(x, y))
    surface.blit(textobj, textrect)

def show_menu(screen):
    font = pygame.font.SysFont(None, 40)
    screen.fill(WHITE)
    draw_text('Cartas Massa', font, BLACK, screen, 364, 100)

    field_image = pygame.image.load('assets/banner.svg')
    field_image = pygame.transform.scale(field_image, (1000, 800))
    screen.blit(field_image, (0, 0))
    
    mx, my = pygame.mouse.get_pos()
    
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 315 <= mx <= 435 and 270 <= my <= 310:
                return False, True 
            if 328 <= mx <= 423 and 337 <= my <= 377:
                pygame.quit()
                sys.exit()
    
    return True, False
