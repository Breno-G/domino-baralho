from carta import Carta, Valores, Naipe
from setup_game import Mesa 

# Cores das cartas
RED = "\033[31m"
RESET = "\033[0m"

def cor_do_naipe(naipe):
    return RED if naipe in [Naipe.COPAS, Naipe.OUROS] else ""

def imprime_superior_carta():
    print("╭─────────╮" )
    
def imprime_meio_carta(carta: Carta):
    if carta.visivel:
        print("│         │")
    else:
        print("│ ::::::: │")

def imprime_inferior_carta():
    print("╰─────────╯ ")

def imprime_carta_inteira(carta: Carta):
    imprime_superior_carta()
    imprime_simbolos_superior(carta)
    imprime_meio_carta(carta)
    imprime_simbolos_intermediario(carta)
    imprime_meio_carta(carta)
    imprime_simbolos_inferior(carta)
    imprime_inferior_carta()

#MODIFICAR ESSE CÓDIGO
def imprime_espacos_vazios():
   
    espacos = [
        [       
            f"\033[31m╭─\033[0m╭─  ───  ─╮",
            f"\033[31m│\033[0m            ",
            f"\033[31m│\033[0m │         │",
            f"\033[0m{i+1}            ",
            f"\033[31m│\033[0m │         │",
            f"\033[31m│\033[0m            ",
            f"\033[31m╰─\033[0m╰─  ───  ─╯"
        ]
        for i in range(4)
    ]

    for linha in range(7):  # 5 linhas por espaço
        print("     ".join(espaco[linha] for espaco in espacos))

def imprime_carta_central():
    imprime_carta_inteira()


def imprime_vazio():
    print("            ")
    
def imprime_simbolos_superior(carta: Carta):
    if carta.visivel:
        valor = carta.valor_str() 
        cor = cor_do_naipe(carta.naipe)
        print(f"│{cor}{valor:>2}     {carta.naipe.value:<2}{RESET}│")
    else:
        imprime_meio_carta(carta)

def imprime_simbolos_intermediario(carta: Carta):
    if carta.visivel:
        cor = cor_do_naipe(carta.naipe)
        print(f"│    {cor}{carta.naipe.value}{RESET}    │")
    else:
        imprime_meio_carta(carta)

def imprime_simbolos_inferior(carta: Carta):
    if carta.visivel:
        valor = carta.valor_str() 
        cor = cor_do_naipe(carta.naipe)
        print(f"│{cor}{carta.naipe.value:>2}     {valor:<2}{RESET}│")
    else:
        imprime_meio_carta(carta)

def imprime_simbolos_lateral():
    print("╭──")

def imprime_pilha_dinamica(pilha_info: dict):
    """
    Imprime uma pilha completa (acima, central, abaixo) com base na estrutura da Mesa.
    Espera um dicionário com as chaves: 'acima', 'abaixo' e 'central'.
    """
    # Parte de cima (cartas acima do 7 — 8 até K)
    for carta in pilha_info['acima']:
        imprime_superior_carta()
        imprime_simbolos_superior(carta)

    # Central (o 7)
    if pilha_info['central']:
        imprime_carta_inteira(pilha_info['central'])
    else:
        imprime_vazio()

    # Parte de baixo (cartas abaixo do 7 — 6 até A)
    for i, carta in enumerate(pilha_info['abaixo']):
        imprime_simbolos_superior(carta)
        imprime_inferior_carta()


def imprime_mesa_completa(mesa: Mesa):
    """Imprime as quatro pilhas da mesa: Copas, Ouros, Espadas e Paus."""
    print("\n================ MESA =================\n")
    for naipe in Naipe:
        print(f"\n--- Pilha de {naipe.value} ---")
        pilha_info = mesa.pilhas[naipe]
        imprime_pilha_dinamica(pilha_info)
    print("\n=======================================\n")

    def imprime_mao_jogador(mao: list[Carta]):
        """Imprime a mão do jogador horizontalmente, com todas as cartas visíveis."""
        # Ordenar por naipe (♥, ♦, ♣, ♠) e valor decrescente
        ordem_naipe = [Naipe.COPAS, Naipe.OUROS, Naipe.PAUS, Naipe.ESPADAS]
        mao.sort(key=lambda c: (ordem_naipe.index(c.naipe), -c.valor.value))

        # Garantir visibilidade das cartas
        for carta in mao:
            carta.visivel = True

        # Linhas de cada carta
        linhas_cartas = [[] for _ in range(6)]

        for carta in mao:
            cor = cor_do_naipe(carta.naipe)
            reset = RESET
            valor_str = carta.valor_str()
            naipe_str = carta.naipe.value

            linhas_cartas[0].append("╭─────────╮")
            linhas_cartas[1].append(f"│{cor}{valor_str:<2}       {reset}│")
            linhas_cartas[2].append(f"│         │")
            linhas_cartas[3].append(f"│    {cor}{naipe_str}{reset}    │")
            linhas_cartas[4].append(f"│         │")
            linhas_cartas[5].append(f"╰─────────╯")

        # Imprimir linha por linha
        for linha in linhas_cartas:
            print(" ".join(linha))

