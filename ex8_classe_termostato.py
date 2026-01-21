class Termostato:
    def __init__(self, temp_atual: float, temp_desejada: float, modo: str = "manual"):
        self.temperatura_atual = float(temp_atual)
        self.temperatura_desejada = float(temp_desejada)

        self.modo = modo if modo in ("manual", "auto") else "manual"
        self.ativo = False  # começa desligado

        # aplica limites à temperatura desejada já na inicialização
        if self.temperatura_desejada > 30:
            self.temperatura_desejada = 30.0
        if self.temperatura_desejada < 10:
            self.temperatura_desejada = 10.0

    def ligar(self):
        self.ativo = True

    def desligar(self):
        self.ativo = False

    def aumentar_temperatura(self, graus: float):
        self.temperatura_desejada += float(graus)
        if self.temperatura_desejada > 30:
            self.temperatura_desejada = 30.0

    def diminuir_temperatura(self, graus: float):
        self.temperatura_desejada -= float(graus)
        if self.temperatura_desejada < 10:
            self.temperatura_desejada = 10.0

    def regulacao_automatica(self):
        if not self.ativo or self.modo != "auto":
            return

        if self.temperatura_atual < self.temperatura_desejada:
            self.temperatura_atual += 1
        elif self.temperatura_atual > self.temperatura_desejada:
            self.temperatura_atual -= 1
        # se igual, mantém

    def status(self) -> str:
        if not self.ativo:
            return "Termostato desligado"

        atual = self.temperatura_atual
        desejada = self.temperatura_desejada

        if atual < desejada:
            return f"Aquecendo... ({atual:.0f}°C / {desejada:.0f}°C)"
        elif atual > desejada:
            return f"Resfriando... ({atual:.0f}°C / {desejada:.0f}°C)"
        else:
            return f"Temperatura ideal! ({atual:.0f}°C / {desejada:.0f}°C)"


if __name__ == "__main__":
    # Teste 1: Criar e ligar termostato
    termo = Termostato(20, 25, "auto")
    termo.ligar()
    termo.regulacao_automatica()
    print(termo.temperatura_atual)  # Esperado: 21

    # Teste 2: Regulação contínua
    for _ in range(5):
        termo.regulacao_automatica()
    print(termo.temperatura_atual)  # Esperado: 25

    # Teste 3: Controle manual
    termo = Termostato(22, 22, "manual")
    termo.ligar()
    termo.aumentar_temperatura(2)
    print(termo.temperatura_desejada)  # Esperado: 24

    # Teste 4: Status detalhado
    termo = Termostato(22, 25, "auto")
    termo.ligar()
    print(termo.status())  # Esperado: "Aquecendo... (22°C / 25°C)"

    # Teste 5: Limite máximo/mínimo
    termo.aumentar_temperatura(10)
    print(termo.temperatura_desejada)  # Esperado: 30
    termo.diminuir_temperatura(25)
    print(termo.temperatura_desejada)  # Esperado: 10
class Termostato:
    def __init__(self, temp_atual: float, temp_desejada: float, modo: str = "manual"):
        self.temperatura_atual = float(temp_atual)
        self.temperatura_desejada = float(temp_desejada)

        self.modo = modo if modo in ("manual", "auto") else "manual"
        self.ativo = False  # começa desligado

        # aplica limites à temperatura desejada já na inicialização
        if self.temperatura_desejada > 30:
            self.temperatura_desejada = 30.0
        if self.temperatura_desejada < 10:
            self.temperatura_desejada = 10.0

    def ligar(self):
        self.ativo = True

    def desligar(self):
        self.ativo = False

    def aumentar_temperatura(self, graus: float):
        self.temperatura_desejada += float(graus)
        if self.temperatura_desejada > 30:
            self.temperatura_desejada = 30.0

    def diminuir_temperatura(self, graus: float):
        self.temperatura_desejada -= float(graus)
        if self.temperatura_desejada < 10:
            self.temperatura_desejada = 10.0

    def regulacao_automatica(self):
        if not self.ativo or self.modo != "auto":
            return

        if self.temperatura_atual < self.temperatura_desejada:
            self.temperatura_atual += 1
        elif self.temperatura_atual > self.temperatura_desejada:
            self.temperatura_atual -= 1
        # se igual, mantém

    def status(self) -> str:
        if not self.ativo:
            return "Termostato desligado"

        atual = self.temperatura_atual
        desejada = self.temperatura_desejada

        if atual < desejada:
            return f"Aquecendo... ({atual:.0f}°C / {desejada:.0f}°C)"
        elif atual > desejada:
            return f"Resfriando... ({atual:.0f}°C / {desejada:.0f}°C)"
        else:
            return f"Temperatura ideal! ({atual:.0f}°C / {desejada:.0f}°C)"


if __name__ == "__main__":
    # Teste 1: Criar e ligar termostato
    termo = Termostato(20, 25, "auto")
    termo.ligar()
    termo.regulacao_automatica()
    print(termo.temperatura_atual)  # Esperado: 21

    # Teste 2: Regulação contínua
    for _ in range(5):
        termo.regulacao_automatica()
    print(termo.temperatura_atual)  # Esperado: 25

    # Teste 3: Controle manual
    termo = Termostato(22, 22, "manual")
    termo.ligar()
    termo.aumentar_temperatura(2)
    print(termo.temperatura_desejada)  # Esperado: 24

    # Teste 4: Status detalhado
    termo = Termostato(22, 25, "auto")
    termo.ligar()
    print(termo.status())  # Esperado: "Aquecendo... (22°C / 25°C)"

    # Teste 5: Limite máximo/mínimo
    termo.aumentar_temperatura(10)
    print(termo.temperatura_desejada)  # Esperado: 30
    termo.diminuir_temperatura(25)
    print(termo.temperatura_desejada)  # Esperado: 10
