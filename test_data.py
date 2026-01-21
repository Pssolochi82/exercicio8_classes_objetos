import unittest

from ex1_classe_data import Data  # se guardares a classe num ficheiro chamado data.py


class TestData(unittest.TestCase):

    # --------- Testes de validação ---------
    def test_data_valida(self):
        d = Data(31, 12, 2024)
        self.assertEqual(d.formatar(), "31/12/2024")

    def test_mes_invalido(self):
        with self.assertRaises(ValueError):
            Data(10, 13, 2024)

    def test_dia_invalido_mes_30(self):
        with self.assertRaises(ValueError):
            Data(31, 4, 2024)  # abril tem 30

    def test_fevereiro_nao_bissexto_invalido(self):
        with self.assertRaises(ValueError):
            Data(29, 2, 2023)  # 2023 não é bissexto

    def test_fevereiro_bissexto_valido(self):
        d = Data(29, 2, 2024)  # 2024 é bissexto
        self.assertEqual(d.formatar(), "29/02/2024")

    # --------- Testes de bissexto ---------
    def test_bissexto_divisivel_por_4(self):
        self.assertTrue(Data(1, 1, 2024).eh_bissexto())

    def test_nao_bissexto_divisivel_por_100(self):
        self.assertFalse(Data(1, 1, 1900).eh_bissexto())

    def test_bissexto_divisivel_por_400(self):
        self.assertTrue(Data(1, 1, 2000).eh_bissexto())

    # --------- Testes de formatar ---------
    def test_formatar_zeros_a_esquerda(self):
        d = Data(3, 4, 2024)
        self.assertEqual(d.formatar(), "03/04/2024")

    # --------- Testes de avançar dia ---------
    def test_avancar_dia_normal(self):
        d = Data(10, 1, 2024)
        d.avancar_dia()
        self.assertEqual(d.formatar(), "11/01/2024")

    def test_avancar_fim_mes_30_dias(self):
        d = Data(30, 4, 2024)
        d.avancar_dia()
        self.assertEqual(d.formatar(), "01/05/2024")

    def test_avancar_fim_mes_31_dias(self):
        d = Data(31, 1, 2024)
        d.avancar_dia()
        self.assertEqual(d.formatar(), "01/02/2024")

    def test_avancar_fevereiro_nao_bissexto(self):
        d = Data(28, 2, 2023)
        d.avancar_dia()
        self.assertEqual(d.formatar(), "01/03/2023")

    def test_avancar_fevereiro_bissexto_28_para_29(self):
        d = Data(28, 2, 2024)
        d.avancar_dia()
        self.assertEqual(d.formatar(), "29/02/2024")

    def test_avancar_fevereiro_bissexto_29_para_marco(self):
        d = Data(29, 2, 2024)
        d.avancar_dia()
        self.assertEqual(d.formatar(), "01/03/2024")

    def test_avancar_fim_ano(self):
        d = Data(31, 12, 2024)
        d.avancar_dia()
        self.assertEqual(d.formatar(), "01/01/2025")


if __name__ == "__main__":
    unittest.main()
