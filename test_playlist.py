import unittest
import random

from ex6_classe_playlist import Playlist


class TestPlaylist(unittest.TestCase):

    def setUp(self):
        self.pl = Playlist("Rock Clássico")
        self.pl.adicionar_musica("Bohemian Rhapsody", 355)
        self.pl.adicionar_musica("Stairway to Heaven", 482)
        self.pl.adicionar_musica("Hotel California", 391)

    def test_duracao_total(self):
        self.assertEqual(self.pl.duracao_total(), "20:28")

    def test_remover_musica(self):
        removida = self.pl.remover_musica("Stairway to Heaven")
        self.assertTrue(removida)
        self.assertEqual(self.pl.duracao_total(), "12:26")

    def test_remover_inexistente(self):
        self.assertFalse(self.pl.remover_musica("Nada"))

    def test_evitar_duplicadas(self):
        self.pl.adicionar_musica("Bohemian Rhapsody", 355)
        self.assertEqual(len(self.pl.musicas), 3)  # não deve adicionar

    def test_duracao_invalida(self):
        pl2 = Playlist("Teste")
        pl2.adicionar_musica("X", -10)
        pl2.adicionar_musica("Y", 0)
        self.assertEqual(len(pl2.musicas), 0)

    def test_tocar_aleatoria(self):
        random.seed(1)
        musica = self.pl.tocar_aleatoria()
        self.assertIsNotNone(musica)
        self.assertIn("titulo", musica)
        self.assertIn("duracao_segundos", musica)


if __name__ == "__main__":
    unittest.main()
