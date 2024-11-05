
import pygame
import sys
import random
from constants import WHITE, GREEN, BLACK
from player import Player
from deck_builder import deck_builder
import sons

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect(center=(x, y))
    surface.blit(textobj, textrect)


def draw_button(surface, text, x, y, width, height, color, hover_color):
    mouse_pos = pygame.mouse.get_pos()
    button_rect = pygame.Rect(x, y, width, height)

    if button_rect.collidepoint(mouse_pos):
        pygame.draw.rect(surface, hover_color, button_rect)
    else:
        pygame.draw.rect(surface, color, button_rect)

    font = pygame.font.SysFont(None, 30)
    text_surf = font.render(text, True, BLACK)
    text_rect = text_surf.get_rect(center=(x + width // 2, y + height // 2))
    surface.blit(text_surf, text_rect)

    return button_rect

def move_back_to_front(grid, player_name):
    # Ajustando a chave para corresponder ao grid
    back_row_key = f'{player_name.lower().replace(" ", "_")}_back_row'
    front_row_key = f'{player_name.lower().replace(" ", "_")}_front_row'
    
    back_row = grid[back_row_key]
    front_row = grid[front_row_key]
    
    for i, back_card in enumerate(back_row):
        if back_card['occupied']:  # Verifica se a posição na back_row está ocupada
            front_card = front_row[i]  # Posição correspondente no front_row
            if not front_card['occupied']:  # Verifica se a posição correspondente no front_row está livre
                front_card['occupied'] = True
                front_card['card'] = back_card['card']  # Move a carta para o front_row
                back_card['occupied'] = False  # Limpa a posição da back_row
                back_card['card'] = None

def show_turn_message(screen, player_name):
    font = pygame.font.SysFont(None, 50)
    text = f"É a vez de {player_name} escolher!"
    text_surf = font.render(text, True, BLACK)
    text_rect = text_surf.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))

    # Desenha um retângulo branco cobrindo toda a tela
    screen.fill(WHITE)
    screen.blit(text_surf, text_rect)
    pygame.display.flip()  # Atualiza a tela

    # Espera 2 segundos
    pygame.time.wait(2000)

def start_game(screen):
    field_image = pygame.image.load('assets/tabuleiro.svg')
    field_image = pygame.transform.scale(field_image, (1000, 800))

    player1 = Player("player 1")
    player2 = Player("player 2")
    
    player1.deck = deck_builder(screen, player1)

    # Chama a função para mostrar a mensagem de turno antes do jogador 2
    show_turn_message(screen, player2.name)

    player2.deck = deck_builder(screen, player2)


    random.shuffle(player1.deck)
    random.shuffle(player2.deck)

    for i in range(0,5):
        player1.hand.append(player1.deck.pop(0))

    for i in range(0,5):
        player2.hand.append(player2.deck.pop(0))

    current_player = player1
    selected_card = None
    dragging = False
    turn_counter = 0  # Contador de turnos
    ctrlPass=0
    # Restante do código continua como está...


    # Definindo o grid com estados de ocupação e contadores de turnos
    grid = {
        'player_1_back_row': [{'pos': (347, 504, 80, 114), 'occupied': False, 'card': None, 'turn_counter': 0},
                              {'pos': (468, 504, 80, 114), 'occupied': False, 'card': None, 'turn_counter': 0},
                              {'pos': (593, 504, 80, 114), 'occupied': False, 'card': None, 'turn_counter': 0}],
        
        'player_1_front_row': [{'pos': (347, 376, 80, 114), 'occupied': False, 'card': None},
                               {'pos': (471, 376, 80, 114), 'occupied': False, 'card': None},
                               {'pos': (593, 376, 80, 114), 'occupied': False, 'card': None}],
        
        'player_2_front_row':  [{'pos': (347, 189, 80, 114), 'occupied': False, 'card': None, 'turn_counter': 0},
                                {'pos': (470, 189, 80, 114), 'occupied': False, 'card': None, 'turn_counter': 0},
                                {'pos': (593, 189, 80, 114), 'occupied': False, 'card': None, 'turn_counter': 0}],
        
        'player_2_back_row': [ {'pos': (347, 60, 80, 114), 'occupied': False, 'card': None},
                               {'pos': (470, 60, 80, 114), 'occupied': False, 'card': None},
                               {'pos': (593, 60, 80, 114), 'occupied': False, 'card': None}],
    }

    while True:
        screen.fill(WHITE)
        screen.blit(field_image, (0, 0))
        
        # Renderiza as cartas no campo
        for row_key in grid:
            for position in grid[row_key]:  
                if position['occupied']:
                    card_image = pygame.image.load(position['card'].img)
                    card_image = pygame.transform.scale(card_image, (position['pos'][2], position['pos'][3]))
                    screen.blit(card_image, (position['pos'][0], position['pos'][1]))

        # Renderiza as cartas na mão do jogador atual
        for i, card in enumerate(current_player.hand):
            x, y, width, height = 230 + i * 95, 656, 81, 117
            card_image = pygame.image.load(card.img)
            card_image = pygame.transform.scale(card_image, (width, height))
            screen.blit(card_image, (x, y))

        # Botão de passar turno
        pass_button = draw_button(screen, 'Passar vez', 10, 300, 120, 50, (0,0,255), GREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Início de arrasto da carta
            if event.type == pygame.MOUSEBUTTONDOWN and not dragging:
                mx, my = pygame.mouse.get_pos()
                for i, card in enumerate(current_player.hand):
                    x, y, width, height = 230 + i * 95, 656, 81, 117
                    if x <= mx <= x + width and y <= my <= y + height:
                        selected_card = card
                        dragging = True
                        break

            # Soltando a carta no campo (somente na back row)
            if event.type == pygame.MOUSEBUTTONUP and dragging:  
                mx, my = pygame.mouse.get_pos()
                for row_key in [f'{current_player.name.lower().replace(" ", "_")}_back_row']:
                    for position in grid[row_key]:
                        x, y, width, height = position['pos']
                        if x <= mx <= x + width and y <= my <= y + height and not position['occupied']:
                            current_player.hand.remove(selected_card)
                            position['occupied'] = True
                            position['card'] = selected_card
                            position['turn_counter'] = 0  # Reseta o contador de turnos ao colocar a carta
                            
                            sons.tocar_musica_carta()
                            break
                dragging = False
                selected_card = None

            # Clique no botão "Passar Turno"
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                if pass_button.collidepoint(pygame.mouse.get_pos()):
                    sons.tocar_musica_turno()
                    turn_counter += 1  # Incrementa o contador de turnos
                    ctrlPass+=1

                    if(len(player1.hand)<6 and len(player1.deck) > 0 and ctrlPass%2 == 0):
                        player1.hand.append(player1.deck.pop(0))
                    if(len(player2.hand)<6 and len(player2.deck) > 0 and ctrlPass%2 != 0 and ctrlPass !=1):
                        player2.hand.append(player2.deck.pop(0))

                    if turn_counter == 1:  # Quando o jogador clicou uma vez
                        # Move cartas do back row do jogador adversário para a frente, se houver
                        if current_player == player1:
                            move_back_to_front(grid, player2.name)  # Move cartas do player 2
                        else:
                            move_back_to_front(grid, player1.name)  # Move cartas do player 1
                    # Trocar o turno
                    current_player = player2 if current_player == player1 else player1
                    turn_counter = 0  # Reinicia o contador geral

        # Se houver uma carta selecionada, segue o mouse enquanto é arrastada
        if dragging and selected_card:
            mx, my = pygame.mouse.get_pos()
            card_image = pygame.image.load(selected_card.img)
            card_image = pygame.transform.scale(card_image, (50, 75))
            screen.blit(card_image, (mx - 25, my - 37))

        pygame.display.flip()
