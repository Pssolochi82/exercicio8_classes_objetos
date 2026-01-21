import unittest
from ex10_tabuleiro_damas import Tabuleiro


class TestTabuleiroDamas(unittest.TestCase):

    def test_init_contadores(self):
        tab = Tabuleiro()
        self.assertEqual(tab.pecas_brancas, 12)
        self.assertEqual(tab.pecas_pretas, 12)

    def test_mover_peca_valido(self):
        tab = Tabuleiro()
        ok = tab.mover_peca('B', 2, 1, 3, 2)
        self.assertTrue(ok)
        self.assertEqual(tab.tabuleiro[2][1], ' ')
        self.assertEqual(tab.tabuleiro[3][2], 'B')

    def test_mover_invalido_nao_diagonal(self):
        tab = Tabuleiro()
        tab.mover_peca('B', 2, 1, 3, 2)
        ok = tab.mover_peca('B', 3, 2, 3, 4)
        self.assertFalse(ok)

    def test_capturar_peca(self):
        tab = Tabuleiro()
        tab.mover_peca('B', 2, 1, 3, 2)

        # garante que a peça a capturar está no meio
        tab.tabuleiro[4][3] = 'P'

        # (5,4) no tabuleiro inicial pode estar ocupado por 'P'
        # então limpamos a casa de destino para o teste bater com o enunciado
        if tab.tabuleiro[5][4] == 'P':
            tab.tabuleiro[5][4] = ' '
            tab.pecas_pretas -= 1  # mantém o contador consistente

        pretas_antes = tab.pecas_pretas
        ok = tab.capturar_peca('B', 3, 2, 5, 4)

        self.assertTrue(ok)
        self.assertEqual(tab.tabuleiro[4][3], ' ')
        self.assertEqual(tab.tabuleiro[5][4], 'B')
        self.assertEqual(tab.pecas_pretas, pretas_antes - 1)

    def test_verificar_vitoria(self):
        tab = Tabuleiro()
        tab.pecas_pretas = 0
        self.assertEqual(tab.verificar_vitoria(), 'brancas')

    def test_listar_movimentos_possiveis(self):
        tab = Tabuleiro()
        movs = tab.listar_movimentos_possiveis('B', 2, 1)
        self.assertTrue(isinstance(movs, list))


if __name__ == "__main__":
    unittest.main()
