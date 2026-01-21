class Loja:
    def __init__(self, nome: str):
        self.nome = nome
        self.produtos = {}  # {codigo: {nome, preco, estoque, vendido}}

    def adicionar_produto(self, codigo: str, nome: str, preco: float, estoque: int):
        if codigo in self.produtos:
            return False

        if preco <= 0 or estoque < 0:
            return False

        self.produtos[codigo] = {
            "nome": nome,
            "preco": float(preco),
            "estoque": int(estoque),
            "vendido": 0
        }
        return True

    def remover_produto(self, codigo: str) -> bool:
        if codigo in self.produtos:
            del self.produtos[codigo]
            return True
        return False

    def realizar_venda(self, codigo: str, quantidade: int):
        if codigo not in self.produtos:
            return -1

        if quantidade <= 0:
            return -1

        produto = self.produtos[codigo]

        if produto["estoque"] < quantidade:
            return -1

        produto["estoque"] -= quantidade
        produto["vendido"] += quantidade

        valor = produto["preco"] * quantidade
        return valor

    def listar_produtos(self):
        print(f"--- Produtos da loja {self.nome} ---")
        print("Código | Nome | Preço | Estoque")
        for codigo, p in self.produtos.items():
            print(
                f"{codigo} | {p['nome']} | €{p['preco']:.2f} | {p['estoque']}"
            )

    def relatorio_vendas(self):
        total_estoque = 0
        produto_mais_vendido = None
        max_vendas = -1

        for p in self.produtos.values():
            total_estoque += p["preco"] * p["estoque"]

            if p["vendido"] > max_vendas:
                max_vendas = p["vendido"]
                produto_mais_vendido = p["nome"]

        print("=== RELATÓRIO DA LOJA ===")
        print(f"Loja: {self.nome}")
        print(f"Quantidade de produtos: {len(self.produtos)}")
        print(f"Valor total em estoque: €{total_estoque:.2f}")

        if produto_mais_vendido:
            print(f"Produto mais vendido: {produto_mais_vendido}")
        else:
            print("Produto mais vendido: Nenhum")
        print("========================")


if __name__ == "__main__":
    # Testes manuais do enunciado
    loja = Loja("Tech Store")
    loja.adicionar_produto("P001", "Notebook", 1500.00, 5)
    loja.adicionar_produto("P002", "Mouse", 50.00, 20)
    loja.adicionar_produto("P003", "Teclado", 150.00, 10)

    valor = loja.realizar_venda("P001", 2)
    print(valor)  # Esperado: 3000.0
    print(loja.produtos["P001"]["estoque"])  # Esperado: 3

    valor = loja.realizar_venda("P002", 25)
    print(valor)  # Esperado: -1

    loja.listar_produtos()
    loja.relatorio_vendas()

    loja.remover_produto("P003")
    print(len(loja.produtos))  # Esperado: 2
