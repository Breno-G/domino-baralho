class Carta:
    def __init__(self, valor: int, naipe: str, visivel: bool = True):
        self.valor = valor
        self.naipe = naipe
        self.visivel = visivel

    def get_valor_str(self):
        mapa = {1: 'A', 11: 'J', 12: 'Q', 13: 'K'}
        return mapa.get(self.valor, str(self.valor))

    def render_top(self):
        if not self.visivel:
            return "│ ∷∷∷∷∷∷∷ │"
        v = self.get_valor_str()
        n = self.naipe
        return f"│{v:<2}     {n}│"

    def render_middle(self):
        if not self.visivel:
            return "│ ∷∷∷∷∷∷∷ │"
        return f"│    {self.naipe}    │"

    def render_bottom(self):
        if not self.visivel:
            return "│ ∷∷∷∷∷∷∷ │"
        v = self.get_valor_str()
        n = self.naipe
        return f"│{n}     {v:>2}│"

    def render_outline_top(self):
        return "╭─────────╮"

    def render_outline_bottom(self):
        return "╰─────────╯"

    def render_empty(self):
        return "│         │"

    def render_horizontal(self):
        """Retorna uma string horizontal para uso no centro da mesa."""
        v = self.get_valor_str()
        return f"[{v}{self.naipe}]"

    def render_back(self):
        """Verso da carta (não visível)"""
        return [
            "╭─────────╮",
            "│ ∷∷∷∷∷∷∷ │",
            "│ ∷∷∷∷∷∷∷ │",
            "│ ∷∷∷∷∷∷∷ │",
            "╰─────────╯"
        ]
def imprimir_mao(cartas):
    linhas = ["", "", "", "", ""]  # 5 linhas para cada parte

    for i, carta in enumerate(cartas):
        v = carta.get_valor_str()
        n = carta.naipe

        if i < len(cartas) - 1:
            # Parcial (cartas intermediárias)
            linhas[0] += "╭──── "
            linhas[1] += f"│{v:<2}  │"
            linhas[2] += "│    │"
            linhas[3] += f"│{n:<2}  │"
            linhas[4] += "╰──── "
        else:
            # Última carta: completa
            linhas[0] += carta.render_outline_top()
            linhas[1] += carta.render_top()
            linhas[2] += carta.render_middle()
            linhas[3] += carta.render_bottom()
            linhas[4] += carta.render_outline_bottom()

    print("\n".join(linhas))
