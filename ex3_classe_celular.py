class Celular:
    def __init__(self, modelo: str, bateria_inicial: int):
        self.modelo = modelo

        # Bateria inicial não pode ultrapassar 100
        if bateria_inicial < 0:
            self.bateria = 0
        elif bateria_inicial > 100:
            self.bateria = 100
        else:
            self.bateria = bateria_inicial

        self.em_chamada = False
        self.duracao_chamada = 0  # em segundos

    def fazer_chamada(self, duracao_minutos: int):
        if duracao_minutos <= 0:
            return

        consumo = duracao_minutos * 5  # 5% por minuto

        # Verifica se há bateria suficiente
        if self.bateria < consumo:
            return  # não inicia chamada

        self.bateria -= consumo
        self.em_chamada = True
        self.duracao_chamada = duracao_minutos * 60

    def encerrar_chamada(self):
        self.em_chamada = False
        self.duracao_chamada = 0

    def carregar_bateria(self, percentual_adicional: int):
        if percentual_adicional <= 0:
            return

        self.bateria += percentual_adicional
        if self.bateria > 100:
            self.bateria = 100

    def status(self) -> str:
        em_chamada_str = "Sim" if self.em_chamada else "Não"
        return f"Modelo: {self.modelo} | Bateria: {self.bateria}% | Em chamada: {em_chamada_str}"


if __name__ == "__main__":
    # Demonstração simples
    cel = Celular("iPhone 15", 100)
    cel.fazer_chamada(10)
    print("Bateria após chamada:", cel.bateria)
    print("Em chamada:", cel.em_chamada)

    cel.encerrar_chamada()
    print("Após encerrar chamada:", cel.em_chamada)

    cel.carregar_bateria(40)
    print("Após carregar bateria:", cel.bateria)

    print(cel.status())
