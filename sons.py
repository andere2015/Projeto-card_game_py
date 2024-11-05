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
    pygame.mixer.music.load('assets/jogo_music.ogg')  # Carrega a música do jogo
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)  # Toca indefinidamente

# Função para som de mover carta
def tocar_musica_carta():
    pygame.mixer.music.load('assets/carta.mp3')  # Carrega a música do jogo
    pygame.mixer.music.set_volume(0.9)
    duracao = 1  # Duração desejada em segundos
    pygame.mixer.music.play()  # Toca indefinidamente
    # Aguarda a duração especificada
    pygame.time.delay(duracao * 1000)  # Converte para milissegundos
    # Para a música após o tempo especificado
    pygame.mixer.music.stop()

def tocar_musica_turno():
    pygame.mixer.music.load('assets/carta.mp3')  # Carrega a música do jogo
    pygame.mixer.music.set_volume(0.9)
    duracao = 1  # Duração desejada em segundos
    pygame.mixer.music.play()  # Toca indefinidamente
    # Aguarda a duração especificada
    pygame.time.delay(duracao * 1000)  # Converte para milissegundos
    # Para a música após o tempo especificado
    pygame.mixer.music.stop()

def tocar_musica_vitoria():
    pygame.mixer.music.load('assets/carta.mp3')  # Carrega a música do jogo
    pygame.mixer.music.set_volume(0.9)
    duracao = 10  # Duração desejada em segundos
    pygame.mixer.music.play()  # Toca indefinidamente
    # Aguarda a duração especificada
    pygame.time.delay(duracao * 1000)  # Converte para milissegundos
    # Para a música após o tempo especificado
    pygame.mixer.music.stop()




