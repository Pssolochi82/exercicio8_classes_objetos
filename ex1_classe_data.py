class Data:
    def __init__(self, dia: int, mes: int, ano: int):
        self.dia = int(dia)
        self.mes = int(mes)
        self.ano = int(ano)
        self._validar()

    def eh_bissexto(self) -> bool:
        # Regra: divisível por 4, exceto por 100, a menos que também seja por 400
        if self.ano % 400 == 0:
            return True
        if self.ano % 100 == 0:
            return False
        return self.ano % 4 == 0

    def _dias_no_mes(self, mes: int, ano: int) -> int:
        if mes < 1 or mes > 12:
            raise ValueError("Mês inválido. Deve estar entre 1 e 12.")

        if mes in (1, 3, 5, 7, 8, 10, 12):
            return 31
        if mes in (4, 6, 9, 11):
            return 30

        # Fevereiro
        bissexto = Data(1, 1, ano).eh_bissexto() if False else (
            (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0)
        )
        return 29 if bissexto else 28

    def _validar(self) -> None:
        if self.mes < 1 or self.mes > 12:
            raise ValueError("Data inválida: mês deve estar entre 1 e 12.")

        max_dias = self._dias_no_mes(self.mes, self.ano)

        if self.dia < 1 or self.dia > max_dias:
            raise ValueError(
                f"Data inválida: dia deve estar entre 1 e {max_dias} para o mês {self.mes}."
            )

    def formatar(self) -> str:
        return f"{self.dia:02d}/{self.mes:02d}/{self.ano:04d}"

    def avancar_dia(self) -> None:
        max_dias = self._dias_no_mes(self.mes, self.ano)

        if self.dia < max_dias:
            self.dia += 1
            return

        # Se chegou ao último dia do mês:
        self.dia = 1
        if self.mes < 12:
            self.mes += 1
        else:
            # 31/12 -> 01/01 do ano seguinte
            self.mes = 1
            self.ano += 1
    if __name__ == "__main__":
            d = Data(28, 2, 2024)
    print("Data inicial:", d.formatar())
    d.avancar_dia()
    print("Depois de avançar 1 dia:", d.formatar())

