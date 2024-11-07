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
        self.alvo= None
    def take_damage(self,card, damage):
        self.vida-=damage
        if card['card'].vida <=0:
            card['card'].reverter()
            card['occupied'] = False
            card = None
        print(f"{self.nome} tomou {damage}")

    def habilidade(self,atual_row,other_row,front_inimiga,back_inimigo):
        return
    def reverter(self):
        return
        
class And(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(1,'And', vida, ataque, 'assets/and.svg', descricao, 'tropa','circuitos')
      

class Arp(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(2,'Arp', vida, ataque, 'assets/arp.svg', descricao, 'feitiço','redes')

class ArvoreB(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(3,'Arvore B', vida, ataque, 'assets/arvoreb.svg', descricao, 'tropa','algoritmos')

class ArvoreRB(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(4,'Árvore RB', vida, ataque, 'assets/rubro.svg', descricao, 'tropa','algoritmos')
    #rouba vida dos aliados adjacentes (o roube é igual a metade da vida atual da arvore rn)
    def habilidade(self, atual_row, other_row, front_inimiga, back_inimigo):
        ist=0
        for i in range(0,3):
            if atual_row[i]['card']==self:
                ist = i
        if ist-1 >=0 and atual_row[ist-1]['occupied'] and atual_row[ist-1]['card'].nome != 'Constante':
            atual_row[ist-1]['card'].take_damage(atual_row[ist-1],2)
            atual_row[ist]['card'].vida += 2
            print(f"Arvore RB roubou 2 de vida de {atual_row[ist-1]['card'].nome} que ficou com {atual_row[ist-1]['card'].vida}")
        
        if ist+1 <=2 and atual_row[ist+1]['occupied'] and atual_row[ist+1]['card'].nome != 'Constante':
            atual_row[ist+1]['card'].take_damage(atual_row[ist+1],2)
            atual_row[ist]['card'].vida += 2
            print(f"Arvore RB roubou 2 de vida de {atual_row[ist+1]['card'].nome} que ficou com {atual_row[ist-1]['card'].vida}")


                
        
        

class Bombe(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(5,'Bombe', vida, ataque, 'assets/bombe.svg', descricao, 'tropa','programação')

class Break(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(6,'Break', vida, ataque, 'assets/break.svg', descricao, 'feitiço','programação')

class Bug(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(7,'Bug', vida, ataque, 'assets/bug.svg', descricao, 'tropa','programação')

class Capacitor(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(8,'Capacitor', vida, ataque, 'assets/capacitor.svg', descricao, 'equipamento','circuitos')

class Clockpulse(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(9,'Clock Pulse', vida, ataque, 'assets/clock.svg', descricao, 'equipamento','circuitos')

class Constante(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(10,'Constante', vida, ataque, 'assets/constant.svg', descricao, 'tropa','programação')

class Continue(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(11,'Continue', vida, ataque, 'assets/continue.svg', descricao, 'feitiço','programação')

class DdosAttack(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(12,'DDoS Attack', vida, ataque, 'assets/ddos.svg', descricao, 'feitiço','Redes')

class Derivada(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(13,'Derivada', vida, ataque, 'assets/derivada.svg', descricao, 'feitiço','cálculo')

class Dijkstra(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(14,'Dijkstra', vida, ataque, 'assets/dijkstra.svg', descricao, 'tropa','cálculo')

class DoWhile(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(15,'Do While', vida, ataque, 'assets/dowhile.svg', descricao, 'tropa','programação')

class EspacoVetorial(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(16,'Espaco Vetorial', vida, ataque, 'assets/vetorial.svg', descricao, 'feitiço','cálculo')

class Fila(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(17,'Fila', vida, ataque, 'assets/fila.svg', descricao, 'feitiço', 'programação')

class Firewall(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(18,'Fire Wall', vida, ataque, 'assets/firewall.svg', descricao, 'tropa', 'redes')

class FlipFlop(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(19,'FlipFlop', vida, ataque, 'assets/flipflop.svg', descricao, 'tropa', 'circuitos')

class Getway(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(20,'Getway', vida, ataque, 'assets/getway.svg', descricao, 'feitiço', 'redes')

class GrafoPonderado(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(21,'Grafo Ponderado', vida, ataque, 'assets/ponderar.svg', descricao, 'feitiço', 'algoritmos')

class GrafoFonte(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(22,'Grafo fonte', vida, ataque, 'assets/fonte.svg', descricao, 'tropa', 'algoritmos')

class GrafoSumidouro(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(23,'Grafo Sumidouro', vida, ataque, 'assets/sumidouro.svg', descricao, 'tropa', 'algoritmos')

class HeapMaximo(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(24,'Heap Max', vida, ataque, 'assets/heapmax.svg', descricao, 'feitiço', 'algoritmos')

class Hub(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(25,'Hub', vida, ataque, 'assets/hub.svg', descricao, 'tropa', 'redes')

class IntegracaoPartes(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(26,'Integracao por Partes', vida, ataque, 'assets/intpartes.svg', descricao, 'equipamento', 'cálculo')


class Integral(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(27,'Integral', vida, ataque, 'assets/integral.svg', descricao, 'equipamento', 'cálculo')

class Karnaugh(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(82,'Karnaugh', vida, ataque, 'assets/karnaugh.svg', descricao, 'tropa', 'circuitos')

class Multiplexador(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(29,'Multiplexador', vida, ataque, 'assets/multplex.svg', descricao, 'feitiço', 'circuitos')

class Nabla(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(30,'Nabla', vida, ataque, 'assets/nabla.svg', descricao, 'tropa', 'cálculo')

class Not(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(31,'Not', vida, ataque, 'assets/not.svg', descricao, 'equipamento', 'circuitos')
        
        

    def habilidade(self, atual_row, other_row, front_inimiga, back_inimigo):
        ist=0
        
        for i in range(0,3):
            if atual_row[i]['card']==self:
                ist = i
        
        self.alvo = other_row[ist]

        if self.alvo['occupied']:
            if self.alvo['card'].nome != 'Constante' and self.effect is not True:
                attack = self.alvo['card'].ataque
                self.alvo['card'].ataque = self.alvo['card'].vida
                self.alvo['card'].vida = attack
                print(f"O efeito not foi aplicado na carta {self.alvo['card'].nome} {self.alvo['card'].vida} <=> {self.alvo['card'].ataque}")
                self.effect = True

    def reverter(self):
        if self.alvo['occupied']:
            if self.alvo['card'].nome != 'Constante' and self.effect is not False:
                attack = self.alvo['card'].ataque
                self.alvo['card'].ataque = self.alvo['card'].vida
                self.alvo['card'].vida = attack
                print(f"O efeito not foi removido na carta {self.alvo['card'].nome} {self.alvo['card'].vida} <=> {self.alvo['card'].ataque}")


class Or(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(32,'Or', vida, ataque, 'assets/or.svg', descricao, 'tropa', 'circuitos')

class Pilha(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(33,'Pilha', vida, ataque, 'assets/pilha.svg', descricao, 'feitiço', 'programação')

class Ponteiro(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(34,'Ponteiro', vida, ataque, 'assets/ponteiro.svg', descricao, 'tropa', 'programação')

class Registrador(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(35,'Registrador', vida, ataque, 'assets/register.svg', descricao, 'tropa', 'circuitos')

class RegraCadeia(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(36,'Regra da cadeia', vida, ataque, 'assets/cadeia.svg', descricao, 'tropa', 'cálculo')

class Repetidor(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(37,'Repetidor', vida, ataque, 'assets/repetidor.svg', descricao, 'tropa', 'redes')

class Return(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(38,'Return', vida, ataque, 'assets/return.svg', descricao, 'feitiço', 'programação')

class Riemann(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(39,'Riemann', vida, ataque, 'assets/riemann.svg', descricao, 'tropa', 'cálculo')

class Roteador(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(40,'Roteador', vida, ataque, 'assets/roteador.svg', descricao, 'tropa', 'redes')

class Sniffer(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(41,'Sniffet', vida, ataque, 'assets/sniffer.svg', descricao, 'tropa', 'redes')

class Somatorio(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(42,'Somatório', vida, ataque, 'assets/shomatorio.svg', descricao, 'feitiço', 'cálculo')

class Struct(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(43,'Struct', vida, ataque, 'assets/struct.svg', descricao, 'tropa', 'programação')

class SubstituicaoTrigonometrica(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(44,'Subs Trigonométrica', vida, ataque, 'assets/subtrig.svg', descricao, 'tropa', 'cálculo')

class Switch(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(45,'Switch', vida, ataque, 'assets/switch.svg', descricao, 'tropa', 'redes')

class Ttl(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(46,'TTL', vida, ataque, 'assets/ttl.svg', descricao, 'feitiço', 'redes')

class Xor(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(47,'Xor', vida, ataque, 'assets/xor.svg', descricao, 'tropa', 'Circuitos')

class TeoremaConfronto(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(48,'Teorema do confronto', vida, ataque, 'assets/confronto.svg', descricao, 'feitiço', 'cálculo')

class SwitchCode(Card):
    def __init__(self, vida, ataque, descricao):
        super().__init__(48,'Código Switch', vida, ataque, 'assets/switchC.svg', descricao, 'equipamento', 'programação')


and_carta = And(10, 5, "A porta lógica AND é muito forte e tal tal tal")
arp_carta = Arp(8, 4, "Ataque de ARP spoofing")
arvore_b_carta = ArvoreB(12, 7, "Árvore B para organização de dados")
arvore_rb_carta = ArvoreRB(14, 9, "Árvore Vermelho-Preto equilibrada")
bombe_carta = Bombe(10, 6, "Máquina Bombe para decifrar códigos")
break_carta = Break(6, 3, "Interrompe o fluxo de execução")
bug_carta = Bug(8, 5, "Um erro inesperado no código")
capacitor_carta = Capacitor(6, 2, "Armazena energia em circuitos")
clockpulse_carta = Clockpulse(7, 3, "Impulsos de clock em circuitos")
constante_carta = Constante(9, 2, "Valor constante em programação")
continue_carta = Continue(5, 3, "Continua o fluxo de execução")
ddos_attack_carta = DdosAttack(10, 7, "Ataque de negação de serviço distribuído")
derivada_carta = Derivada(11, 6, "Derivada de uma função matemática")
dijkstra_carta = Dijkstra(14, 8, "Algoritmo de caminho mínimo")
do_while_carta = DoWhile(7, 4, "Loop do-while em programação")
espaco_vetorial_carta = EspacoVetorial(9, 5, "Espaço vetorial em álgebra linear")
fila_carta = Fila(6, 2, "Estrutura de dados do tipo fila")
firewall_carta = Firewall(10, 6, "Barreira de proteção em redes")
flipflop_carta = FlipFlop(7, 4, "Elemento de armazenamento em circuitos")
getway_carta = Getway(8, 5, "Dispositivo de comunicação em redes")
grafo_ponderado_carta = GrafoPonderado(12, 7, "Grafo com pesos nas arestas")
grafo_fonte_carta = GrafoFonte(11, 6, "Grafo com um único vértice de origem")
grafo_sumidouro_carta = GrafoSumidouro(11, 6, "Grafo com um único vértice de destino")
heap_maximo_carta = HeapMaximo(10, 7, "Heap máximo para gerenciamento de prioridades")
hub_carta = Hub(8, 4, "Dispositivo concentrador de redes")
integracao_partes_carta = IntegracaoPartes(11, 6, "Método de integração por partes")
integral_carta = Integral(10, 5, "Cálculo integral")
karnaugh_carta = Karnaugh(12, 8, "Mapa de Karnaugh para simplificação de circuitos")
multiplexador_carta = Multiplexador(9, 5, "Dispositivo de multiplexação de sinais")
nabla_carta = Nabla(10, 6, "Operador nabla em cálculo vetorial")
not_carta = Not(6, 3, "Porta lógica NOT")
or_carta = Or(7, 4, "Porta lógica OR")
pilha_carta = Pilha(9, 5, "Estrutura de dados do tipo pilha")
ponteiro_carta = Ponteiro(8, 4, "Referência a um endereço de memória")
registrador_carta = Registrador(10, 6, "Armazenamento temporário em circuitos")
regra_cadeia_carta = RegraCadeia(11, 6, "Regra da cadeia em cálculo diferencial")
repetidor_carta = Repetidor(8, 4, "Dispositivo de amplificação de sinais de rede")
return_carta = Return(7, 3, "Instrução de retorno em programação")
riemann_carta = Riemann(12, 7, "Soma de Riemann para cálculo de integrais")
roteador_carta = Roteador(10, 5, "Dispositivo de roteamento de redes")
sniffer_carta = Sniffer(9, 5, "Captura de pacotes de rede")
somatorio_carta = Somatorio(11, 6, "Soma de uma série numérica")
struct_carta = Struct(9, 5, "Estrutura de dados em programação")
substituicao_trigonometrica_carta = SubstituicaoTrigonometrica(11, 6, "Substituição trigonométrica em cálculo")
switch_carta = Switch(8, 4, "Dispositivo de comutação em redes")
ttl_carta = Ttl(7, 4, "Tempo de vida em pacotes de rede")
xor_carta = Xor(7, 4, "Porta lógica XOR")
teorema_confronto_carta = TeoremaConfronto(12, 7, "Teorema do confronto em cálculo")
switch_code_carta = SwitchCode(10, 5, "Código Switch para controle de fluxo")

cartas_existentes = [
    and_carta, arp_carta, arvore_b_carta, arvore_rb_carta, bombe_carta, break_carta, bug_carta, 
    capacitor_carta, clockpulse_carta, constante_carta, continue_carta, ddos_attack_carta, derivada_carta, 
    dijkstra_carta, do_while_carta, espaco_vetorial_carta, fila_carta, firewall_carta, flipflop_carta, 
    getway_carta, grafo_ponderado_carta, grafo_fonte_carta, grafo_sumidouro_carta, heap_maximo_carta, 
    hub_carta, integracao_partes_carta, integral_carta, karnaugh_carta, multiplexador_carta, nabla_carta, 
    not_carta, or_carta, pilha_carta, ponteiro_carta, registrador_carta, regra_cadeia_carta, repetidor_carta, 
    return_carta, riemann_carta, roteador_carta, sniffer_carta, somatorio_carta, struct_carta, 
    substituicao_trigonometrica_carta, switch_carta, ttl_carta, xor_carta, teorema_confronto_carta, switch_code_carta
]