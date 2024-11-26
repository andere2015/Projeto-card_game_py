import copy
import sons, random,time,pygame

class Card:
    def __init__(self, id , nome, vida, ataque, img, descricao,tipo,area):
        self.id = id
        self.nome = nome 
        self.vida = vida
        self.ataque = ataque
        self.img = img
        self.descricao = descricao
        self.tipo = tipo
        self.area = area
        # coloquei esses dois novos atributos para as cartas de efeito e feitiço
        # o effect é pra garantir que o efeito de aplicação unica não vai ser lançado mais de uma vez
        # o alvo é pra quando o efeito acabar, reverter o efeito na carta
        # tem um exemplo disso na carta not, já tá toda implementada
        self.effect=False
        self.alvo = []
    def take_damage(self,card, damage):

        if damage>0:
            from game import draw_damage_animation
            draw_damage_animation(card)
            self.vida-=damage
        if card['card'].vida <=0:
            sons.tocar_musica_morte()
            if len(card['card'].alvo)>0 or card['card'].nome == 'Capacitor':
                card['card'].reverter()
            card['occupied'] = False
            card['card'] = None
        print(f"{self.nome} tomou {damage} | vida atual {self.vida}")

    def habilidade(self,atual_row,other_row,back_inimigo,front_inimiga,player, opponent):
        return
    def reverter(self):
        return
        
class And(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(1,'And', vida, ataque, 'assets/and.svg', descricao, 'tropa','circuitos')  

class Arp(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(1,'Arp', vida, ataque, 'assets/arp.svg', descricao, 'feitiço','redes')
        
    def habilidade(self,atual_row,other_row,back_inimigo,front_inimiga,player, opponent):

        for i in range(0,3):
            if atual_row[i]['occupied'] is True and  atual_row[i]['card'] != self and atual_row[i]['card'].nome != 'Constante':
                print(f"A carta {atual_row[i]['card'].nome} sofreu um de dano do arp")
                atual_row[i]['card'].take_damage(atual_row[i],1)
                

            if other_row[i]['occupied'] is True and other_row[i]['card'].nome != 'Constante':
                print(f"A carta {other_row[i]['card'].nome} sofreu um de dano do arp")
                other_row[i]['card'].take_damage(other_row[i],1)
                

            if front_inimiga[i]['occupied'] is True and front_inimiga[i]['card'].nome != 'Constante':
                print(f"A carta {front_inimiga[i]['card'].nome} sofreu um de dano do arp")
                front_inimiga[i]['card'].take_damage(front_inimiga[i],1)
                

            if back_inimigo[i]['occupied'] is True and back_inimigo[i]['card'].nome != 'Constante':
                print(f"A carta {back_inimigo[i]['card'].nome} sofreu um de dano do arp")
                back_inimigo[i]['card'].take_damage(back_inimigo[i],1)
                

class ArvoreB(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(3,'Arvore B', vida, ataque, 'assets/arvoreb.svg', descricao, 'tropa','algoritmos')
    def habilidade(self, atual_row, other_row, back_inimigo, front_inimiga, player, opponent):
        if self.effect is False:
            ist=0
            for i in range(0,3):
                if atual_row[i]['card']==self:
                    ist = i
            if ist-1 >=0 and atual_row[ist-1]['occupied'] is False:
                atual_row[ist-1]['card'] = Nob()
                atual_row[ist-1]['occupied'] = True 
                
            
            if ist+1 <=2 and atual_row[ist+1]['occupied'] is False:
                atual_row[ist+1]['card'] = Nob()
                atual_row[ist+1]['occupied'] = True 
            self.effect=True

class ArvoreRB(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(4,'Árvore RB', vida, ataque, 'assets/rubro.svg', descricao, 'tropa','algoritmos')
    #rouba vida dos aliados adjacentes (o roube é igual a metade da vida atual da arvore rn)
    
    def habilidade(self,atual_row,other_row,back_inimigo,front_inimiga,player, opponent):

        ist=0
        for i in range(0,3):
            if atual_row[i]['card']==self:
                ist = i
        if ist-1 >=0 and atual_row[ist-1]['occupied'] and atual_row[ist-1]['card'].nome != 'Constante':
            print(f"Arvore RB roubou 2 de vida de {atual_row[ist-1]['card'].nome} que ficou com {atual_row[ist-1]['card'].vida}")
            atual_row[ist-1]['card'].take_damage(atual_row[ist-1],2)
            atual_row[ist]['card'].vida += 2
            
        
        if ist+1 <=2 and atual_row[ist+1]['occupied'] and atual_row[ist+1]['card'].nome != 'Constante':
            print(f"Arvore RB roubou 2 de vida de {atual_row[ist+1]['card'].nome} que ficou com {atual_row[ist+1]['card'].vida}")
            atual_row[ist+1]['card'].take_damage(atual_row[ist+1],2)
            atual_row[ist]['card'].vida += 2
            

class Bombe(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(5,'Bombe', vida, ataque, 'assets/bombe.svg', descricao, 'tropa','programação')
    def habilidade(self, atual_row, other_row, back_inimigo, front_inimiga, player, opponent):
        if self.effect is False:
            for i in range(0,3):
                if front_inimiga[i]['occupied']:
                    if front_inimiga[i]['card'].nome !='Constante':
                        print(f"a carta {front_inimiga[i]['card'].nome} teve o ataque reduzido pelo bombe")
                        front_inimiga[i]['card'].ataque-=1
            self.effect=True

class Break(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(6,'Break', 1, 0, 'assets/break.svg', descricao, 'feitiço','programação')
    def habilidade(self, atual_row, other_row, back_inimigo, front_inimiga, player, opponent):
        ist=0
        for i in range(0,3):
            if atual_row[i]['card']==self:
                ist = i
        if other_row[ist]['occupied']:
            other_row[ist]['card'].take_damage(other_row[ist],other_row[ist]['card'].vida)

        elif front_inimiga[ist]['occupied']:
            front_inimiga[ist]['card'].take_damage(front_inimiga[ist],front_inimiga[ist]['card'].vida)
            
        elif back_inimigo[ist]['occupied']:
            back_inimigo[ist]['card'].take_damage(back_inimigo[ist],back_inimigo[ist]['card'].vida)


class Bug(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(7,'Bug', vida, ataque, 'assets/bug.svg', descricao, 'tropa','programação')
    
    def habilidade(self, atual_row, other_row, back_inimigo, front_inimiga, player, opponent):
        if self.effect is False:
            for i in range(0,3):
                if atual_row[i]['occupied'] and atual_row[i]['card'].tipo == 'tropa' and atual_row[i]['card'].nome != 'Constante':
                    self.alvo.append(atual_row[i]['card'])
                if other_row[i]['occupied'] and other_row[i]['card'].tipo == 'tropa' and other_row[i]['card'].nome != 'Constante':
                    self.alvo.append(other_row[i]['card'])
                if back_inimigo[i]['occupied'] and back_inimigo[i]['card'].tipo == 'tropa' and back_inimigo[i]['card'].nome != 'Constante':
                    self.alvo.append(back_inimigo[i]['card'])
                if front_inimiga[i]['occupied'] and front_inimiga[i]['card'].tipo == 'tropa' and front_inimiga[i]['card'].nome != 'Constante':
                    self.alvo.append(front_inimiga[i]['card'])
            if len(self.alvo) <=3:
                for card in self.alvo:
                    card.ataque -= 2
                    if card.ataque<0:
                        card.ataque=1
                    print(f"A carta {card.nome} teve o ataque reduzido pelo bug")
            elif len(self.alvo)>3:
                self.alvo = random.sample(self.alvo,3)
                for card in self.alvo:
                    card.ataque -=2
                    if card.ataque<0:
                        card.ataque=1
                    print(f"A carta {card.nome} teve o ataque reduzido pelo bug")
            self.effect=True

class Capacitor(Card):
    
    def __init__(self, vida, ataque, descricao):
        super().__init__(8,'Capacitor', vida, ataque, 'assets/capacitor.svg', descricao, 'equipamento','circuitos')
        self.copias=[]

    def habilidade(self,atual_row,other_row,back_inimigo,front_inimiga,player, opponent):

        if self.effect is not True:
            self.effect=True
            for i in range (0,3):
                if atual_row[i]['occupied'] is not True or atual_row[i]['card'] == self:
                    atual_row[i]['card']=self
                    self.copias.append(atual_row[i])
                    atual_row[i]['occupied']=True
                    if other_row[i]['occupied'] and other_row[i]['card'].nome != 'Constante':
                        other_row[i]['card'].ataque+=2
                        self.alvo.append(other_row[i])
                        print(f"A carta {other_row[i]['card'].nome} sofreu efeito do capacitor | {other_row[i]['card'].ataque}")
        
    def reverter(self):
        for cardCopy in self.copias:
            cardCopy['card']=None
            cardCopy['occupied']=False
        for card in self.alvo:
            if card['occupied']:
                card['card'].ataque-=2
                print(f"o efeito do capacitor foi revertido na carta {card['card'].nome} | {card['card'].ataque} ")



class Clockpulse(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(9,'Clock Pulse', vida, ataque, 'assets/clock.svg', descricao, 'equipamento','circuitos')
        self.turno=1
    def habilidade(self,atual_row,other_row,back_inimigo,front_inimiga,player, opponent):

        ist=0
        for i in range(0,3):
            if atual_row[i]['card']==self:
                ist = i
        self.turno *= -1
        if(self.turno == 1):
            if other_row[ist]['occupied']:
                if front_inimiga[ist]['occupied'] and front_inimiga[ist]['card'].nome != 'Constante':
                    front_inimiga[ist]['card'].take_damage(front_inimiga[ist],other_row[ist]['card'].ataque)
                    print(f"a carta {other_row[ist]['card'].nome} atacou mais uma vez fora do seu turno")
                elif back_inimigo[ist]['occupied'] and back_inimigo[ist]['card'].nome != 'Constante':
                    back_inimigo[ist]['card'].take_damage(back_inimigo[ist],other_row[ist]['card'].ataque)
                    print(f"a carta {other_row[ist]['card'].nome} atacou mais uma vez fora do seu turno")



class Constante(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(10,'Constante', vida, ataque, 'assets/constant.svg', descricao, 'tropa','programação')

class Continue(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(11,'Continue', vida, ataque, 'assets/continue.svg', descricao, 'equipamento','programação')
    def habilidade(self, atual_row, other_row, back_inimigo, front_inimiga, player, opponent):
        ist=0
        for i in range(0,3):
            if atual_row[i]['card']==self:
                ist = i
        if other_row[ist]['occupied']:
            if front_inimiga[ist]['occupied'] and back_inimigo[ist]['occupied']:
                back_inimigo[ist]['card'].take_damage(back_inimigo[ist],other_row[ist]['card'].ataque)
            else:
                opponent.take_damage(other_row[ist]['card'].ataque)

class DdosAttack(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(12,'DDoS Attack', 4, 0, 'assets/ddos.svg', descricao, 'equipamento','Redes')

    def habilidade(self,atual_row,other_row,back_inimigo,front_inimiga,player, opponent):

        
        for i in range(0,3):
            if front_inimiga[i]['occupied'] and front_inimiga[i]['card'].nome != 'Constante' and self.effect is False:
                if front_inimiga[i]['card'].vida > 2:
                    self.alvo.append(front_inimiga[i])
                    front_inimiga[i]['card'].take_damage(front_inimiga[i],2)
                    print(f"A carta {front_inimiga[i]['card'].nome} sofreu 2 de dano do arp")
        self.effect= True

    def reverter(self):
        for card in self.alvo:
            if card['occupied'] and self.effect:
                card['card'].vida+=2
                print(f"A carta {card['card'].nome} recuperou 2 de vida")

class Derivada(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(13,'Derivada', 1, 0, 'assets/derivada.svg', descricao, 'feitiço','cálculo')
    def habilidade(self, atual_row, other_row, back_inimigo, front_inimiga, player, opponent):
        ist=0
        for i in range(0,3):
            if atual_row[i]['card']==self:
                ist = i
        if other_row[ist]['occupied']:
            other_row[ist]['card'].ataque //= 2

        elif front_inimiga[ist]['occupied']:
            front_inimiga[ist]['card'].ataque //= 2 

        elif back_inimigo[ist]['occupied']:
            back_inimigo[ist]['card'].ataque //= 2 

class Dijkstra(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(14,'Dijkstra', vida, ataque, 'assets/dijkstra.svg', descricao, 'tropa','cálculo')

class DoWhile(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(15,'Do While', vida, ataque, 'assets/dowhile.svg', descricao, 'tropa','programação')

class EspacoVetorial(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(16,'Espaco Vetorial', 1, 0, 'assets/vetorial.svg', descricao, 'feitiço','cálculo')
    def habilidade(self, atual_row, other_row, back_inimigo, front_inimiga, player, opponent):
        for i in range(0,3):
            if atual_row[i]['occupied']:
                if  atual_row[i]['card'].tipo == 'cálculo':
                    atual_row[i]['card'].ataque +=1
            if other_row[i]['occupied']:
                if  other_row[i]['card'].tipo == 'cálculo':
                    other_row[i]['card'].ataque +=1

class Fila(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(17,'Fila', 1, 0, 'assets/fila.svg', descricao, 'feitiço', 'programação')
    def habilidade(self, atual_row, other_row, back_inimigo, front_inimiga, player, opponent):
        if len(player.hand)<6 and len(player.deck)>0:
            player.hand.append(player.hand.pop())

            print(f"a o {player.name} recebeu a ultima carta do seu dack")
        

class Firewall(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(18,'Fire Wall', vida, ataque, 'assets/firewall.svg', descricao, 'equipamento', 'redes')
        self.copias=[]

    def habilidade(self,atual_row,other_row,back_inimigo,front_inimiga,player, opponent):

        if self.effect is not True:
            self.effect=True
            for i in range (0,3):
                if atual_row[i]['occupied'] is not True or atual_row[i]['card'] == self:
                    atual_row[i]['card']=self
                    self.copias.append(atual_row[i])
                    atual_row[i]['occupied']=True
                    if other_row[i]['occupied'] and other_row[i]['card'].nome != 'Constante':
                        other_row[i]['card'].vida+=2
                        self.alvo.append(other_row[i])
                        print(f"A carta {other_row[i]['card'].nome} sofreu efeito do firewall | {other_row[i]['card'].vida}")
        
    def reverter(self):
        for cardCopy in self.copias:
            cardCopy['card']=None
            cardCopy['occupied']=False
        

class FlipFlop(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(19,'FlipFlop', vida, ataque, 'assets/flipflop.svg', descricao, 'tropa', 'circuitos')

class Getway(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(20,'Getway', 1, 0, 'assets/getway.svg', descricao, 'feitiço', 'redes')
    def habilidade(self, atual_row, other_row, back_inimigo, front_inimiga, player, opponent):
        ist=0
        for i in range(0,3):
            if atual_row[i]['card']==self:
                ist = i
        if other_row[ist]['occupied']:
            other_row[ist]['card'].ataque = 0
            if other_row[0]['occupied'] and ist != 0:
                other_row[ist]['card'].ataque += other_row[0]['card'].ataque
            if other_row[1]['occupied'] and ist != 1:
                other_row[ist]['card'].ataque += other_row[1]['card'].ataque
            if other_row[2]['occupied'] and ist != 2:
                other_row[ist]['card'].ataque += other_row[2]['card'].ataque

        elif front_inimiga[ist]['occupied']:
            front_inimiga[ist]['card'].ataque = 0
            if front_inimiga[0]['occupied'] and ist != 0:
                front_inimiga[ist]['card'].ataque += front_inimiga[0]['card'].ataque
            if front_inimiga[1]['occupied'] and ist != 1:
                front_inimiga[ist]['card'].ataque += front_inimiga[1]['card'].ataque
            if front_inimiga[2]['occupied'] and ist != 2:
                front_inimiga[ist]['card'].ataque += front_inimiga[2]['card'].ataque

        elif back_inimigo[ist]['occupied']:
            back_inimigo[ist]['card'].ataque = 0
            if back_inimigo[0]['occupied'] and ist != 0:
                back_inimigo[ist]['card'].ataque += back_inimigo[0]['card'].ataque
            if back_inimigo[1]['occupied'] and ist != 1:
                back_inimigo[ist]['card'].ataque += back_inimigo[1]['card'].ataque
            if back_inimigo[2]['occupied'] and ist != 2:
                back_inimigo[ist]['card'].ataque += back_inimigo[2]['card'].ataque



class GrafoPonderado(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(21,'Grafo Ponderado', 1, 0, 'assets/ponderar.svg', descricao, 'feitiço', 'algoritmos')
    def habilidade(self, atual_row, other_row, back_inimigo, front_inimiga, player, opponent):
        menorInimigo = 100
        menorAliado = 100
        for i in range(0,3):
            if front_inimiga[i]['occupied']:
                if front_inimiga[i]['card'].tipo == 'tropa' and front_inimiga[i]['card'].ataque<menorInimigo:
                    menorInimigo=front_inimiga[i]['card'].ataque
            if back_inimigo[i]['occupied']:
                if back_inimigo[i]['card'].tipo == 'tropa' and back_inimigo[i]['card'].ataque<menorInimigo:
                    menorInimigo=back_inimigo[i]['card'].ataque

        for i in range(0,3):
            if other_row[i]['occupied']:
                if other_row[i]['card'].tipo == 'tropa' and other_row[i]['card'].ataque<menorAliado:
                    menorAliado=other_row[i]['card'].ataque
            if atual_row[i]['occupied']:
                if atual_row[i]['card'].tipo == 'tropa' and atual_row[i]['card'].ataque<menorAliado:
                    menorAliado=atual_row[i]['card'].ataque

        for i in range(0,3):
            if front_inimiga[i]['occupied']:
                if front_inimiga[i]['card'].tipo == 'tropa' and menorInimigo != 100:
                    front_inimiga[i]['card'].ataque=menorInimigo
            if back_inimigo[i]['occupied']:
                if back_inimigo[i]['card'].tipo == 'tropa' and menorInimigo != 100:
                    back_inimigo[i]['card'].ataque =menorInimigo

        for i in range(0,3):
            if other_row[i]['occupied']:
                if other_row[i]['card'].tipo == 'tropa' and menorAliado != 100:
                    other_row[i]['card'].ataque = menorAliado
            if atual_row[i]['occupied']:
                if atual_row[i]['card'].tipo == 'tropa' and menorAliado != 100:
                    atual_row[i]['card'].ataque = menorAliado


class GrafoFonte(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(22,'Grafo fonte', vida, ataque, 'assets/fonte.svg', descricao, 'tropa', 'algoritmos')

class GrafoSumidouro(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(23,'Grafo Sumidouro', vida, ataque, 'assets/sumidouro.svg', descricao, 'tropa', 'algoritmos')

class HeapMaximo(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(24,'Heap Max', 1, 0, 'assets/heapmax.svg', descricao, 'feitiço', 'algoritmos')
    def habilidade(self, atual_row, other_row, back_inimigo, front_inimiga, player, opponent):
        player.deck.sort(key=lambda Card: Card.ataque, reverse=True)
        print(f"O baralho do {player.name} foi ordenado")

class HeapMinimo(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(24,'Heap Max', 1, 0, 'assets/heapmin.svg', descricao, 'feitiço', 'algoritmos')
    def habilidade(self, atual_row, other_row, back_inimigo, front_inimiga, player, opponent):
        player.deck.sort(key=lambda Card: Card.ataque)
        print(f"O baralho do {player.name} foi ordenado")


class Hub(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(25,'Hub', vida, ataque, 'assets/hub.svg', descricao, 'tropa', 'redes')

class IntegracaoPartes(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(26,'Integracao por Partes', vida, ataque, 'assets/intpartes.svg', descricao, 'tropa', 'cálculo')

class Integral(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(27,'Integral', vida, ataque, 'assets/integral.svg', descricao, 'equipamento', 'cálculo')
    def habilidade(self, atual_row, other_row, back_inimigo, front_inimiga, player, opponent):
        ist=0
        for i in range(0,3):
            if atual_row[i]['card']==self:
                ist = i
        if other_row[ist]['occupied']:
            other_row[ist]['card'].ataque *= 2

        elif front_inimiga[ist]['occupied']:
            front_inimiga[ist]['card'].ataque *= 2 

        elif back_inimigo[ist]['occupied']:
            back_inimigo[ist]['card'].ataque *= 2 

class Karnaugh(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(82,'Karnaugh', vida, ataque, 'assets/karnaugh.svg', descricao, 'tropa', 'circuitos')

class Multiplexador(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(29,'Multiplexador', 1, 0, 'assets/multplex.svg', descricao, 'feitiço', 'circuitos')
    def habilidade(self, atual_row, other_row, back_inimigo, front_inimiga, player, opponent):
        if len(player.deck) > 0:
            player.hand.append(player.deck.pop(0))

class Nabla(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(30,'Nabla', vida, ataque, 'assets/nabla.svg', descricao, 'tropa', 'cálculo')

class Not(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(31,'Not', vida, ataque, 'assets/not.svg', descricao, 'equipamento', 'circuitos')
        
    def habilidade(self,atual_row,other_row,back_inimigo,front_inimiga,player, opponent):

        ist=0
        
        for i in range(0,3):
            if atual_row[i]['card']==self:
                ist = i
        
        self.alvo.append(other_row[ist])

        if self.alvo[0]['occupied']:
            if self.alvo[0]['card'].nome != 'Constante' and self.effect is not True:
                attack = self.alvo[0]['card'].ataque
                self.alvo[0]['card'].ataque = self.alvo[0]['card'].vida
                self.alvo[0]['card'].vida = attack
                print(f"O efeito not foi aplicado na carta {self.alvo[0]['card'].nome} {self.alvo[0]['card'].vida} <=> {self.alvo[0]['card'].ataque}")
                self.effect = True

    def reverter(self):
        if self.alvo[0]['occupied']:
            if self.alvo[0]['card'].nome != 'Constante' and self.effect is not False:
                attack = self.alvo[0]['card'].ataque
                self.alvo[0]['card'].ataque = self.alvo[0]['card'].vida
                self.alvo[0]['card'].vida = attack
                print(f"O efeito not foi removido na carta {self.alvo[0]['card'].nome} {self.alvo[0]['card'].vida} <=> {self.alvo[0]['card'].ataque}")


class Or(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(32,'Or', vida, ataque, 'assets/or.svg', descricao, 'tropa', 'circuitos')

class Pilha(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(33,'Pilha', 1, 0, 'assets/pilha.svg', descricao, 'feitiço', 'programação')
    def habilidade(self, atual_row, other_row, back_inimigo, front_inimiga, player, opponent):
        if len(player.hand)<6 and len(player.deck)>0:
            player.hand.append(player.hand.pop(0))

            print(f"a o {player.name} recebeu a ultima carta do seu dack")

class Ponteiro(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(34,'Ponteiro', vida, ataque, 'assets/ponteiro.svg', descricao, 'tropa', 'programação')

class Registrador(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(35,'Registrador', vida, ataque, 'assets/register.svg', descricao, 'tropa', 'circuitos')


class RegraCadeia(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(36,'Regra da cadeia', vida, ataque, 'assets/cadeia.svg', descricao, 'tropa', 'cálculo')
    def habilidade(self, atual_row, other_row, back_inimigo, front_inimiga, player, opponent):
        if self.effect is False:
            ist=0
            
            for i in range(0,3):
                if atual_row[i]['card']==self:
                    ist = i

            if other_row[ist]['occupied']:
                self.alvo.append(other_row[ist]['card'])
                other_row[ist]['occupied']=False
                other_row[ist]['card']=None
            
            elif front_inimiga[ist]['occupied']:
                self.alvo.append(front_inimiga[ist]['card'])
                front_inimiga[ist]['occupied']=False
                front_inimiga[ist]['card']=None

            elif back_inimigo[ist]['occupied']:
                self.alvo.append(back_inimigo[ist]['card'])
                back_inimigo[ist]['occupied']=False
                back_inimigo[ist]['card']=None

            self.effect = True


class Repetidor(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(37,'Repetidor', vida, ataque, 'assets/repetidor.svg', descricao, 'tropa', 'redes')

class Return(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(38,'Return', 1, 0, 'assets/return.svg', descricao, 'feitiço', 'programação')
    def habilidade(self, atual_row, other_row, back_inimigo, front_inimiga, player, opponent):
        ist=0
        
        for i in range(0,3):
            if atual_row[i]['card']==self:
                ist = i
        
        for i in range(0,3):
            if other_row[i]['occupied'] is True and other_row[i]['card'].nome != 'Constante':
                print(f"A carta {other_row[i]['card'].nome} retornou para a mão do jogador")
                if len(player.hand)<6:
                    player.hand.append(other_row[i]['card'])
                else:
                    player.deck.append(other_row[i]['card'])
                atual_row[i]['card']=None
                atual_row[i]['occupied']=False

            elif front_inimiga[i]['occupied'] is True and front_inimiga[i]['card'].nome != 'Constante':
                print(f"A carta {front_inimiga[i]['card'].nome} retornou para a mão do jogador")
                if len(player.hand)<6:
                    player.hand.append(front_inimiga[i]['card'])
                else:
                    player.deck.append(front_inimiga[i]['card'])
                front_inimiga[i]['card']=None
                front_inimiga[i]['occupied']=False

            elif back_inimigo[i]['occupied'] is True and back_inimigo[i]['card'].nome != 'Constante':
                print(f"A carta {back_inimigo[i]['card'].nome} retornou para a mão do jogador")
                if len(player.hand)<6:
                    player.hand.append(back_inimigo[i]['card'])
                else:
                    player.deck.append(back_inimigo[i]['card'])
                back_inimigo[i]['card']=None
                back_inimigo[i]['occupied']=False

class Riemann(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(39,'Riemann', vida, ataque, 'assets/riemann.svg', descricao, 'tropa', 'cálculo')

class Roteador(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(40,'Roteador', vida, ataque, 'assets/roteador.svg', descricao, 'tropa', 'redes')
    
    def habilidade(self,atual_row,other_row,back_inimigo,front_inimiga,player, opponent):

        if self.effect is not True:
            for i in range(0,3):
                if other_row[i]['occupied'] and other_row[i]['card'].area == 'redes':
                    other_row[i]['card'].ataque += 1
                    self.alvo.append(other_row[i])
                    self.effect = True
                    print(f"a carta {other_row[i]['card'].nome} recebeu ponto de ataque")

    def reverter(self):
        if self.effect is True:
            for card in self.alvo:
                if card['occupied']:
                    card['card'].ataque-=1
                    print(f"a carta {card['card'].nome} vou tou ao seu atque normal")

class Sniffer(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(41,'Sniffer', vida, ataque, 'assets/sniffer.svg', descricao, 'tropa', 'redes')

    def habilidade(self,atual_row,other_row,back_inimigo,front_inimiga,player, opponent):
        if self.effect is False:
            player.deck.append(opponent.hand.pop(0))
            self.effect=True

class Somatorio(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(42,'Somatório', 1, 0, 'assets/shomatorio.svg', descricao, 'feitiço', 'cálculo')
    def habilidade(self, atual_row, other_row, back_inimigo, front_inimiga, player, opponent):
        ist=0
        for i in range(0,3):
            if atual_row[i]['card']==self:
                ist = i
        if other_row[ist]['occupied']:
            if other_row[0]['occupied'] and ist != 0:
                other_row[ist]['card'].ataque += other_row[0]['card'].ataque
                other_row[0]['card'].take_damage(other_row[0], other_row[0]['card'].vida)

            if other_row[1]['occupied'] and ist != 1:
                other_row[ist]['card'].ataque += other_row[1]['card'].ataque
                other_row[1]['card'].take_damage(other_row[1], other_row[1]['card'].vida)

            if other_row[2]['occupied'] and ist != 2:
                other_row[ist]['card'].ataque += other_row[2]['card'].ataque
                other_row[2]['card'].take_damage(other_row[2], other_row[2]['card'].vida)


class Struct(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(43,'Struct', vida, ataque, 'assets/struct.svg', descricao, 'tropa', 'programação')

class SubstituicaoTrigonometrica(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(44,'Subs Trigonométrica', vida, ataque, 'assets/subtrig.svg', descricao, 'tropa', 'cálculo')
    def habilidade(self, atual_row, other_row, back_inimigo, front_inimiga, player, opponent):
        if self.effect is False:

            ist=0
            for i in range(0,3):
                if atual_row[i]['card']==self:
                    ist = i
            if other_row[ist]['occupied']:
                auxCard = other_row[ist]['card']
                other_row[ist]['card'] = atual_row[ist]['card']
                atual_row[ist]['card'] = auxCard
            self.effect= True

class Switch(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(45,'Switch', vida, ataque, 'assets/switch.svg', descricao, 'tropa', 'redes')

class Ttl(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(46,'TTL', 1, 0, 'assets/ttl.svg', descricao, 'feitiço', 'redes')
    def habilidade(self,atual_row,other_row,back_inimigo,front_inimiga,player, opponent):
        ist=0
        
        for i in range(0,3):
            if atual_row[i]['card']==self:
                ist = i

        if other_row[ist]['occupied'] and other_row[ist]['card'].nome!='Constante':
            other_row[ist]['card'].tipo = 'equipamento'
            print(f"a vida da carta {other_row[ist]['card'].nome} agora é ttl")

        elif front_inimiga[ist]['occupied'] and front_inimiga[ist]['card'].nome!='Constante':
            front_inimiga[ist]['card'].tipo = 'equipamento'
            print(f"a vida da carta {front_inimiga[ist]['card'].nome} agora é ttl")

        elif back_inimigo[ist]['occupied'] and back_inimigo[ist]['card'].nome!='Constante' and back_inimigo[ist]['card'].tipo!='feitiço':
            back_inimigo[ist]['card'].tipo = 'equipamento'
            print(f"a vida da carta {back_inimigo[ist]['card'].nome} agora é ttl")

class Xor(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(47,'Xor', vida, ataque, 'assets/xor.svg', descricao, 'tropa', 'Circuitos')

class TeoremaConfronto(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(48,'Teorema do confronto', 1, 0, 'assets/confronto.svg', descricao, 'feitiço', 'cálculo')
    def habilidade(self, atual_row, other_row, back_inimigo, front_inimiga, player, opponent):
        ist=0
        for i in range(0,3):
            if atual_row[i]['card']==self:
                ist = i

        if other_row[ist]['occupied']:
            if front_inimiga[ist]['occupied']:
                front_inimiga[ist]['card'].take_damage(front_inimiga[ist],other_row[ist]['card'].ataque)
            elif back_inimigo[ist]['occupied']:
                back_inimigo[ist]['card'].take_damage(back_inimigo[ist],other_row[ist]['card'].ataque)

class SwitchCode(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(48,'Código Switch', vida, ataque, 'assets/switchC.svg', descricao, 'equipamento', 'programação')

class Nob(Card):
    def __init__(self):
        super().__init__(48,'Código Switch', 3, 1, 'assets/nob.svg', 'Atrapalhar', 'tropa', 'algoritmos')


and_carta = And(50, 1, "Operação lógica que resulta em verdadeiro se ambas as entradas forem verdadeiras.Nenhuma habilidade especial.")
arp_carta = Arp(8, 4, "Protocolo que mapeia endereços IP para endereços MAC em uma rede local.Causa 1 de dano a todas as cartas.")
arvore_b_carta = ArvoreB(12, 7, "Estrutura de dados para organização eficiente de informações. Nenhuma habilidade especial.")
arvore_rb_carta = ArvoreRB(14, 9, "Árvore binária de busca autoajustável e equilibrada. Rouba 2 de vida dos aliados adjacentes.")
bombe_carta = Bombe(10, 6, "Primeiro computador criado por Alan Turing para vencer a máquina Enigma. Reduz o ataque dos inimigos em 1 unidade.")
break_carta = Break(6, 3, "Interrompe o fluxo de execução em estruturas de controle. Nenhuma habilidade especial.")
bug_carta = Bug(8, 5, "Um erro inesperado no código que pode causar falhas. Reduz o dano ou o ataque de 3 cartas aleatórias no campo de batalha.")
capacitor_carta = Capacitor(6, 2, "Componente que armazena carga elétrica em circuitos. Cria cópias no backend, aumentando o ataque de cartas à frente em 2 pontos.")
clockpulse_carta = Clockpulse(7, 3, "Sinal periódico que sincroniza circuitos digitais. Faz com que a carta da frente ataque cartas inimigas todos os turnos.")
constante_carta = Constante(9, 2, "Valor fixo que não muda durante a execução do programa. Nenhuma habilidade especial.")
continue_carta = Continue(5, 3, "Continua o fluxo de execução no próximo ciclo de um loop. Nenhuma habilidade especial.")
ddos_attack_carta = DdosAttack(10, 7, "Ataque que sobrecarrega um serviço com tráfego malicioso de múltiplas fontes. Reduz a vida de todas as cartas inimigas em 2 por um turno.")
derivada_carta = Derivada(11, 6, "Representa a taxa de variação de uma função. Nenhuma habilidade especial.")
dijkstra_carta = Dijkstra(14, 8, "Algoritmo para encontrar o caminho mais curto em um grafo. Nenhuma habilidade especial.")
do_while_carta = DoWhile(7, 4, "Estrutura de controle que executa um bloco de código ao menos uma vez. Nenhuma habilidade especial.")
espaco_vetorial_carta = EspacoVetorial(9, 5, "Conjunto de vetores que podem ser somados e multiplicados por escalares. Aumenta o ataque e a vida das cartas de cálculo em 1 unidade.")
fila_carta = Fila(6, 2, "Estrutura de dados que segue o princípio FIFO (First In, First Out). Pega a carta na última posição do baralho.")
firewall_carta = Firewall(10, 6, "Sistema de segurança que controla o tráfego de entrada e saída em uma rede. Preenche espaços vazios no backend e cura cartas no frontend em 2 pontos.")
flipflop_carta = FlipFlop(7, 4, "Dispositivo de memória que armazena um bit. Nenhuma habilidade especial.")
getway_carta = Getway(8, 5, "Dispositivo que interliga redes distintas. Nenhuma habilidade especial.")
grafo_ponderado_carta = GrafoPonderado(12, 7, "Grafo onde as arestas possuem pesos associados. Nenhuma habilidade especial.")
grafo_fonte_carta = GrafoFonte(11, 6, "Grafo onde todos os caminhos começam em um único ponto. Nenhuma habilidade especial.")
grafo_sumidouro_carta = GrafoSumidouro(11, 6, "Grafo onde todos os caminhos levam a um único ponto final. Nenhuma habilidade especial.")
heap_maximo_carta = HeapMaximo(1, 0, "Estrutura onde o valor máximo é sempre a raiz. Ordena as cartas do baralho pelo maior valor de poder ou vida.")
heap_minimo_carta = HeapMinimo(1, 0, "Estrutura onde o valor mínimo é sempre a raiz. Ordena as cartas do baralho pelo menor valor de poder ou vida.")
hub_carta = Hub(8, 4, "Dispositivo que conecta vários dispositivos em uma rede. Nenhuma habilidade especial.")
integracao_partes_carta = IntegracaoPartes(11, 6, "Técnica de integração baseada na regra do produto da derivação. Nenhuma habilidade especial.")
integral_carta = Integral(10, 5, "Operação que calcula a área sob uma curva. Nenhuma habilidade especial.")
karnaugh_carta = Karnaugh(12, 8, "Mapa usado para simplificar expressões booleanas. Nenhuma habilidade especial.")
multiplexador_carta = Multiplexador(9, 5, "Dispositivo que combina vários sinais em um único canal. Nenhuma habilidade especial.")
nabla_carta = Nabla(10, 6, "Operador usado em cálculo vetorial para gradientes, divergências e rotacionais. Nenhuma habilidade especial.")
not_carta = Not(6, 3, "Porta lógica que inverte o valor lógico de uma entrada. Inverte a vida com o ataque de uma carta.")
or_carta = Or(7, 4, "Porta lógica que resulta em verdadeiro se pelo menos uma entrada for verdadeira. Nenhuma habilidade especial.")
pilha_carta = Pilha(9, 5, "Estrutura de dados que segue o princípio LIFO (Last In, First Out). Pega a carta no topo do baralho.")
ponteiro_carta = Ponteiro(8, 4, "Variável que armazena o endereço de memória de outro dado. Nenhuma habilidade especial.")
registrador_carta = Registrador(10, 6, "Componente de armazenamento temporário em processadores. Nenhuma habilidade especial.")
regra_cadeia_carta = RegraCadeia(11, 6, "Método para calcular derivadas de funções compostas. Nenhuma habilidade especial.")
repetidor_carta = Repetidor(8, 4, "Dispositivo que amplifica sinais para estender a comunicação. Nenhuma habilidade especial.")
return_carta = Return(7, 3, "Comando que encerra a execução de uma função e pode retornar um valor. Retorna a carta imediatamente para a mão.")
riemann_carta = Riemann(12, 7, "Método de aproximação para calcular integrais. Nenhuma habilidade especial.")
roteador_carta = Roteador(10, 5, "Dispositivo que encaminha pacotes de dados entre redes. Aumenta o ataque e a vida das cartas do tipo Redes em 1 ponto.")
sniffer_carta = Sniffer(9, 5, "Ferramenta que captura pacotes de dados em uma rede. Remove uma carta aleatória da mão do inimigo e coloca-a no seu baralho.")
somatorio_carta = Somatorio(11, 6, "Soma de uma sequência de números. Nenhuma habilidade especial.")
struct_carta = Struct(9, 5, "Estrutura que agrupa diferentes tipos de dados. Nenhuma habilidade especial.")
substituicao_trigonometrica_carta = SubstituicaoTrigonometrica(11, 6, "Técnica de substituição em cálculos integrais. Nenhuma habilidade especial.")
switch_carta = Switch(8, 4, "Dispositivo que conecta dispositivos dentro de uma mesma rede. Nenhuma habilidade especial.")
ttl_carta = Ttl(7, 4, "Determina por quanto tempo um pacote pode circular na rede. Transforma a vida do monstro em TTL.")
xor_carta = Xor(7, 4, "Porta lógica que retorna verdadeiro se as entradas forem diferentes. Nenhuma habilidade especial.")
teorema_confronto_carta = TeoremaConfronto(12, 7, "Afirmação que relaciona funções em limites. Nenhuma habilidade especial.")
switch_code_carta = SwitchCode(10, 5, "Estrutura de controle de fluxo baseada em condições. Nenhuma habilidade especial.")


cartas_existentes = [
    and_carta, arp_carta, arvore_b_carta, arvore_rb_carta, bombe_carta, break_carta, bug_carta, 
    capacitor_carta, clockpulse_carta, constante_carta, continue_carta, ddos_attack_carta, derivada_carta, 
    dijkstra_carta, do_while_carta, espaco_vetorial_carta, fila_carta, firewall_carta, flipflop_carta, 
    getway_carta, grafo_ponderado_carta, grafo_fonte_carta, grafo_sumidouro_carta, heap_maximo_carta,heap_minimo_carta, 
    hub_carta, integracao_partes_carta, integral_carta, karnaugh_carta, multiplexador_carta, nabla_carta, 
    not_carta, or_carta, pilha_carta, ponteiro_carta, registrador_carta, regra_cadeia_carta, repetidor_carta, 
    return_carta, riemann_carta, roteador_carta, sniffer_carta, somatorio_carta, struct_carta, 
    substituicao_trigonometrica_carta, switch_carta, ttl_carta, xor_carta, teorema_confronto_carta, switch_code_carta
]