import threading
from .carta import Valores, Carta
from .visual import cor_do_naipe, RESET, limpar_tela, imprime_estado
from .entidades import ORDEM_NAIPE

class TimeoutInput:
    def __init__(self, prompt, timeout=30):
        self.prompt = prompt
        self.timeout = timeout
        self.result = None

    def _input_thread(self):
        try:
            self.result = input(self.prompt)
        except EOFError:
            self.result = None

    def get_input(self):
        thread = threading.Thread(target=self._input_thread)
        thread.daemon = True
        thread.start()
        thread.join(self.timeout)
        if thread.is_alive():
            # Timeout ocorreu
            return None
        return self.result

class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.mao = []

    def receber_cartas(self, cartas):
        self.mao.extend(cartas)
        self.organizar_mao()

    def organizar_mao(self):
        self.mao.sort(key=lambda carta: (ORDEM_NAIPE.index(carta.naipe), -carta.valor.value))

    def tem_jogada_valida(self, mesa):
        for carta in self.mao:
            pilha = mesa.pilhas[carta.naipe]
            centro = pilha['central']

            if centro is None:
                if carta.valor.value == 7:
                    return True
            else:
                menor = pilha.get('menor', 7)
                maior = pilha.get('maior', 7)
                if carta.valor.value == menor - 1 or carta.valor.value == maior + 1:
                    return True
        return False

    def jogar(self, mesa, jogo, bots):
        while True:
            try:
                limpar_tela()
                imprime_estado(mesa, self, bots)
                opcoes = []
                print("\nDigite 0 para passar a vez (se não tiver jogada válida).")
                for idx, naipe in enumerate(ORDEM_NAIPE):
                    cor = cor_do_naipe(naipe)
                    opcao = f"{idx+1} {cor}{naipe.value}{RESET} {naipe.name} {cor}{naipe.value}{RESET}"
                    opcoes.append(opcao)

                print(" | ".join(opcoes))

                escolha_input = TimeoutInput("Naipe: ", timeout=30).get_input()
                if escolha_input is None:
                    print(f"\n{self.nome} demorou demais! Passando a vez...")
                    return None  # Timeout: passa a vez

                escolha = int(escolha_input)

                if escolha == 99:
                    print("⚠ Debug: Forçando fim de jogo manualmente.")
                    self.mao.clear()
                    return None

                if escolha == 0:
                    if self.tem_jogada_valida(mesa):
                        raise ValueError("Você tem jogadas possíveis! Não pode passar a vez.")
                    print(f"{self.nome} passou a vez.")
                    return None

                if not 1 <= escolha <= 4:
                    raise ValueError("Escolha de naipe inválida.")

                naipe_escolhido = ORDEM_NAIPE[escolha - 1]

                valor_input = TimeoutInput("Valor da carta (1-13): ", timeout=30).get_input()
                if valor_input is None:
                    print(f"\n{self.nome} demorou demais! Passando a vez...")
                    return None  # Timeout: passa a vez

                valor = int(valor_input)

                if not 1 <= valor <= 13:
                    raise ValueError("Valor da carta inválido.")

                valor_enum = Valores(valor)
                carta = Carta(valor_enum, naipe_escolhido)

                if carta not in self.mao:
                    raise ValueError("Você não tem essa carta.")

                pilha = mesa.pilhas[naipe_escolhido]
                centro = pilha['central']

                if centro is None and valor != 7:
                    raise ValueError("Você deve começar com o 7 nesse naipe.")

                menor = pilha.get('menor', 7)
                maior = pilha.get('maior', 7)

                if centro is not None and not (valor == menor - 1 or valor == maior + 1):
                    raise ValueError("Você só pode jogar o número abaixo do menor ou acima do maior na pilha.")

                if mesa.jogar_carta(carta):
                    self.mao.remove(carta)
                    self.organizar_mao()
                    jogo.verificar_fim_de_jogo()
                    return carta
                else:
                    raise ValueError("Jogada inválida.")

            except Exception as e:
                print(f"\nErro: {e}")
                input("\nPressione Enter para tentar novamente...")
