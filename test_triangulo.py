import unittest
from ex5_classe_triangulo import Triangulo


class TestTriangulo(unittest.TestCase):

    def test_equilatero(self):
        tri = Triangulo(5, 5, 5)
        self.assertEqual(tri.tipo_triangulo(), "Equilátero")
        self.assertFalse(tri.eh_retangulo())

    def test_isosceles(self):
        tri = Triangulo(5, 5, 8)
        self.assertEqual(tri.tipo_triangulo(), "Isósceles")
        self.assertFalse(tri.eh_retangulo())

    def test_escaleno_retangulo(self):
        tri = Triangulo(3, 4, 5)
        self.assertEqual(tri.tipo_triangulo(), "Escaleno")
        self.assertTrue(tri.eh_retangulo())

    def test_area_3_4_5(self):
        tri = Triangulo(3, 4, 5)
        self.assertAlmostEqual(tri.calcular_area(), 6.0, places=7)

    def test_invalido(self):
        with self.assertRaises(ValueError):
            Triangulo(1, 2, 10)

    def test_lado_zero_ou_negativo(self):
        with self.assertRaises(ValueError):
            Triangulo(0, 4, 5)
        with self.assertRaises(ValueError):
            Triangulo(-3, 4, 5)


if __name__ == "__main__":
    unittest.main()
