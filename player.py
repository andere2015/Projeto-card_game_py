import pygame

class Player:
    def __init__(self, name):
        self.name = name
        self.life = 40
        self.hand = []
        self.deck = []
    
    def take_damage(self,damage):
        if damage<0:
            return
        self.life-=damage
        print(f"{self.name} tomou {damage} de dano")

   
            
    