from collections.abc import Iterable, Iterator
#clase que recibe la lista y la itera posicion por posición
class Iteraciones(Iterator):
    def __init__(self, collection) -> None:
        self.listapropia = collection
        self.posicion_iterator = 0
    
    def __next__(self):
        try:
            nueva_lista = self.listapropia[self.posicion_iterator]
            self.posicion_iterator += 1
        except IndexError:
            raise StopIteration()

        return nueva_lista

#funcion para saber que equipo se escogio para hacer los unittest cases
def pilotos(seleccion):
    RedBull = ["Sergio Perez", "Max Verstappen"]
    Mercedes = ["Lewis Hamilton", "Valteri Bottas"]
    Ferrari = ["Charles Leclerc", "Carlos Sainz"]
    McLaren = ["Lando Norris", "Daniel Ricciardo"]
    AlphaThauri = ["Pierre Gasly", "Yuki Tsunoda"]
    AstonMartin = ["Lance Stroll", "Sebastian Vettel"]
    Alphine = ["Fernando Alonso", "Esteban Ocon"]
    Haas = ["Mick Schumacher", "Nikita Mazepin"]
    AlphaRomeo = ["Antonio Giovinazzi", "Kimi Raikkonen"]
    Williams = ["George Rusell", "Nicholas Latifi"]
    global listaEquipo

    if seleccion == "Redbull" :
        listaEquipo = RedBull
    if seleccion == "Mercedes" :
        listaEquipo = Mercedes
    if seleccion == "Ferrari" :
        listaEquipo = Ferrari
    if seleccion == "Haas" :
        listaEquipo = Haas
    if seleccion == "AlphaRomeo" :
        listaEquipo = AlphaRomeo
    if seleccion == "Alphine" :
        listaEquipo = Alphine
    if seleccion == "AlphaTauri" :
        listaEquipo = AlphaThauri
    if seleccion == "McLaren" :
        listaEquipo = McLaren
    if seleccion == "Williams" :
        listaEquipo = Williams
    if seleccion == "AstonMartin" :
        listaEquipo = AstonMartin
    
    return listaEquipo

#clase que recibe la lista y la manda a la primer clase para iterarla
class ListaPilotos(Iterable):
    def __init__(self) -> None:
        self.listapropia = listaEquipo
    
    def __iter__(self) -> Iteraciones:
        return Iteraciones(self.listapropia)
