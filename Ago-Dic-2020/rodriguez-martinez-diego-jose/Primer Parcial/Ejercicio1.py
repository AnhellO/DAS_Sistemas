class Pista:

    __iniciales = False

    def __init__(self,**kwargs):
        self._nombre = kwargs.get("nombre", "Untitled")
        self._favorita = kwargs.get("favorita", False)
        self._duracion = kwargs.get("duracion", 0.0)
        self._artista = kwargs.get("artista", "Artista Desconocido")
        self.__artistabak = kwargs.get("artista", "Artista Desconocido")

    def toggle_favourite(self):
        self._favorita = not self._favorita

    def toggle_iniciales_artista(self):
        
        if not self.__iniciales:
            self._artista = ". ".join([i[0].upper() for i in self._artista.split(" ")])
            self.__iniciales = True
        else:
            self._artista = self.__artistabak

    @property
    def informacion_cancion(self,**kwargs):
        informacion = [f"{'#'*5} INFORMACION DE {self._nombre.upper()} {'#'*5}"]

        for k,v in vars(self).items():
            informacion.append(k[1:].title() + ": "  + str(v))

        return "\n".join([i for i in informacion if "__" not in i]) + "\n"

    @informacion_cancion.setter
    def informacion_cancion(self, datos):

        self._nombre = datos.get("nombre", self._nombre)
        self._favorita = datos.get("favorita", self._favorita)
        self._duracion = datos.get("duracion", self._duracion)
        self._artista = datos.get("artista", self._artista)


######
class ReproductorMusical():

    marca = "SONY"
    modelo = "2020"

    def __init__(self, canciones):
        self.play_queue = canciones
    
    def agregar_pista(self, cancion):
        self.play_queue.append(cancion)

    @property
    def informacion(self):
        return ", ".join([self.marca,self.modelo])
    
    def informacion_de_pistas(self):
        return "\n".join([cancion.informacion_cancion for cancion in self.play_queue])

    def quitar_pista(self, index = 0, nombre = None):

        if len(self.play_queue) == 0:
            raise ValueError("Playlist Vacia")

        if not nombre:
            self.play_queue.pop(index)
        else:
            for i in self.play_queue:
                if i._nombre == nombre:
                    cancion = i
                    exit

            self.play_queue.remove(cancion)

    def get_canciones_favoritas(self):
        return [cancion._nombre for cancion in self.play_queue if cancion._favorita]

    def get_canciones(self):
        canciones = [cancion for cancion in self.play_queue]
        canciones.sort(key= lambda x: x._duracion)

        self.play_queue = canciones

        return [[cancion._nombre,cancion._artista,cancion._duracion] for cancion in canciones]
        


#####


if __name__ == "__main__":
    
    # pista = Pista(artista = "JUICE Wrld")
    # print(pista.informacion_cancion)
    # pista.toggle_favourite()
    # pista.toggle_iniciales_artista()
    # print(pista.informacion_cancion)
    # pista.toggle_iniciales_artista()
    # pista.informacion_cancion = {"duracion": 10.1}
    # print(pista.informacion_cancion)

    canciones = [Pista(nombre = "Cancion1", favorita= True, duracion = 12, artista = "A")]

    mReproductor = ReproductorMusical(canciones)
    print("PLAY LIST:\n", mReproductor.get_canciones())
    print("\nCANCIONES FAVORITAS:\n", mReproductor.get_canciones_favoritas())
    mReproductor.agregar_pista(Pista(nombre = "Cancion5", favorita = True, duracion = 5.5))
    print("\nPLAY LIST:\n",mReproductor.get_canciones())
    mReproductor.quitar_pista()
    print("\nPLAY LIST:\n",mReproductor.get_canciones())
    print(mReproductor.informacion)

    print(mReproductor.informacion_de_pistas())