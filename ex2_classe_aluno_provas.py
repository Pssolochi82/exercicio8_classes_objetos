class AlunoProvas:
    def __init__(self, nome: str, matricula: str):
        self.nome = nome
        self.matricula = matricula
        self.provas = []

    def adicionar_prova(self, notas):
        # Validar se é lista com exatamente 3 elementos
        if not isinstance(notas, list) or len(notas) != 3:
            return  # simplesmente não adiciona

        # Validar cada nota
        for nota in notas:
            if not isinstance(nota, (int, float)):
                return
            if nota < 0 or nota > 20:
                return

        # Se tudo estiver válido, adiciona a prova
        self.provas.append(notas)

    def media_geral(self) -> float:
        if not self.provas:
            return 0.0

        total = 0
        quantidade = 0

        for prova in self.provas:
            for nota in prova:
                total += nota
                quantidade += 1

        return total / quantidade

    def conceito_final(self) -> str:
        media = self.media_geral()

        if media >= 14:
            return 'A'
        elif media >= 11:
            return 'B'
        elif media >= 9:
            return 'C'
        else:
            return 'R'


if __name__ == "__main__":
    # Demonstração simples
    aluno = AlunoProvas("João Silva", "2024001")
    aluno.adicionar_prova([12, 14, 13])
    print("Média:", aluno.media_geral())
    print("Conceito:", aluno.conceito_final())
