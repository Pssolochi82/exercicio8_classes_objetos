import unittest
from ex9_classe_loja import Loja


class TestLoja(unittest.TestCase):

    def setUp(self):
        self.loja = Loja("Tech Store")
        self.loja.adicionar_produto("P001", "Notebook", 1500.00, 5)
        self.loja.adicionar_produto("P002", "Mouse", 50.00, 20)
        self.loja.adicionar_produto("P003", "Teclado", 150.00, 10)

    def test_venda_sucesso(self):
        valor = self.loja.realizar_venda("P001", 2)
        self.assertEqual(valor, 3000.0)
        self.assertEqual(self.loja.produtos["P001"]["estoque"], 3)

    def test_venda_estoque_insuficiente(self):
        valor = self.loja.realizar_venda("P002", 25)
        self.assertEqual(valor, -1)

    def test_remover_produto(self):
        self.assertTrue(self.loja.remover_produto("P003"))
        self.assertEqual(len(self.loja.produtos), 2)

    def test_adicionar_produto_duplicado(self):
        resultado = self.loja.adicionar_produto("P001", "Notebook", 1500, 5)
        self.assertFalse(resultado)

    def test_produto_inexistente_venda(self):
        valor = self.loja.realizar_venda("P999", 1)
        self.assertEqual(valor, -1)


if __name__ == "__main__":
    unittest.main()
