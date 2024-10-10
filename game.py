import pygame
import sys
import random
from constants import WHITE, GREEN, BLACK
from player import Player
from deck_builder import deck_builder

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect(center=(x, y))
    surface.blit(textobj, textrect)
def draw_button(surface, text, x, y, width, height, color, hover_color):
    mouse_pos = pygame.mouse.get_pos()  # Obtém a posição do mouse
    button_rect = pygame.Rect(x, y, width, height)  # Define a área do botão

    # Verifica se o mouse está sobre o botão (hover)
    if button_rect.collidepoint(mouse_pos):
        pygame.draw.rect(surface, hover_color, button_rect)  # Muda a cor para hover_color
    else:
        pygame.draw.rect(surface, color, button_rect)  # Desenha o botão com a cor normal

    # Desenha o texto do botão
    font = pygame.font.SysFont(None, 30)
    text_surf = font.render(text, True, BLACK)
    text_rect = text_surf.get_rect(center=(x + width // 2, y + height // 2))
    surface.blit(text_surf, text_rect)

    return button_rect  # Retorna o retângulo do botão para verificar cliques

def start_game(screen):
    field_image = pygame.image.load('image.png')
    field_image = pygame.transform.scale(field_image, (729, 625))

    player1 = Player("jogador 1")
    player2 = Player("jogador 2")


    player1.deck = deck_builder(screen, player1)
    player2.deck = deck_builder(screen, player2)
    player1.hand = random.sample(player1.deck, 5)
    player2.hand = random.sample(player2.deck, 5)

    current_player = player1  # Jogador 1 começa o turno
    selected_card = None  # Armazena a carta sendo arrastada
    dragging = False  # Flag para arrastar a carta
    grid = {
    'jogador_1_back_row': [(269, 417, 50, 75), (353, 417, 50, 75), (438, 417, 50, 75)],
    'jogador_1_front_row': [(269, 330, 50, 75), (353, 330, 50, 75), (438, 330, 50, 75)],
    'jogador_2_front_row': [(268, 202, 50, 75), (353, 202, 50, 75), (439, 202, 50, 75)],
    'jogador_2_back_row': [(266, 115, 50, 75), (351, 115, 50, 75), (436, 115, 50, 75)],
    'jogador_1_hand': [(201, 520, 45, 70), (260, 520, 45, 70), (324, 520, 45, 70), (389, 520, 45, 70), (449, 520, 45, 70), (504, 520, 45, 70)],
    'jogador_2_hand': [(204, 20, 45, 70), (263, 20, 45, 70), (327, 20, 45, 70), (392, 20, 45, 70), (452, 20, 45, 70), (507, 20, 45, 70)]
    }


    while True:
        screen.fill(WHITE)
        screen.blit(field_image, (0, 0))

        # Renderiza as cartas na mão do jogador atual
        if current_player == player1:
            for i, card in enumerate(player1.hand):
                x, y, width, height = grid['jogador_1_hand'][i]
                card_image = pygame.image.load(card.asset)
                card_image = pygame.transform.scale(card_image, (width, height))
                screen.blit(card_image, (x, y))
        else:
            for i, card in enumerate(player2.hand):
                x, y, width, height = grid['jogador_2_hand'][i]
                card_image = pygame.image.load(card.asset)
                card_image = pygame.transform.scale(card_image, (width, height))
                screen.blit(card_image, (x, y))

        # Desenha os retângulos da grid do campo
        
        # Botão de passar turno
        pass_button = draw_button(screen, 'Passar Turno', 700, 650, 150, 50, BLACK, GREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Início de arrasto da carta
            if event.type == pygame.MOUSEBUTTONDOWN and not dragging:
                mx, my = pygame.mouse.get_pos()
                for i, card in enumerate(current_player.hand):
                    x, y, width, height = grid[f'{current_player.name.lower().replace(" ", "_")}_hand'][i]
                    if x <= mx <= x + width and y <= my <= y + height:
                        selected_card = card
                        dragging = True
                        break

            # Soltando a carta na back row
            if event.type == pygame.MOUSEBUTTONUP and dragging:
                mx, my = pygame.mouse.get_pos()
                for i, position in enumerate(grid[f'{current_player.name.lower().replace(" ", "_")}_back_row']):
                    x, y, width, height = position
                    if x <= mx <= x + width and y <= my <= y + height:
                        current_player.hand.remove(selected_card)
                        # Adicionar a carta na posição correspondente (a lógica do tabuleiro pode ser mais detalhada)
                        break
                dragging = False
                selected_card = None

            # Clique no botão "Passar Turno"
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pass_button.collidepoint(pygame.mouse.get_pos()):
                    current_player = player2 if current_player == player1 else player1

        # Se houver uma carta selecionada, segue o mouse enquanto é arrastada
        if dragging and selected_card:
            mx, my = pygame.mouse.get_pos()
            card_image = pygame.image.load(selected_card.asset)
            card_image = pygame.transform.scale(card_image, (50, 75))
            screen.blit(card_image, (mx - 25, my - 37))

        pygame.display.flip()