from carta import Carta, Valores, Naipe

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

#REFATORAR CÓDIGO
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

def imprime_pilha_empilhada(pilha_exemplo: list[Carta]):
    pilha_acima_7 = [c for c in pilha_exemplo if c.valor.value > 7]
    carta_7 = next(c for c in pilha_exemplo if c.valor == Valores.SETE)
    pilha_abaixo_7 = [c for c in pilha_exemplo if c.valor.value < 7]

    for i, carta in enumerate(pilha_acima_7):
        imprime_superior_carta()
        imprime_simbolos_superior(carta)

    imprime_carta_inteira(carta_7)
            
    for i, carta in enumerate(pilha_abaixo_7):
       
        imprime_simbolos_superior(carta)
        imprime_inferior_carta()
    

