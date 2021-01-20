class Pista:
    def __init__(self, nombre, favorita, duracion, fechadesalida):
        self.nombre = nombre
        self.favorita = favorita
        self.duracion = duracion
        self.fechadesalida = fechadesalida

    def __str__(self):
        return self.nombre

    def get_nombre(self):
        return self.nombre
        
    def get_favorita(self):
        return self.favorita

    def get_duracion(self):
        return self.duracion
        
    def get_fechadesalida(self):
        return self.fechadesalida
        
    def set_nombre(self, snombre):
        self.nombre = snombre
        
    def set_favorita(self, sfavorita):
        self.favorita = sfavorita
        
    def set_duracion(self, sduracion):
        self.duracion = sduracion
        
    def set_fecha(self, sfecha):
        self.fechadesalida = sfecha

    def descripcion_pista(self):
        return f"La canción se llama {self.nombre}, dura {self.duracion} minutos y salio el {self.fechadesalida}"

    def cancion_favorita(self):
        if self.favorita:
            return "La canción forma parte de tus canciones favoritas"
        return "La cancion no forma parte de tus canciones favoritas"

class ReproductorMusical:
    def __init__(self, canciones, nombre, artista):
        self.canciones = canciones
        self.nombre = nombre
        self.artista = artista

    def agregar_pista(self, pista):
        self.canciones.append(pista)

    def get_favoritas(self):

        favoritas = list(filter(lambda x: x.favorita == True, self.canciones))

        print(f"Tus canciones favoritas del disco {self.nombre} del artista {self.artista} son:")

        return [str(x) for x in favoritas]

    def get_pistas_ordenadas_por_duracion(self):

        ordenacion = sorted(self.canciones, key=lambda x: x.duracion)

        print(f"El disco {self.nombre} del artista {self.artista} contiene las canciones:")

        return [str(x) for x in ordenacion]

def main():

    cancion1 = Pista("Bajo El Sol", False, 3.24, "03/08/2016")

    print(cancion1.descripcion_pista())
    print(cancion1.cancion_favorita())
    print("")#salto de linea por estetica

    cancion2 = Pista("La Playa", False, 3.33, "05/03/2016")
    cancion3 = Pista("Balada Conformista", True, 3.28, "16/04/2016")
    cancion4 = Pista("Corazón Abierto", True, 2.58, "18/05/2016")
    cancion5 = Pista("Corporal", False, 4.42, "02/07/2016")

    canciones = [cancion1, cancion2, cancion3, cancion4, cancion5]

    factores = ReproductorMusical(canciones, "Factores", "Primavera club")

    cancion6 = Pista("Sangre", True, 2.42, "17/07/2016")

    factores.agregar_pista(cancion6)

    print(factores.get_favoritas())
    print("")#salto de linea por estetica

    print(factores.get_pistas_ordenadas_por_duracion())

if __name__ == "__main__":
    main()




    
