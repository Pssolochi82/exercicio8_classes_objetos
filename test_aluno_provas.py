import unittest
from exercicio8_classes_objetos.ex2_classe_aluno_provas import AlunoProvas


class TestAlunoProvas(unittest.TestCase):

    # Teste 1: Criar aluno e adicionar prova
    def test_adicionar_uma_prova(self):
        aluno = AlunoProvas("João Silva", "2024001")
        aluno.adicionar_prova([12, 14, 13])
        self.assertEqual(aluno.media_geral(), 13.0)
        self.assertEqual(aluno.conceito_final(), 'B')

    # Teste 2: Múltiplas provas
    def test_multiplas_provas(self):
        aluno = AlunoProvas("Maria Santos", "2024002")
        aluno.adicionar_prova([10, 12, 11])
        aluno.adicionar_prova([14, 15, 16])
        self.assertEqual(aluno.media_geral(), 13.0)
        self.assertEqual(aluno.conceito_final(), 'B')

    # Teste 3: Notas altas (conceito A)
    def test_conceito_a(self):
        aluno = AlunoProvas("Pedro Costa", "2024003")
        aluno.adicionar_prova([15, 16, 17])
        self.assertEqual(aluno.conceito_final(), 'A')

    # Teste 4: Notas baixas (conceito R)
    def test_conceito_r(self):
        aluno = AlunoProvas("Ana Oliveira", "2024004")
        aluno.adicionar_prova([5, 6, 7])
        self.assertEqual(aluno.conceito_final(), 'R')

    # Teste 5: Validação de notas inválidas
    def test_notas_invalidas(self):
        aluno = AlunoProvas("Teste", "0000")
        aluno.adicionar_prova([10, 25, 8])  # Nota inválida
        self.assertEqual(len(aluno.provas), 0)

    # Teste extra: lista com tamanho errado
    def test_lista_tamanho_errado(self):
        aluno = AlunoProvas("Teste", "0001")
        aluno.adicionar_prova([10, 12])  # só 2 notas
        self.assertEqual(len(aluno.provas), 0)

    # Teste extra: sem provas
    def test_sem_provas(self):
        aluno = AlunoProvas("Vazio", "0002")
        self.assertEqual(aluno.media_geral(), 0.0)
        self.assertEqual(aluno.conceito_final(), 'R')


if __name__ == "__main__":
    unittest.main()
