# print_card.py

class Carta:
    def __init__(self, valor, naipe):
        self.valor = valor
        self.naipe = naipe

    def __str__(self):
        return f"{self.valor}{self.naipe}"

def imprimir_mao(mao):
    for carta in mao:
        print(str(carta), end=' ')
    print()