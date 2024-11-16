import pygame
import time

pygame.mixer.init()
pygame.init()
import pygame
import time

pygame.mixer.init()
pygame.init()


# Função para tocar a música do menu
def tocar_musica_menu():
    pygame.mixer.music.load('assets/videoplayback.mp3')  # Carrega a música do menu
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)  # Toca indefinidamente

# Função para parar a música
def parar_musica():
    pygame.mixer.music.stop()

# Função para tocar a música do jogo
def tocar_musica_jogo():
    pygame.mixer.music.load('assets/Legião Urbana.mp3')  # Carrega a música do jogo
    pygame.mixer.music.set_volume(0.9)
    pygame.mixer.music.play(-1)  # Toca indefinidamente

# Função para som de mover carta
def tocar_musica_carta():
    carta = pygame.mixer.Sound('assets/carta.mp3')  
    carta.set_volume(0.9)
    carta.play() 


def tocar_musica_turno():
    turno = pygame.mixer.Sound('assets/carta.mp3')  
    turno.set_volume(0.9)
    turno.play() 

def tocar_musica_morte():
    morte = pygame.mixer.Sound('assets/dano.mp3')  
    morte.set_volume(0.7)
    morte.play() 


def tocar_musica_vitoria():
    pygame.mixer.music.load('assets/carta.mp3')  
   
    pygame.mixer.music.set_volume(0.9)
    pygame.mixer.music.play()  
  




