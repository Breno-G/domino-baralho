from carta import Naipe, Valores, Carta

class Jogador:
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
        while True:
            try:
                print("\nDigite 0 para passar a vez.")
                print("Escolha o naipe:")
                for idx, naipe in enumerate(Naipe):
                    print(f"{idx+1} - {naipe.name}")
                escolha = int(input("Naipe: "))
    
                if escolha == 0:
                    print(f"{self.nome} passou a vez.")
                    return  # passa o turno
    
                if not 1 <= escolha <= 4:
                    print("Escolha inválida. Tente novamente.")
                    continue
                
                naipe_escolhido = list(Naipe)[escolha - 1]
    
                valor = int(input("Valor da carta (1-13): "))
                if not 1 <= valor <= 13:
                    print("Valor inválido.")
                    continue
                
                valor_enum = Valores(valor)
                carta = Carta(valor_enum, naipe_escolhido)
    
                if carta not in self.mao:
                    print("Você não tem essa carta.")
                    continue
                
                pilha = mesa.pilhas[naipe_escolhido]
                if pilha['central'] is None and valor != 7:
                    print("Você deve jogar o 7 primeiro nesse naipe.")
                    continue
                
                if mesa.jogar_carta(carta):
                    self.mao.remove(carta)
                    self.organizar_mao()
                    return  # jogou com sucesso
                else:
                    print("Jogada inválida.")
            except Exception:
                print("Entrada inválida. Tente novamente.")
    
    
