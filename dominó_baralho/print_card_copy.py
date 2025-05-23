from carta import Carta

def imprime_superio_carta(carta: Carta):
    print("╭─────────╮" )
    
def imprime_meio_carta(carta: Carta):
    if carta.visivel:
        print("|         |")
    else:
        print("| ::::::: |")

def imprime_fundo_carta():
    print("╰─────────╯ ")
    
def imprime_espaco_vazio(carta: Carta):
    print("╭─  ──  ──  ─╮")
    print("              ")
    print("│            │")
    print("              ")
    print("╰─  ──  ──  ─╯")