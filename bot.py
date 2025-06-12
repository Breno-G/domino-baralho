from carta import Naipe, Valores, Carta

class Bot:
    def __init__(self, nome):
        self.nome = nome
        self.mao = []

    def receber_cartas(self, cartas):
        self.mao.extend(cartas)
        self.organizar_mao()

    def organizar_mao(self):
        ordem_naipe = [Naipe.ESPADAS, Naipe.COPAS, Naipe.PAUS, Naipe.OUROS]
        self.mao.sort(key=lambda carta: (ordem_naipe.index(carta.naipe), -carta.valor.value))

    def jogar(self, mesa):
        for carta in self.mao:
            if mesa.jogar_carta(carta):
                self.mao.remove(carta)
                self.organizar_mao()
                return
