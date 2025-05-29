import random
from enum import Enum

# Enumeração para os naipes
class Naipe(Enum):
    PAUS = '♣'
    OUROS = '♦'
    COPAS = '♥'
    ESPADAS = '♠'

# Classe que representa uma carta
class Carta:
    def __init__(self, valor: int, naipe: Naipe):
        self.valor = valor
        self.naipe = naipe

    def __repr__(self):
        nomes = {1: 'A', 11: 'J', 12: 'Q', 13: 'K'}
        valor_str = nomes.get(self.valor, str(self.valor))
        return f"{valor_str}{self.naipe.value}"

# Classe que representa o estado geral do jogo
class EstadoDoJogo:
    def __init__(self):
        self.baralho = []
        self.jogadores = [[] for _ in range(4)]  # 4 jogadores

    def gerar_baralho(self):
        """Cria um baralho completo com 52 cartas (1 a 13 de cada naipe)."""
        self.baralho = [Carta(valor, naipe) for naipe in Naipe for valor in range(1, 14)]

    def embaralhar_baralho(self):
        """Embaralha o baralho aleatoriamente."""
        random.shuffle(self.baralho)

    def distribuir_cartas(self):
        """Distribui 13 cartas para cada jogador."""
        for _ in range(13):
            for jogador in self.jogadores:
                carta = self.baralho.pop()
                jogador.append(carta)

    def mostrar_maos(self):
        for i, mao in enumerate(self.jogadores):
            print(f"Jogador {i+1}: {mao}")
