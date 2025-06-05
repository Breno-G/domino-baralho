import random
from typing import List
from carta import Carta, Naipe, Valores

class Baralho:
    def __init__(self):
        """Inicializa o baralho com as 52 cartas padrão."""
        self.cartas = [Carta(valor, naipe) for naipe in Naipe for valor in Valores]

    def embaralhar(self):
        """Embaralha o baralho."""
        random.shuffle(self.cartas)

    def distribuir(self, jogadores: int = 4) -> list[list[Carta]]:
        """Distribui o baralho igualmente entre os jogadores."""
        if len(self.cartas) % jogadores != 0:
            raise ValueError("Não é possível dividir igualmente entre os jogadores.")
        
        tamanho_mao = len(self.cartas) // jogadores
        return [self.cartas[i * tamanho_mao:(i + 1) * tamanho_mao] for i in range(jogadores)]

class Jogador:
    def __init__(self, nome: str):
        """Cria um jogador com nome e mão vazia."""
        self.nome = nome
        self.mao: List[Carta] = []

    def receber_cartas(self, cartas: List[Carta]):
        """Adiciona uma lista de cartas à mão do jogador."""
        self.mao.extend(cartas)

    def mostrar_mao(self):
        """Mostra todas as cartas da mão do jogador."""
        print(f"\nCartas de {self.nome}:")
        for carta in self.mao:
            print(carta)


class Mesa:
    def __init__(self):
        """Inicializa as pilhas para cada naipe."""
        self.pilhas = {
            naipe: {'acima': [], 'abaixo': [], 'central': None}
            for naipe in Naipe
        }

    def jogar_carta(self, carta: Carta) -> bool:
        """
        Tenta adicionar uma carta na mesa.
        Retorna True se a carta foi colocada com sucesso, False caso contrário.
        """
        pilha = self.pilhas[carta.naipe]

        if carta.valor == Valores.SETE:
            if pilha['central'] is None:
                pilha['central'] = carta
                return True
            return False  # já tem o 7

        if pilha['central'] is None:
            return False  # precisa jogar o 7 antes

        if carta.valor.value > 7:
            topo = pilha['acima'][0].valor.value if pilha['acima'] else 7
            if carta.valor.value == topo + 1:
                pilha['acima'].insert(0, carta)
                return True
        elif carta.valor.value < 7:
            fundo = pilha['abaixo'][-1].valor.value if pilha['abaixo'] else 7
            if carta.valor.value == fundo - 1:
                pilha['abaixo'].append(carta)
                return True

        return False  # carta fora da sequência

    def mostrar_pilha(self, naipe: Naipe):
        """Mostra uma pilha específica (apenas para testes)."""
        pilha = self.pilhas[naipe]
        print(f"\nPilha de {naipe.value}:")
        for carta in pilha['acima']:
            print(f"{carta.valor.name} {carta.naipe.value}")
        if pilha['central']:
            print(f"[7 {pilha['central'].naipe.value}]")
        for carta in pilha['abaixo']:
            print(f"{carta.valor.name} {carta.naipe.value}")
