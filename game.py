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

def start_game(screen):
    field_image = pygame.image.load('image.png')
    field_image = pygame.transform.scale(field_image, (729, 625))

    player1 = Player("Jogador 1")
    player2 = Player("Jogador 2")

    player1.deck = deck_builder(screen, player1)
    player2.deck = deck_builder(screen, player2)
    # aki é so pra trest depois usarei a função draw pra pegar de fato uma carta e n apenas sortear
    player1.hand = random.sample(player1.deck, 6)
    player2.hand = random.sample(player2.deck, 6)

    screen.fill(WHITE)
    screen.blit(field_image, (0, 0))

    # Grid para posicionar as cartas no campo
    grid = {
        'player_1_back_row': [(269, 417, 50, 75), (353, 417, 50, 75), (438, 417, 50, 75)],
        'player_1_front_row': [(269, 330, 50, 75), (353, 330, 50, 75), (438, 330, 50, 75)],
        'player_2_front_row': [(268, 202, 50, 75), (353, 202, 50, 75), (439, 202, 50, 75)],
        'player_2_back_row': [(266, 115, 50, 75), (351, 115, 50, 75), (436, 115, 50, 75)],
        'player_1_hand': [(201, 520, 45, 70), (260, 520, 45, 70), (324, 520, 45, 70), (389, 520, 45, 70), (449, 520, 45, 70), (504, 520, 45, 70)],
        'player_2_hand': [(204, 20, 45, 70), (263, 20, 45, 70), (327, 20, 45, 70), (392, 20, 45, 70), (452, 20, 45, 70), (507, 20, 45, 70)]
    }

    for i, card in enumerate(player1.hand):
        x, y, width, height = grid['player_1_hand'][i]
        card_image = pygame.image.load(card.asset)
        card_image = pygame.transform.scale(card_image, (width+20, height+25))
        screen.blit(card_image, (x, y))

    for i, card in enumerate(player2.hand):
        x, y, width, height = grid['player_2_hand'][i]
        card_image = pygame.image.load(card.asset)
        card_image = pygame.transform.scale(card_image, (width, height))
        screen.blit(card_image, (x, y))


    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
