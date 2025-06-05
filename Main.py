from setup_game import Baralho, Jogador, Valores, Mesa
from carta import Carta, Naipe
from print_card import imprime_mesa_completa, imprime_mao_jogador

class Jogo:
    def __init__(self):
        self.baralho = Baralho()
        self.jogadores = [
            Jogador("Você"),
            Jogador("Bot 1"),
            Jogador("Bot 2"),
            Jogador("Bot 3")
        ]
        self.mesa = Mesa()

    def iniciar(self):
        self.baralho.embaralhar()
        maos = self.baralho.distribuir()

        for i, jogador in enumerate(self.jogadores):
            jogador.receber_cartas(maos[i])
            jogador.mostrar_mao()

        # Exibir estado inicial da mesa
        from print_card import imprime_mesa_completa
        print("\nEstado inicial da mesa (vazio):")
        imprime_mesa_completa(self.mesa)

        # Jogar 7 de Copas
        carta = Carta(Valores.SETE, Naipe.COPAS)
        self.mesa.jogar_carta(carta)
        print(f"\n{carta.valor.name} de {carta.naipe.value} foi jogado na mesa.")
        imprime_mesa_completa(self.mesa)

        # Após mostrar as mãos
        print("\nEstado inicial da mesa (vazio):")
        imprime_mesa_completa(self.mesa)

        # Exemplo: Jogador joga 7 de Copas
        carta = Carta(Valores.SETE, Naipe.COPAS)
        self.mesa.jogar_carta(carta)
        print(f"\n{carta.valor.name} de {carta.naipe.value} foi jogado na mesa.")
        imprime_mesa_completa(self.mesa)

        

        # Mostrar a mão do jogador humano
        print("Sua mão:")
        imprime_mao_jogador(self.jogadores[0].mao)

    # (No futuro podemos adicionar lógica de turno com threads aqui)
if __name__ == "__main__":
    jogo = Jogo()
    jogo.iniciar()

