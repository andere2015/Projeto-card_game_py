import pygame

class Player:
    def __init__(self, name):
        self.name = name
        self.life = 20
        self.hand = []
        self.deck = []
    
    def take_damage(self,damage):
        self.life-=damage
        print(f"{self.name} tomou {damage} de dano")

   
            
    