import pygame
import sys
from menu import show_menu
from game import start_game
import sons


screen = pygame.display.set_mode((1000, 800))
# Função principal
def main():
    pygame.init()   
    pygame.display.set_caption("Cartas Massa")
    menu = True
    playing = False

    while True:
        if menu:
            menu, playing = show_menu(screen)
           
        elif playing:
            start_game(screen)
           
        
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
if __name__ == "__main__":
    main()