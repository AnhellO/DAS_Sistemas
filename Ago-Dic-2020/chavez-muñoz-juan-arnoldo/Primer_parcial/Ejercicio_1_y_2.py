class Pista(object):# modelar una pista musical (cancion)
    def __init__(self, nombre, favorita, duracion, artista):
        self.nombre = nombre     #Srting
        self.favorita = favorita #tipo boolean
        self.duracion = duracion #tipo float
        self.artista = artista   #String

    #Getters and Setters
    def set_name_song(self, nombre):
        self.nombre = nombre

    def set_favorita(self, favorita):
        self.favorita = favorita

    def set_duracion(self, duracion):
        self.duracion = duracion
        
    def set_artista(self, artista):
        self.artista = artista

    def get_name_song(self):
        return self.nombre

    def get_favorita(self):
        return self.favorita

    def get_duracion(self):
        return self.duracion

    def get_artista(self):
        return self.artista

    #Funciones extra
    def hit_of_the_month():
        return "The hit of the month is:\n'Jump' from the legendary group called 'Van Hallen', check it out now!"

    def song_of_the_week():
        return "The song of the week is:\n'Safaera' from Bad Bunny, (I know, the people are stupid) anyway, play it now!"

class ReproductorMusical(Pista): #modelar un objeto "disco" de la vida real
    def __init__(self, disk_list, disk_price, disk_name):
        self.disk_list = disk_list
        self.disk_price = disk_price
        self.disk_name = disk_name
        
    #Una función que nos permita agregar pistas a una instancia de la clase
    #después de usar add_track, pasar como parámetro llenando_pistas() (hacerle unpacking)
    #y el otro parámetro será la lista para que sean los 5 elementos que recibe add_track()
    def add_track(name, fav, duration, artist, list) -> list:
        list.append(Pista(name, fav, duration, artist))
        return list

    # *********AQUÍ SE ENCUENTRAN LOS DECORADORES*********
    def page_artist(function):
        def wrapper(list):
            for elem in list:
                print(f"La página del artista {elem.artista} es: www.{elem.artista}.com.mx")
            return function
        return wrapper

    def charging_lyrics(function):
        def wrapper(list):
            print(f"Las letras de la canción {list[0].nombre} se están cargando...")
            return function
        return wrapper

    #Función decorada que nos devuelva todas las pistas marcadas como favoritas en el reproductor musical
    #Además de incluir la página web del artista
    @page_artist
    def return_favs(list) -> list:
        favoritas_list = []
        for pista_obj in list:
            if (pista_obj.favorita == True):
                favoritas_list.append(pista_obj.get_name_song)    
        return favoritas_list

    #Finalmente, agrega una última función (decorada) que nos devuelva todas las pistas por orden de duracion
    #Y también carga las lyrics de su respectiva pista
    @charging_lyrics
    def pistas_por_orden(list) ->list:
        return sorted(list, key=lambda Pista : Pista.duracion)


if __name__ == "__main__":
    #Acá se guardan todas las pistas
    lista = []
    #Creamos dinamicamente las pistas
    def llenando_pistas():
        name = input('Nombre de la canción: ')
        fav = input("escribe t si es True, otra cosa si es False: ")
        if fav.lower() == 't':
            fav = True
        else:
            fav = False
        duration = float(input('Duracion: '))
        artist = input('Nombre del artista: ')
        return name, fav, duration, artist


    ReproductorMusical.add_track(*llenando_pistas(),lista)
    ReproductorMusical.add_track(*llenando_pistas(),lista)
    print(ReproductorMusical.return_favs(lista))
    print(ReproductorMusical.pistas_por_orden(lista))