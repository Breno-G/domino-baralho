from carta import Carta, Naipe, Valores  # seus Enums
from print_card_copy  import imprime_espaco_vazio

NAIPES = list(Naipe)
VALORES = list(Valores)

baralho = [Carta(valor, naipe) for naipe in NAIPES for valor in VALORES]

carta = Carta(Valores.AS, Naipe.OUROS)
imprime_espaco_vazio(carta)


