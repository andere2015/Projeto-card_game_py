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

    field_image = pygame.image.load('assets/banner.png')
    field_image = pygame.transform.scale(field_image, (1427/2, 425/2))
    screen.blit(field_image, (0, 0))

    draw_text('Iniciar Jogo', font, BLACK, screen, 364, 225)
    draw_text('Sair', font, BLACK, screen, 364, 325)
    
    mx, my = pygame.mouse.get_pos()
    
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 264 <= mx <= 464 and 200 <= my <= 250:
                return False, True 
            if 264 <= mx <= 464 and 300 <= my <= 350:
                pygame.quit()
                sys.exit()
    
    return True, False
