class Vendedor:
    def __init__(self, nome: str, meta: float, percentual_comissao: float):
        self.nome = nome
        self.meta_mes = float(meta)
        self.percentual_comissao = float(percentual_comissao)
        self.vendas_mes = 0.0

    def registrar_venda(self, valor: float):
        try:
            valor = float(valor)
        except (ValueError,TypeError):
            return
        if valor <= 0:
            return  # ignora vendas inválidas

        self.vendas_mes += valor

    def calcular_comissao(self) -> float:
        if self.vendas_mes <= self.meta_mes:
            return 0.0

        excedente = self.vendas_mes - self.meta_mes
        comissao = excedente * self.percentual_comissao / 100
        return comissao

    def atingiu_meta(self) -> bool:
        return self.vendas_mes >= self.meta_mes

    def exibir_relatorio(self):
        percentual_atingido = 0.0
        if self.meta_mes > 0:
            percentual_atingido = (self.vendas_mes / self.meta_mes) * 100

        atingiu = "Sim" if self.atingiu_meta() else "Não"
        comissao = self.calcular_comissao()

        print("=== RELATÓRIO DO VENDEDOR ===")
        print(f"Nome: {self.nome}")
        print(f"Meta do mês: €{self.meta_mes:.2f}")
        print(f"Vendas realizadas: €{self.vendas_mes:.2f}")
        print(f"Percentual da meta atingido: {percentual_atingido:.2f}%")
        print(f"Atingiu a meta? {atingiu}")
        print(f"Comissão a receber: €{comissao:.2f}")
        print("============================")


if __name__ == "__main__":
    # Demonstração simples
    vendedor = Vendedor("João", 10000, 5)
    vendedor.registrar_venda(6000)
    vendedor.registrar_venda(5500)
    vendedor.exibir_relatorio()

if __name__ == "__main__":
    # Teste 3: Múltiplas vendas
    vendedor = Vendedor("Pedro", 5000, 10)
    vendedor.registrar_venda(1000)
    vendedor.registrar_venda(2000)
    vendedor.registrar_venda(3000)
    print(vendedor.vendas_mes)  # Esperado: 6000
    print(vendedor.calcular_comissao())  # Esperado: 100.0

    # Teste 4: Relatório completo
    vendedor = Vendedor("Ana", 15000, 8)
    vendedor.registrar_venda(18000)
    vendedor.exibir_relatorio()

