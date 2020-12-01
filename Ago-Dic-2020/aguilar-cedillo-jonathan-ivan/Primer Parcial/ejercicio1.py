class Pista():
    def __init__ (self, nombre: str, favorita: bool, duracion: int, artista: str):
        #la duracion esta contemplada en segundos
        self.nombre = nombre
        self.favorita = favorita
        self.duracion = duracion
        self.artista = artista
    def get_informacion(self):
        return f"Nombre de la cancion: {self.nombre} \ncancion favorita: {self.c_favorita()} \nduracion: {self.duracion} \nartista: {self.artista}"
    def c_favorita(self):
        if self.favorita:
            return 'es mi cancion favoria uwu'
        return 'quien puso esto? (¬.¬)'

class ReproductorMusical():
    def __init__(self, cancion, duracion, artista):
        self.playlist = list()
        self.cancion = cancion
        self.duracion = duracion
        self.artista = artista
    def add_cancion(self, tema):
        self.playlist.append(tema)
    def get_favorita(self):
        orden= list()
        for tema in self.playlist:
            if tema.favorita:
                orden.append(tema)
        orden.sort(key=lambda a: a.duracion, reverse=False)
        return orden

if __name__ == "__main__":
    EDGE= Pista('metalingust', True, 261, 'Alter Bridge')
    Maluma = Pista('hawai', False, 259, 'Maluma')
    Nirvana = Pista('Smells Like Teen Spirit', True, 278, 'Nirvana')
    KISS = Pista('Rock And Roll All Nite', True, 242, 'KISS')
    bunny=Pista('La Dificil', False, 193, 'Bad Bunny')
    sigo= Pista('Sigo Aqui', True, 216, 'Alex Ubago')

    reproductor = ReproductorMusical('Rock and all nite', '242','KISS')
    reproductor.add_cancion(EDGE)
    reproductor.add_cancion(Maluma)
    reproductor.add_cancion(Nirvana)
    reproductor.add_cancion(KISS)
    reproductor.add_cancion(bunny)
    reproductor.add_cancion(sigo)
    orden = reproductor.get_favorita()
    for tema in orden:
        print(tema.nombre)