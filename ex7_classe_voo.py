class Voo:
    def __init__(self, numero: str, destino: str, passageiros_max: int):
        self.numero = numero
        self.destino = destino
        self.passageiros_max = int(passageiros_max)
        self.passageiros_atuais = []

    def embarcar(self, nome: str) -> bool:
        # Já embarcou?
        if nome in self.passageiros_atuais:
            return False

        # Há vagas?
        if len(self.passageiros_atuais) >= self.passageiros_max:
            return False

        self.passageiros_atuais.append(nome)
        return True

    def desembarcar(self, nome: str) -> bool:
        if nome in self.passageiros_atuais:
            self.passageiros_atuais.remove(nome)
            return True
        return False

    def vagas_disponiveis(self) -> int:
        return self.passageiros_max - len(self.passageiros_atuais)

    def lotacao_percentual(self) -> float:
        if self.passageiros_max == 0:
            return 0.0
        return (len(self.passageiros_atuais) / self.passageiros_max) * 100

    def status_voo(self) -> str:
        if len(self.passageiros_atuais) == 0:
            return "Voo deserto"
        if len(self.passageiros_atuais) == self.passageiros_max:
            return "Voo lotado"
        return "Vagas disponíveis"


if __name__ == "__main__":
    # Testes manuais (do enunciado)
    voo = Voo("AA100", "Lisboa", 5)
    voo.embarcar("João")
    voo.embarcar("Maria")
    voo.embarcar("Pedro")
    print(voo.vagas_disponiveis())       # Esperado: 2
    print(voo.status_voo())              # Esperado: "Vagas disponíveis"
    print(voo.lotacao_percentual())      # Esperado: 60.0

    voo.embarcar("Ana")
    voo.embarcar("Carlos")
    print(voo.status_voo())              # Esperado: "Voo lotado"

    voo.desembarcar("João")
    print(voo.vagas_disponiveis())       # Esperado: 1
    print(voo.status_voo())              # Esperado: "Vagas disponíveis"

    resultado = voo.embarcar("Maria")
    print(resultado)                      # Esperado: False


