import unittest
from ex3_classe_celular import Celular


class TestCelular(unittest.TestCase):

    # Teste 1: Criar celular e fazer chamada
    def test_fazer_chamada(self):
        cel = Celular("iPhone 15", 100)
        cel.fazer_chamada(10)  # 10 minutos = 50% consumo
        self.assertEqual(cel.bateria, 50)
        self.assertTrue(cel.em_chamada)

    # Teste 2: Encerrar chamada
    def test_encerrar_chamada(self):
        cel = Celular("iPhone 15", 100)
        cel.fazer_chamada(10)
        cel.encerrar_chamada()
        self.assertFalse(cel.em_chamada)
        self.assertEqual(cel.bateria, 50)  # não muda ao encerrar

    # Teste 3: Carregar bateria
    def test_carregar_bateria(self):
        cel = Celular("iPhone 15", 50)
        cel.carregar_bateria(40)
        self.assertEqual(cel.bateria, 90)

    # Teste 4: Bateria máxima 100
    def test_bateria_maxima(self):
        cel = Celular("iPhone 15", 90)
        cel.carregar_bateria(20)
        self.assertEqual(cel.bateria, 100)

    # Teste 5: Bateria insuficiente
    def test_bateria_insuficiente(self):
        cel = Celular("Samsung", 30)
        cel.fazer_chamada(10)  # precisaria 50%
        self.assertFalse(cel.em_chamada)
        self.assertEqual(cel.bateria, 30)

    # Teste 6: Status completo
    def test_status(self):
        cel = Celular("Pixel 8", 75)
        status = cel.status()
        self.assertEqual(
            status,
            "Modelo: Pixel 8 | Bateria: 75% | Em chamada: Não"
        )


if __name__ == "__main__":
    unittest.main()
