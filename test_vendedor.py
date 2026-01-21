import unittest
from ex4_classe_vendedor import Vendedor


class TestVendedor(unittest.TestCase):

    # Teste 1: Venda que atinge a meta
    def test_atinge_meta(self):
        vendedor = Vendedor("João", 10000, 5)
        vendedor.registrar_venda(6000)
        vendedor.registrar_venda(5500)

        self.assertTrue(vendedor.atingiu_meta())
        self.assertEqual(vendedor.calcular_comissao(), 75.0)

    # Teste 2: Venda abaixo da meta
    def test_abaixo_meta(self):
        vendedor = Vendedor("Maria", 10000, 5)
        vendedor.registrar_venda(8000)

        self.assertFalse(vendedor.atingiu_meta())
        self.assertEqual(vendedor.calcular_comissao(), 0.0)

    # Teste 3: Múltiplas vendas
    def test_multiplas_vendas(self):
        vendedor = Vendedor("Pedro", 5000, 10)
        vendedor.registrar_venda(1000)
        vendedor.registrar_venda(2000)
        vendedor.registrar_venda(3000)  # total = 6000

        self.assertTrue(vendedor.atingiu_meta())
        self.assertEqual(vendedor.vendas_mes, 6000)
        self.assertEqual(vendedor.calcular_comissao(), 100.0)  # (6000-5000)*10%

    # Teste 4: Venda inválida (negativa ou zero)
    def test_venda_invalida(self):
        vendedor = Vendedor("Teste", 1000, 5)
        vendedor.registrar_venda(-500)
        vendedor.registrar_venda(0)

        self.assertEqual(vendedor.vendas_mes, 0.0)
        self.assertFalse(vendedor.atingiu_meta())
        self.assertEqual(vendedor.calcular_comissao(), 0.0)

    # Teste 5: Meta zero
    def test_meta_zero(self):
        vendedor = Vendedor("Zero", 0, 10)
        vendedor.registrar_venda(1000)

        self.assertTrue(vendedor.atingiu_meta())
        self.assertEqual(vendedor.calcular_comissao(), 100.0)  # 1000 * 10%


if __name__ == "__main__":
    unittest.main()
