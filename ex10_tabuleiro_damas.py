class Tabuleiro:
    def __init__(self):
        self.tamanho = 8
        self.tabuleiro = [[' ' for _ in range(self.tamanho)] for _ in range(self.tamanho)]

        # Coloca 12 brancas nas 3 primeiras linhas (0,1,2) nas casas "escuras"
        for linha in range(3):
            for col in range(self.tamanho):
                if self._casa_escura(linha, col):
                    self.tabuleiro[linha][col] = 'B'

        # Coloca 12 pretas nas 3 últimas linhas (5,6,7) nas casas "escuras"
        for linha in range(5, 8):
            for col in range(self.tamanho):
                if self._casa_escura(linha, col):
                    self.tabuleiro[linha][col] = 'P'

        self.pecas_brancas = 12
        self.pecas_pretas = 12

    def _casa_escura(self, linha: int, col: int) -> bool:
        # Em tabuleiro xadrez, casas escuras alternam. Usamos (linha+col) ímpar.
        return (linha + col) % 2 == 1

    def _dentro(self, linha: int, col: int) -> bool:
        return 0 <= linha < self.tamanho and 0 <= col < self.tamanho

    def exibir_tabuleiro(self):
        letras = "ABCDEFGH"
        print("    " + "   ".join(letras))
        print("  +" + "---+" * self.tamanho)

        for i in range(self.tamanho):
            linha_str = f"{i} |"
            for j in range(self.tamanho):
                linha_str += f" {self.tabuleiro[i][j]} |"
            print(linha_str)
            print("  +" + "---+" * self.tamanho)

    def mover_peca(self, cor: str, linha_origem: int, col_origem: int, linha_dest: int, col_dest: int) -> bool:
        if cor not in ('B', 'P'):
            return False
        if not (self._dentro(linha_origem, col_origem) and self._dentro(linha_dest, col_dest)):
            return False

        if self.tabuleiro[linha_origem][col_origem] != cor:
            return False

        if self.tabuleiro[linha_dest][col_dest] != ' ':
            return False

        dl = linha_dest - linha_origem
        dc = col_dest - col_origem

        # movimento diagonal simples: 1 casa
        if abs(dl) != 1 or abs(dc) != 1:
            return False

        self.tabuleiro[linha_dest][col_dest] = cor
        self.tabuleiro[linha_origem][col_origem] = ' '
        return True

    def capturar_peca(self, cor: str, linha_origem: int, col_origem: int, linha_dest: int, col_dest: int) -> bool:
        if cor not in ('B', 'P'):
            return False
        if not (self._dentro(linha_origem, col_origem) and self._dentro(linha_dest, col_dest)):
            return False

        if self.tabuleiro[linha_origem][col_origem] != cor:
            return False

        if self.tabuleiro[linha_dest][col_dest] != ' ':
            return False

        dl = linha_dest - linha_origem
        dc = col_dest - col_origem

        # captura: 2 casas na diagonal
        if abs(dl) != 2 or abs(dc) != 2:
            return False

        linha_meio = linha_origem + (dl // 2)
        col_meio = col_origem + (dc // 2)

        adversaria = 'P' if cor == 'B' else 'B'
        if self.tabuleiro[linha_meio][col_meio] != adversaria:
            return False

        # Faz a captura
        self.tabuleiro[linha_dest][col_dest] = cor
        self.tabuleiro[linha_origem][col_origem] = ' '
        self.tabuleiro[linha_meio][col_meio] = ' '

        if adversaria == 'P':
            self.pecas_pretas -= 1
        else:
            self.pecas_brancas -= 1

        return True

    def verificar_vitoria(self):
        if self.pecas_pretas == 0:
            return 'brancas'
        if self.pecas_brancas == 0:
            return 'pretas'
        return None

    def listar_movimentos_possiveis(self, cor: str, linha: int, coluna: int):
        if cor not in ('B', 'P'):
            return []
        if not self._dentro(linha, coluna):
            return []
        if self.tabuleiro[linha][coluna] != cor:
            return []

        movimentos = []
        # diagonais possíveis (simples)
        for dl, dc in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            nl, nc = linha + dl, coluna + dc
            if self._dentro(nl, nc) and self.tabuleiro[nl][nc] == ' ':
                movimentos.append((nl, nc))

        # capturas possíveis (2 casas)
        adversaria = 'P' if cor == 'B' else 'B'
        for dl, dc in [(-2, -2), (-2, 2), (2, -2), (2, 2)]:
            nl, nc = linha + dl, coluna + dc
            ml, mc = linha + (dl // 2), coluna + (dc // 2)
            if self._dentro(nl, nc) and self.tabuleiro[nl][nc] == ' ':
                if self._dentro(ml, mc) and self.tabuleiro[ml][mc] == adversaria:
                    movimentos.append((nl, nc))

        return movimentos


if __name__ == "__main__":
    tab = Tabuleiro()
    print(f"Brancas: {tab.pecas_brancas}, Pretas: {tab.pecas_pretas}")
    tab.exibir_tabuleiro()

    resultado = tab.mover_peca('B', 2, 1, 3, 2)
    print("Mover (esperado True):", resultado)

    resultado = tab.mover_peca('B', 3, 2, 3, 4)
    print("Mover inválido (esperado False):", resultado)

    # preparar captura conforme enunciado
    tab.tabuleiro[4][3] = 'P'
    resultado = tab.capturar_peca('B', 3, 2, 5, 4)
    print("Capturar (esperado True):", resultado)

    tab.pecas_pretas = 0
    print("Vitória (esperado 'brancas'):", tab.verificar_vitoria())
