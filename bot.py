from carta import Naipe, Valores, Carta

class Bot:
    def __init__(self, nome):
        self.nome = nome
        self.mao = []

    def receber_cartas(self, cartas):
        self.mao.extend(cartas)
        

    def jogar(self, mesa):
        for carta in self.mao:
            if mesa.jogar_carta(carta):
                self.mao.remove(carta)
                return
