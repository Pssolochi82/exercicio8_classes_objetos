import unittest
from ex7_classe_voo import Voo


class TestVoo(unittest.TestCase):

    def test_embarque_e_vagas(self):
        voo = Voo("AA100", "Lisboa", 5)
        voo.embarcar("João")
        voo.embarcar("Maria")
        voo.embarcar("Pedro")
        self.assertEqual(voo.vagas_disponiveis(), 2)

    def test_status_vagas_disponiveis(self):
        voo = Voo("AA100", "Lisboa", 5)
        voo.embarcar("João")
        self.assertEqual(voo.status_voo(), "Vagas disponíveis")

    def test_lotacao_percentual(self):
        voo = Voo("AA100", "Lisboa", 5)
        voo.embarcar("João")
        voo.embarcar("Maria")
        voo.embarcar("Pedro")
        self.assertEqual(voo.lotacao_percentual(), 60.0)

    def test_voo_lotado(self):
        voo = Voo("AA100", "Lisboa", 5)
        voo.embarcar("João")
        voo.embarcar("Maria")
        voo.embarcar("Pedro")
        voo.embarcar("Ana")
        voo.embarcar("Carlos")
        self.assertEqual(voo.status_voo(), "Voo lotado")

    def test_desembarque(self):
        voo = Voo("AA100", "Lisboa", 5)
        voo.embarcar("João")
        voo.embarcar("Maria")
        voo.embarcar("Pedro")
        voo.embarcar("Ana")
        voo.embarcar("Carlos")
        self.assertTrue(voo.desembarcar("João"))
        self.assertEqual(voo.vagas_disponiveis(), 1)
        self.assertEqual(voo.status_voo(), "Vagas disponíveis")

    def test_passageiro_duplicado(self):
        voo = Voo("AA100", "Lisboa", 5)
        self.assertTrue(voo.embarcar("Maria"))
        self.assertFalse(voo.embarcar("Maria"))


if __name__ == "__main__":
    unittest.main()
