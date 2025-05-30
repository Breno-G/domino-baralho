from carta import Carta, Naipe, Valores  # seus Enums
from print_card_copy  import imprime_espacos_vazios
from print_card_copy import imprime_carta_inteira
from print_card_copy import imprime_pilha_empilhada

NAIPES = list(Naipe)
VALORES = list(Valores)

baralho = [Carta(valor, naipe) for naipe in NAIPES for valor in VALORES]

carta = Carta(Valores.AS, Naipe.OUROS)
#imprime_espacos_vazios()
#imprime_carta_inteira(carta)

pilha_exemplo = [Carta(valor, Naipe.ESPADAS) for valor in reversed(Valores)]

imprime_pilha_empilhada(pilha_exemplo)
        
        
