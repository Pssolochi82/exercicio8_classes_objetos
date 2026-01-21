import random


class Playlist:
    def __init__(self, nome: str):
        self.nome = nome
        self.musicas = []  # lista de dicts: {'titulo': str, 'duracao_segundos': int}

    def adicionar_musica(self, titulo: str, duracao_segundos: int):
        # valida duração
        if not isinstance(duracao_segundos, int) or duracao_segundos <= 0:
            return  # não adiciona

        # evita duplicados por título (igualdade exata)
        for musica in self.musicas:
            if musica["titulo"] == titulo:
                return  # já existe

        self.musicas.append({"titulo": titulo, "duracao_segundos": duracao_segundos})

    def remover_musica(self, titulo: str) -> bool:
        for i, musica in enumerate(self.musicas):
            if musica["titulo"] == titulo:
                self.musicas.pop(i)
                return True
        return False

    def duracao_total(self) -> str:
        total = 0
        for musica in self.musicas:
            total += musica["duracao_segundos"]

        minutos = total // 60
        segundos = total % 60
        return f"{minutos}:{segundos:02d}"

    def tocar_aleatoria(self):
        if not self.musicas:
            return None
        return random.choice(self.musicas)

    def listar_musicas(self):
        for i, musica in enumerate(self.musicas, start=1):
            dur = musica["duracao_segundos"]
            min_ = dur // 60
            seg_ = dur % 60
            print(f"{i}. {musica['titulo']} ({min_}:{seg_:02d})")


if __name__ == "__main__":
    # Testes manuais (do enunciado)
    pl = Playlist("Rock Clássico")
    pl.adicionar_musica("Bohemian Rhapsody", 355)   # 5:55
    pl.adicionar_musica("Stairway to Heaven", 482)  # 8:02
    pl.adicionar_musica("Hotel California", 391)    # 6:31

    print(pl.duracao_total())  # Esperado: 20:28 (355+482+391=1228s => 20:28)

    pl.listar_musicas()

    pl.remover_musica("Stairway to Heaven")
    print(pl.duracao_total())  # Esperado: 12:26 (355+391=746s => 12:26)

    print(pl.tocar_aleatoria())
