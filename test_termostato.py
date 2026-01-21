import unittest
from ex8_classe_termostato import Termostato


class TestTermostato(unittest.TestCase):

    def test_aquecimento_automatico(self):
        termo = Termostato(20, 25, "auto")
        termo.ligar()
        termo.regulacao_automatica()
        self.assertEqual(termo.temperatura_atual, 21.0)

    def test_regulacao_continua_ate_meta(self):
        termo = Termostato(20, 25, "auto")
        termo.ligar()
        for _ in range(10):
            termo.regulacao_automatica()
        self.assertEqual(termo.temperatura_atual, 25.0)

    def test_controle_manual(self):
        termo = Termostato(22, 22, "manual")
        termo.ligar()
        termo.aumentar_temperatura(2)
        self.assertEqual(termo.temperatura_desejada, 24.0)

    def test_status_aquecendo(self):
        termo = Termostato(22, 25, "auto")
        termo.ligar()
        self.assertEqual(termo.status(), "Aquecendo... (22°C / 25°C)")

    def test_limites_maximo_minimo(self):
        termo = Termostato(22, 25, "auto")
        termo.ligar()
        termo.aumentar_temperatura(10)  # 25 + 10 = 35 -> 30
        self.assertEqual(termo.temperatura_desejada, 30.0)
        termo.diminuir_temperatura(25)  # 30 - 25 = 5 -> 10
        self.assertEqual(termo.temperatura_desejada, 10.0)

    def test_desligado_nao_regula(self):
        termo = Termostato(20, 25, "auto")
        termo.regulacao_automatica()
        self.assertEqual(termo.temperatura_atual, 20.0)

    def test_manual_nao_regula(self):
        termo = Termostato(20, 25, "manual")
        termo.ligar()
        termo.regulacao_automatica()
        self.assertEqual(termo.temperatura_atual, 20.0)


if __name__ == "__main__":
    unittest.main()
