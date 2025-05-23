from enum import Enum

## ---- Criação das cartas ----
class Cores(Enum):
    RED = "\033[31m"
    RESET = "\033[0m"

class Naipe(Enum):
    COPAS = '♥'
    OUROS = '♦'
    ESPADAS = '♠'
    PAUS = '♣'
    
    @classmethod
    def from_index(cls, i):
        return list(cls)[i]
    
class Valores(Enum):
    AS = 1
    DOIS = 2
    TRES = 3
    QUATRO = 4
    CINCO = 5
    SEIS = 6 
    SETE = 7
    OITO = 8
    NOVE = 9
    DEZ = 10
    VALETE = 11
    DAMA = 12
    REI = 13    

    @classmethod
    def from_index(cls, i):
        return list(cls)[i]
    
class Carta:
    def __init__(self, valor, naipe, visivel = True):
        self.valor = valor
        self.naipe = naipe
        self.visivel = visivel
    def __repr__(self):
        return f"{self.valor.name}{self.naipe.value}"

##class Carta(self, valor, naipe, visivel = True):
  ##  self.valor = valor
   ## self.naipe = naipe
   ## self.visivel = visivel

