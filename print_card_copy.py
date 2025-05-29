from carta import Carta

def imprime_superio_carta():
    print("╭─────────╮" )
    
def imprime_meio_carta(carta: Carta):
    if carta.visivel:
        print("|         |")
    else:
        print("| ::::::: |")

def imprime_fundo_carta():
    print("╰─────────╯ ")
    
def imprime_espacos_vazios():
    topo =     ["╭─  ╭─  ──  ──  ─╮"] * 4
    vazio1 =   ["|               |"] * 4
    numeros =  [f"{i+1}     │               │" for i in range(4)]
    vazio2 =   ["|               |"] * 4
    base =     ["╰─  ╰─  ──  ──  ─╯"] * 4

    # Junta lado a lado com dois espaços entre cada "coluna"
    for linha in zip(topo, vazio1, numeros, vazio2, base):
        print("   ".join(linha))
    
def imprime_vazio():
    print("            ")
    
def imprime_simbolos_superior(carta: Carta):
    if carta.visivel:
        valor = carta.valor_str() 
        print(f"│{valor:>2}     {carta.naipe.value:<2}│")
    else:
        imprime_meio_carta(carta)

def imprime_simbolos_intermediario(carta: Carta):
    if carta.visivel:
        print(f"│    {carta.naipe.value}    │")
    else:
        imprime_meio_carta(carta)

def imprime_simbolos_inferior(carta: Carta):
    if carta.visivel:
        valor = carta.valor_str() 
        print(f"│{carta.naipe.value:>2}     {valor:<2}│")
    else:
        imprime_meio_carta(carta)

def imprime_simbolos_lateral():
    print("╭──")
