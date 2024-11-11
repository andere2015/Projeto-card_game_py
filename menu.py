import pygame
import sys
from constants import WHITE, BLACK
import sons 

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect(center=(x, y))
    surface.blit(textobj, textrect)

def show_menu(screen):
    # Configuração da fonte e carregamento da música do menu
    font = pygame.font.SysFont(None, 40)
    sons.tocar_musica_menu()

    running = True
    while running:
        screen.fill(WHITE)
        draw_text('Cartas Massa', font, BLACK, screen, 364, 100)

        # Carregar e desenhar a imagem do menu
        field_image = pygame.image.load('assets/banner.svg')
        field_image = pygame.transform.scale(field_image, (1000, 800))
        screen.blit(field_image, (0, 0))
        
        # Capturar a posição do mouse
        mx, my = pygame.mouse.get_pos()

        # Processamento de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Verificar cliques nos botões
                if 440 <= mx <= 567 and 331 <= my <= 369:
                    sons.parar_musica()
                    sons.tocar_musica_jogo()
                    return False, True  # Fechar o menu e iniciar o jogo
                if 453 <= mx <= 548 and 395 <= my <= 433:
                    pygame.quit()
                    sys.exit()  # Sair do jogo

        # Atualizar a tela a cada quadro
        pygame.display.update()

    return True, False
