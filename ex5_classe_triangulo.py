import math


class Triangulo:
    def __init__(self, lado1: float, lado2: float, lado3: float):
        self.lado1 = float(lado1)
        self.lado2 = float(lado2)
        self.lado3 = float(lado3)

        # lados devem ser positivos
        if self.lado1 <= 0 or self.lado2 <= 0 or self.lado3 <= 0:
            raise ValueError("Triângulo inválido: lados devem ser positivos.")

        if not self.eh_valido():
            raise ValueError("Triângulo inválido: viola a desigualdade triangular.")

    def eh_valido(self) -> bool:
        a, b, c = self.lado1, self.lado2, self.lado3
        return (a + b > c) and (a + c > b) and (b + c > a)

    def tipo_triangulo(self) -> str:
        a, b, c = self.lado1, self.lado2, self.lado3

        if a == b == c:
            return "Equilátero"
        elif (a == b) or (a == c) or (b == c):
            return "Isósceles"
        else:
            return "Escaleno"

    def eh_retangulo(self) -> bool:
        # Ordena para garantir que c é o maior lado
        lados = sorted([self.lado1, self.lado2, self.lado3])
        a, b, c = lados[0], lados[1], lados[2]

        # Comparação com tolerância (floats)
        return math.isclose(a * a + b * b, c * c, rel_tol=1e-9, abs_tol=1e-9)

    def calcular_area(self) -> float:
        a, b, c = self.lado1, self.lado2, self.lado3
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return area


if __name__ == "__main__":
    # Testes manuais (iguais ao enunciado)
    tri = Triangulo(5, 5, 5)
    print(tri.tipo_triangulo())  # Equilátero
    print(tri.eh_retangulo())    # False

    tri = Triangulo(5, 5, 8)
    print(tri.tipo_triangulo())  # Isósceles

    tri = Triangulo(3, 4, 5)
    print(tri.tipo_triangulo())  # Escaleno
    print(tri.eh_retangulo())    # True
    print(tri.calcular_area())   # 6.0

    try:
        tri = Triangulo(1, 2, 10)
    except ValueError:
        print("Triângulo inválido!")
