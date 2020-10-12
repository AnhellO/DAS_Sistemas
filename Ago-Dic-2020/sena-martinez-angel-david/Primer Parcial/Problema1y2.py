import random

class Pista():
    def __init__(self, nombre, favorita:bool, duracion:float, genero):
        self.nombre = nombre
        self.favorita = favorita
        self.duracion = duracion
        self.genero = genero

    def _str_(self):
        return f"Nombre: {self.nombre}, ¿es favorita?: {self.favorita}, tiene una duracion de: {self.duracion} y el genero es: {self.genero}"
    
    def genero_favorito(self):
        if self.genero == "Reggaeton":
            print(f"{self.genero} es mi Genero Favorito")
        else:
            print("Me Caga el Reggaeton")
  
    
class AppMusical():
    def __init__(self, lista, nombre, ecualizador):
        self.lista = lista
        self.nombre = nombre
        self.ecualizador = ecualizador
    
    def _str_(self):
        return f"La {self.lista} tiene un ecualizador {self.ecualizador}"
    
    def add_song(self,song):#funcion para agragar canciones a la lista
        self.lista.append(song)
        for cancion in self.lista:
            print(cancion.nombre, cancion.duracion)

    def decorador(function):
        def wrapper(self):
            print("Las canciones favoritas son:")
            function(self)
        return wrapper
    
    @decorador
    def favoritas(self):# Solo imprimo las favoritas
        for cancion in self.lista:
            if cancion.favorita == True:
                print(cancion.nombre)

    def ordenar(self):
        orden= sorted(self.lista, key=lambda x: x.duracion,reverse=True)
        for cancion in orden:
            print(cancion.nombre,cancion.genero)

    def decorador2(function):
        def wrapper(self):
            print("El Nuevo Ecualizador de la lista es:")
            print('--------')
            function(self)
        return wrapper

    @decorador2
    def change_ecualizador(self):
        list_ecualizadores = ["Clásico", "Profundo", "Ruidoso", "Acústico", "Electronico"]
        print(random.choice(list_ecualizadores))


def main():
    lista =[]
    j_balvin=Pista("Rojo", True, 1.6, "Reggaeton")
    acdc=Pista("Back in Black", False, 3.2, "Rock")
    reik = Pista("Indeciso", False, 2.2, "Pop")
    App=AppMusical(lista,"Lista Perrona", "Clasico")
    #print(App)
    #Funcion genero favorito
    print("Genero Favorito:")
    acdc.genero_favorito()
    j_balvin.genero_favorito()
    print("\n")
    App.add_song(j_balvin)
    App.add_song(acdc)
    print("\n")
    print("Canciones en Orden:")
    App.ordenar()
    print("\n")
    App.favoritas()
    print("\n")
    App.change_ecualizador()
    
if __name__ == "__main__":
    main()