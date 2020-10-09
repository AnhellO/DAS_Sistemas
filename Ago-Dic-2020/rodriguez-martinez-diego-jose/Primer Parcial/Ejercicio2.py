 ############   PISTA   ##################
########################################

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

 ############   PLUGIN  TIMER  ##################
########################################

import datetime

def plugin_timer(Cls):

    class Wrapper(object):
        def __init__(self,*args,**kwargs):
            self.instance = Cls(*args,**kwargs)

        def __getattribute__(self,s):

            try:    
                x = super(Wrapper,self).__getattribute__(s)
            except AttributeError:      
                pass
        
            else:
                return x

            x = self.instance.__getattribute__(s)

            if type(x) == type(self.__init__):
                return time_this(x)  
            else:
                return x

    return Wrapper

def time_this(original_function):      
                    
    def new_function(*args,**kwargs):
                 
        before = datetime.datetime.now()                     
        x = original_function(*args,**kwargs)                
        after = datetime.datetime.now()                      
        print("Tiempo de ejecucion = {0}".format(after-before))

        return x                                             
    return new_function  

 ############   PLUGIN  CHANGE BACKGROUND  ##################
########################################
import os
import platform

def plugin_changeBackground(original_function):      
    def new_function(*args,**kwargs):
        plt = platform.system()

        if plt == "Windows":
            os.system('color 1f')

        elif plt == "Linux":
            os.system('setterm -background blue -foreground white')
            # pass

        else:
            print("su sistema operativo no cuenta con soporte para este plugin")

        x = original_function(*args,**kwargs)                

        return x
    return new_function  


 ############   REPRODUCTOR   ##################
########################################

@plugin_timer
class ReproductorMusical():

    marca = "SONY"
    modelo = "2020"

    def __init__(self, canciones):
        self.play_queue = canciones
    
    @plugin_changeBackground
    def agregar_pista(self, cancion):
        self.play_queue.append(cancion)

    @property
    def informacion(self):
        return ", ".join([self.marca,self.modelo])
    
    def informacion_de_pistas(self):
        return "\n".join([cancion.informacion_cancion for cancion in self.play_queue])

    @plugin_changeBackground
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

    @plugin_changeBackground
    def get_canciones_favoritas(self):
        return [cancion._nombre for cancion in self.play_queue if cancion._favorita]

    @plugin_changeBackground
    def get_canciones(self):
        canciones = [cancion for cancion in self.play_queue]
        canciones.sort(key= lambda x: x._duracion)

        self.play_queue = canciones

        return [[cancion._nombre,cancion._artista, cancion._duracion] for cancion in canciones]


if __name__ == "__main__":
    canciones = [Pista(nombre = "Cancion1", favorita= True, duracion = 12, artista = "A"),
                Pista(nombre = "Cancion2", favorita= False, duracion = 10, artista = "B"),
                Pista(nombre = "Cancion3", favorita= True, duracion = 15, artista = "A"),
                Pista(nombre = "Cancion4", favorita= False, duracion = 120)]

    mReproductor = ReproductorMusical(canciones)
    print("CANCIONES FAVORITAS:\n", mReproductor.get_canciones_favoritas())
    print("PLAYLIST:\n", mReproductor.get_canciones())