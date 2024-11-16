import sys
import pygame
import copy
from constants import WHITE, BLACK, GREEN
from cartas import cartas_existentes

# Configurações iniciais do Pygame
pygame.init()

# Função para exibir texto com quebra automática de linha
def draw_text_wrapped(text, font, color, surface, x, y, max_width):
    words = text.split(' ')
    lines = []
    current_line = words[0]

    # Quebra o texto em linhas de acordo com o tamanho máximo permitido
    for word in words[1:]:
        test_line = current_line + ' ' + word
        if font.size(test_line)[0] < max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word
    lines.append(current_line)

    for i, line in enumerate(lines):
        line_surface = font.render(line, True, color)
        surface.blit(line_surface, (x, y + i * font.get_height()))

# Pré-carregar e redimensionar as imagens fora do loop
def load_and_scale_image(path, size):
    image = pygame.image.load(path)
    return pygame.transform.smoothscale(image, size)

def draw_card_options(screen, cards, selected_cards, scroll_offset):
    font = pygame.font.SysFont(None, 20)
    quantity_font = pygame.font.SysFont(None, 25)

    # Carregar e redimensionar todas as imagens antes do loop
    card_images = {card: load_and_scale_image(card.img, (100, 150)) for card in cards}
    
    # Ajusta a posição das cartas com base no scroll
    for i, card in enumerate(cards):
        x = 50 + (i % 5) * 120
        y = 150 + (i // 5) * 200 + scroll_offset  # Aplicando o scroll_offset para rolagem
        screen.blit(card_images[card], (x, y))  # Usa a imagem redimensionada

        if selected_cards.get(card, 0) > 0:
            pygame.draw.rect(screen, GREEN, (x - 5, y - 5, 110, 160), 3)

        card_count = selected_cards.get(card, 0)
        draw_text_wrapped(f'x{card_count}', quantity_font, BLACK, screen, x + 85, y + 140, 100)
        draw_text_wrapped(card.tipo, font, BLACK, screen, x + 50, y + 160, 100)


# Função para desenhar o modal com a imagem e informações da carta
def draw_modal(screen, card):
    modal_surface = pygame.Surface((345, 600))  # Modal com 345x600
    modal_surface.fill(WHITE)
    pygame.draw.rect(modal_surface, BLACK, modal_surface.get_rect(), 2)
    font = pygame.font.SysFont(None, 30)
    
    # Pré-carrega e redimensiona a imagem da carta
    card_image = load_and_scale_image(card.img, (150, 225))  # Define o tamanho da imagem no modal
    
    # Exibe a imagem da carta no topo do modal
    modal_surface.blit(card_image, (97, 20))

    # Exibe informações da carta abaixo da imagem
    draw_text_wrapped(card.nome, font, BLACK, modal_surface, 10, 260, 325)
    draw_text_wrapped(f"Vida: {card.vida} | Ataque: {card.ataque}", font, BLACK, modal_surface, 10, 300, 325)
    draw_text_wrapped(card.descricao, font, BLACK, modal_surface, 10, 340, 325)
    
    # Posição do modal na tela principal
    screen.blit(modal_surface, (640, 100))
    
# Função para construir o deck com rolagem
def deck_builder(screen, player):
    
    font = pygame.font.SysFont(None, 30)
    selected_cards = {}
    available_cards = cartas_existentes
    modal_card = None  # Variável para armazenar a carta que será exibida no modal
    scroll_offset = 10  # Offset para controlar a rolagem

    while sum(selected_cards.values()) < 10:
        screen.fill(WHITE)
        draw_text_wrapped(f'{player.name}, escolha suas cartas ({sum(selected_cards.values())}/20)', font, BLACK, screen, 640, 50, 500)

        # Desenha as cartas com o offset de rolagem
        draw_card_options(screen, available_cards, selected_cards, scroll_offset)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()

                # Controle do scroll
                if event.button == 4:  # Rolagem para cima
                    scroll_offset = min(scroll_offset + 20, 0)  # Aumenta o valor para rolagem mais rápida
                elif event.button == 5:  # Rolagem para baixo
                    scroll_offset -= 40  # Aumenta o valor para rolagem mais rápida

                # Clique com o botão direito (abre o modal)
                if event.button == 3:  # Botão direito do mouse
                    for i, card in enumerate(available_cards):
                        x = 50 + (i % 5) * 120
                        y = 150 + (i // 5) * 200 + scroll_offset
                        if x <= mx <= x + 100 and y <= my <= y + 150:
                            modal_card = card  # Armazena a carta que será exibida no modal
                            break

                # Clique com o botão esquerdo (seleciona a carta)
                elif event.button == 1:  
                    for i, card in enumerate(available_cards):
                        x = 50 + (i % 5) * 120
                        y = 150 + (i // 5) * 200 + scroll_offset
                        if x <= mx <= x + 100 and y <= my <= y + 150:
                            current_count = selected_cards.get(card, 0)
                            if current_count < 3:
                                selected_cards[card] = current_count + 1
                            elif current_count == 3:
                                selected_cards[card] = 0
                            if selected_cards[card] == 0:
                                del selected_cards[card]
                            modal_card = None  # Fecha o modal ao selecionar
                            break

        # Se houver uma carta selecionada para o modal, desenha o modal
        if modal_card:
            draw_modal(screen, modal_card)

        pygame.display.flip()

    player.deck = [copy.deepcopy(card) for card, count in selected_cards.items() for _ in range(count)]
    return player.deck
