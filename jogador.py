from carta import Naipe, Valores, Carta
from visual import cor_do_naipe, RESET
from setup_game import ORDEM_NAIPE



class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.mao = [] 

    def receber_cartas(self, cartas):
        self.mao.extend(cartas)
        self.organizar_mao()

    def organizar_mao(self):
        self.mao.sort(key=lambda carta: (ORDEM_NAIPE.index(carta.naipe), -carta.valor.value))

    def jogar(self, mesa):
        while True:
            try:
                opcoes = []
                print("\nDigite 0 para passar a vez.")
                for idx, naipe in enumerate(ORDEM_NAIPE):
                    cor = cor_do_naipe(naipe)
                    opcao = f"{idx+1} {cor}{naipe.value}{RESET} {naipe.name} {cor}{naipe.value}{RESET} "
                    opcoes.append(opcao)

                print(" | ".join(opcoes))  # <-- agora exibe ANTES de pedir a entrada

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
    
    
