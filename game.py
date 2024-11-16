
import pygame
import sys
import random
from constants import WHITE, GREEN, BLACK, RED
from player import Player
from deck_builder import deck_builder
import sons
import time


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

def draw_player_life(screen, player1, player2):
    
    circuloVida = pygame.image.load("assets/circuloVida.svg")
    circuloVida = pygame.transform.scale(circuloVida, (82, 82))
    

    circuloVida = pygame.image.load("assets/circuloVida.svg")
    circuloVida.blit
    full_life_color = GREEN  # Cor da vida cheia
    empty_life_color = RED  # Cor da vida vazia
    bar_width, bar_height = 60, 60  # Tamanho da barra de vida


    player1_life_ratio = player1.life / 20  # Proporção da vida atual sobre o máximo
    player1_life_width = int(bar_width * player1_life_ratio)  # Largura proporcional ao valor de vida atual
    pygame.draw.rect(screen, empty_life_color, (110,701, bar_width, bar_height))  # Barra vazia
    pygame.draw.rect(screen, full_life_color, (110,701, player1_life_width, bar_height))  # Vida atual

    # Desenhar barra de vida para o jogador 2
    player2_life_ratio = player2.life / 20
    player2_life_width = int(bar_width * player2_life_ratio)
    pygame.draw.rect(screen, empty_life_color, (830,694, bar_width, bar_height))  # Barra vazia
    pygame.draw.rect(screen, full_life_color, (830,694, player2_life_width, bar_height))  # Vida atual
    font = pygame.font.SysFont(None, 30)

    player1_text = font.render(f"{player1.life}", True, BLACK)
    player2_text = font.render(f"{player2.life}", True, BLACK)

    
    player1_text_rect = player1_text.get_rect(center=(142, 733))
    player2_text_rect = player2_text.get_rect(center=(861, 725))

    
    screen.blit(player1_text, player1_text_rect)
    screen.blit(player2_text, player2_text_rect)
    screen.blit(circuloVida, (101, 692))
    screen.blit(circuloVida, (820, 684))



def show_end_screen(screen, winner_name):
    sons.tocar_musica_vitoria()
  # Tela de finalização com mensagem do vencedor
    field_image = pygame.image.load('assets/TELA_FINAL.svg')
    field_image = pygame.transform.scale(field_image, (1000, 800))
    screen.blit(field_image, (0, 0))

    font = pygame.font.SysFont(None, 50)
    text = f"{winner_name} venceu!"
    draw_text(text, font, BLACK, screen, screen.get_width() // 2, screen.get_height() // 2 - 50)

    # Botões centralizados
    replay_button = draw_button(screen, 'Jogar Novamente',  screen.get_width() // 2 - 100, 400, 200, 50, WHITE, (0, 255, 0))
    quit_button = draw_button(screen, 'Sair',  screen.get_width() // 2 - 40, 460, 80, 50, WHITE, (200, 0, 0))

    pygame.display.flip()

    # Loop da tela de fim
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if replay_button.collidepoint(event.pos):
                    start_game(screen)  # Reinicia o jogo
                    return
                elif quit_button.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

def move_back_to_front(grid, player_name):
    # Ajustando a chave para corresponder ao grid
    back_row_key = f'{player_name.lower().replace(" ", "_")}_back_row'
    front_row_key = f'{player_name.lower().replace(" ", "_")}_front_row'
    
    back_row = grid[back_row_key]
    front_row = grid[front_row_key]
    
    for i, back_card in enumerate(back_row):
        if back_card is not None and back_card['occupied'] and back_card['card'].tipo != "equipamento" : 
            front_card = front_row[i]  
            if not front_card['occupied']: 
                front_card['occupied'] = True
                front_card['card'] = back_card['card'] 
                back_card['occupied'] = False  
                back_card['card'] = None

def show_turn_message(screen, player_name):
    font = pygame.font.SysFont(None, 50)
    text = f"É a vez de {player_name} escolher!"
    text_surf = font.render(text, True, BLACK)
    text_rect = text_surf.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
    screen.fill(WHITE)
    screen.blit(text_surf, text_rect)
    pygame.display.flip()  # Atualiza a tela
    pygame.time.wait(1500)

def draw_damage_animation(card):
    from main import screen
    pygame.draw.rect(screen, (255,0,0), card['pos'], width=0, border_radius=10)
    pygame.display.flip()
    pygame.time.wait(30)
    

def show_atributes(screen,card):
    font = pygame.font.SysFont(None, 25)

    text_life = font.render(f"{card['card'].vida}", True, BLACK)
    text_attack = font.render(f"{card['card'].ataque}", True, BLACK)
    
    attack_pos = (card['pos'][0]+15,card['pos'][1]+card['pos'][3]-30)
    life_pos = (card['pos'][0]+card['pos'][2]-15,card['pos'][1]+card['pos'][3]-30)
    
    screen.blit(text_life, life_pos)
    screen.blit(text_attack, attack_pos)

def start_game(screen):
    sons.tocar_musica_jogo()
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

    for i in range(0,3):
        player1.hand.append(player1.deck.pop(0))

    for i in range(0,3):
        player2.hand.append(player2.deck.pop(0))

    current_player = player1
    selected_card = None
    dragging = False
    turn_counter = 0  # Contador de turnos
    ctrlPass=0
    # Restante do código continua como está...


    # Definindo o grid com estados de ocupação e contadores de turnos
    grid = {
        'player_1_back_row': [{'pos': [347, 504, 80, 114], 'occupied': False, 'card': None, 'turn_counter': 0},
                              {'pos': [468, 504, 80, 114], 'occupied': False, 'card': None, 'turn_counter': 0},
                              {'pos': [593, 504, 80, 114], 'occupied': False, 'card': None, 'turn_counter': 0}],
        
        'player_1_front_row': [{'pos': [347, 376, 80, 114], 'occupied': False, 'card': None},
                               {'pos': [471, 376, 80, 114], 'occupied': False, 'card': None},
                               {'pos': [593, 376, 80, 114], 'occupied': False, 'card': None}],
        
        'player_2_front_row':  [{'pos': [347, 189, 80, 114], 'occupied': False, 'card': None, 'turn_counter': 0},
                                {'pos': [470, 189, 80, 114], 'occupied': False, 'card': None, 'turn_counter': 0},
                                {'pos': [593, 189, 80, 114], 'occupied': False, 'card': None, 'turn_counter': 0}],
        
        'player_2_back_row': [ {'pos': [347, 60, 80, 114], 'occupied': False, 'card': None},
                               {'pos': [470, 60, 80, 114], 'occupied': False, 'card': None},
                               {'pos': [593, 60, 80, 114], 'occupied': False, 'card': None}],
    }

    while True:
        screen.fill(WHITE)
        screen.blit(field_image, (0, 0))
        draw_player_life(screen, player1, player2)
        
        for row_key in grid:
            for position in grid[row_key]:  
                if position['occupied']:
                    card_image = pygame.image.load(position['card'].img)
                    card_image = pygame.transform.scale(card_image, (position['pos'][2], position['pos'][3]))
                    screen.blit(card_image, (position['pos'][0], position['pos'][1]))

        for row_key, row_positions in grid.items():
            for position in row_positions:
                if position['occupied']:
                    show_atributes(screen,position)

        for i, card in enumerate(current_player.hand):
            x, y, width, height = 230 + i * 95, 656, 81, 117
            card_image = pygame.image.load(card.img)
            card_image = pygame.transform.scale(card_image, (width, height))
            screen.blit(card_image, (x, y))

        # Botão de passar turno
        pass_button = draw_button(screen, 'Passar vez', 10, 300, 120, 50, (0,0,255), GREEN)

        if player1.life <= 0:
            show_end_screen(screen, player2.name)
            return
        elif player2.life <= 0:
            show_end_screen(screen, player1.name)
            return
        
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
                            print(f"a carta {selected_card.nome} foi colocada com {selected_card.vida} de vida")
                            sons.tocar_musica_carta()
                            break
                dragging = False
                selected_card = None

            # Clique no botão "Passar Turno"
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pass_button.collidepoint(pygame.mouse.get_pos()):
                    
                    opponent = player2 if current_player == player1 else player1

                    print(f"vez do jogador {current_player.name}")

                    current_front_row = grid[f'{current_player.name.lower().replace(" ", "_")}_front_row']
                    current_back_row = grid[f'{current_player.name.lower().replace(" ", "_")}_back_row']
                    opponent_front_row = grid[f'{opponent.name.lower().replace(" ", "_")}_front_row']
                    opponent_back_row = grid[f'{opponent.name.lower().replace(" ", "_")}_back_row']

                    for i in range(0,3):
                        if current_back_row[i]['card'] is not None:
                        
                            current_back_row[i]['card'].habilidade(current_back_row,current_front_row,opponent_back_row,opponent_front_row, current_player,opponent)
                            if current_back_row[i]['card'].tipo == 'equipamento' or current_back_row[i]['card'].tipo == 'feitiço':
                                current_back_row[i]['card'].take_damage(current_back_row[i],1)


                        if current_front_row[i]['card'] is not None:
                  
                            current_front_row[i]['card'].habilidade(current_front_row,current_back_row,opponent_back_row,opponent_front_row, current_player,opponent)
                            if current_front_row[i]['card'].tipo == 'equipamento' or current_front_row[i]['card'].tipo == 'feitiço':
                                current_front_row[i]['card'].take_damage(current_front_row[i],1)
                                
                    for i in range(0,3):
                        if opponent_back_row[i]['card'] is not None:
       
                            opponent_back_row[i]['card'].habilidade(opponent_back_row,opponent_front_row,current_back_row,current_front_row,opponent, current_player)

                            if opponent_back_row[i]['card'].tipo == 'equipamento' or opponent_back_row[i]['card'].tipo == 'feitiço':
                                opponent_back_row[i]['card'].take_damage(opponent_back_row[i],1)


                        if opponent_front_row[i]['card'] is not None:
                 
                            opponent_front_row[i]['card'].habilidade(opponent_front_row,opponent_back_row,current_back_row,current_front_row,opponent, current_player)

                            if opponent_front_row[i]['card'].tipo == 'equipamento' or opponent_front_row[i]['card'].tipo == 'feitiço':
                                opponent_front_row[i]['card'].take_damage(opponent_front_row[i],1)


                    # Itera pelas posições da linha de frente do jogador atual
                    for i, front_card in enumerate(current_front_row):
                        if front_card['occupied']:
                            if opponent_front_row[i]['occupied'] and opponent_front_row[i]['card'] is not None:
                                opponent_front_row[i]['card'].take_damage(opponent_front_row[i],front_card['card'].ataque)
   

                          
                            elif opponent_back_row[i]['occupied'] and opponent_back_row[i]['card'] is not None:
                                opponent_back_row[i]['card'].take_damage(opponent_back_row[i],front_card['card'].ataque)


                                
                            else:
                                opponent.take_damage(front_card['card'].ataque)

                    sons.tocar_musica_turno()
                    turn_counter += 1  # Incrementa o contador de turnos
                    ctrlPass+=1



                    if(len(player1.hand)<6 and len(player1.deck) > 0 and ctrlPass%2 == 0):
                        player1.hand.append(player1.deck.pop(0))
                    if(len(player2.hand)<6 and len(player2.deck) > 0 and ctrlPass%2 != 0 and ctrlPass !=1):
                        player2.hand.append(player2.deck.pop(0))
 

                    if turn_counter == 1:  
                        if current_player == player1:
                            move_back_to_front(grid, player2.name) 
                        else:
                            move_back_to_front(grid, player1.name)  

                    current_player = player2 if current_player == player1 else player1
                    turn_counter = 0 

        if dragging and selected_card:
            mx, my = pygame.mouse.get_pos()
            card_image = pygame.image.load(selected_card.img)
            card_image = pygame.transform.scale(card_image, (50, 75))
            screen.blit(card_image, (mx - 25, my - 37))

        pygame.display.flip()
