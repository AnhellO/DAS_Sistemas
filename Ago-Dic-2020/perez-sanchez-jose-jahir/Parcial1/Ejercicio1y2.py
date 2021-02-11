import random

class Pista:
    def __init__(self, nombre: str, favorita: bool, duracion: float, genero):
        self.nombre = nombre 
        self.favorita = favorita 
        self.duracion = duracion
        self.genero = genero
    
    def __str__(self):
        return f"Cancion: {self.nombre}, favorita: {self.favorita}, duracion: {self.duracion}, grupo: {self.genero}"
    
    def es_mi_fav(self):
        if self.favorita == True:
            print(f"{self.nombre} si es mi favorita")
        else: 
            print(f"{self.nombre} no es mi favorita")
    

class ReproductorMusical:
    def __init__(self,lista, nombre_lista, color_fondo):
        self.lista = lista
        self.nombre_lista = nombre_lista
        self.color_fondo = color_fondo
    
    def __str__(self):
        return f"La {self.nombre_lista} tiene un color {self.color_fondo}"

    def agregar_pista(self, pista):
        self.lista.append(pista)
        for cancion in self.lista:
            print(cancion.nombre, cancion.duracion, cancion.genero)

    def decorador(function):
        def wrapper(self):
            print("Mis canciones favoritas son:")
            function(self)
            print(":D")
        return wrapper

    @decorador
    def favoritas(self):
        for cancion in self.lista:
            if cancion.favorita == True:
                print(cancion.nombre)

    def orden(self):
        orden = sorted(self.lista, key=lambda x: x.duracion, reverse=True)
        for cancion in orden:
            print(cancion.nombre, cancion.duracion, cancion.genero)

    def decorador2(function):
        def wrapper(self):
            print("El reproductor cambiara al color")
            print("......")
            print("Tatatachán!!!!")
            function(self)
        return wrapper
    
    @decorador2
    def cambiar_color(self):
        l = ["Verde", "Azul", "Amarillo","Rojo","Naranja", "Morado"]
        print(random.choice(l))

def main():
    lista = []
    juanes = Pista("Camisa negra", True, 2.40, "pop")
    panda = Pista("Los malaventurados no lloran", False, 3.23, "rock")
    bose = Pista("Amante Bandido", True, 3.24, "pop")
    Reproductor = ReproductorMusical(lista, "Lista 1","Rojo")
    Reproductor.agregar_pista(juanes)
    print("\n")
    Reproductor.agregar_pista(panda)
    print("\n")
    Reproductor.agregar_pista(bose)
    print("\n")
    Reproductor.orden()
    print("\n")
    Reproductor.favoritas()
    print("\n")
    panda.es_mi_fav()
    print("\n")
    Reproductor.cambiar_color()

if __name__ == "__main__":
    main()
                
