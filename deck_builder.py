import sys
import pygame
from constants import WHITE, BLACK, GREEN
from cartas import cartas_existentes

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect(center=(x, y))
    surface.blit(textobj, textrect)

def draw_card_options(screen, cards, selected_cards):
    font = pygame.font.SysFont(None, 20)
    quantity_font = pygame.font.SysFont(None, 25)

    for i, card in enumerate(cards):
        x = 50 + (i % 5) * 120
        y = 150 + (i // 5) * 200
        card_image = pygame.image.load(card.img)
        card_image = pygame.transform.scale(card_image, (100, 150))
        screen.blit(card_image, (x, y))

        if selected_cards.get(card, 0) > 0:
            pygame.draw.rect(screen, GREEN, (x - 5, y - 5, 110, 160), 3)

        card_count = selected_cards.get(card, 0)
        draw_text(f'x{card_count}', quantity_font, BLACK, screen, x + 85, y + 140)

        draw_text(card.tipo, font, BLACK, screen, x + 50, y + 160)

def deck_builder(screen, player):
    font = pygame.font.SysFont(None, 30)
    selected_cards = {}
    available_cards = cartas_existentes

    while sum(selected_cards.values()) < 5:
        screen.fill(WHITE)
        draw_text(f'{player.name}, escolha suas cartas ({sum(selected_cards.values())}/20)', font, BLACK, screen, 364, 50)
        draw_card_options(screen, available_cards, selected_cards)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                for i, card in enumerate(available_cards):
                    x = 50 + (i % 5) * 120
                    y = 150 + (i // 5) * 200
                    if x <= mx <= x + 100 and y <= my <= y + 150:
                        current_count = selected_cards.get(card, 0)
                        if current_count < 3:
                            selected_cards[card] = current_count + 1
                        elif current_count == 3:
                            selected_cards[card] = 0
                        if selected_cards[card] == 0:
                            del selected_cards[card]
                        break

        pygame.display.flip()

    player.deck = [card for card, count in selected_cards.items() for _ in range(count)]
    return player.deck
