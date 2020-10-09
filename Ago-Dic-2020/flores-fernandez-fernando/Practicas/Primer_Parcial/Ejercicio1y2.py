
class Pista:
    def __init__(self,nombre,starred,length,author):
        self._nombre = nombre
        self._starred = starred
        self._length = length 
        self._author = author
    
    def get_nombre(self):
        return self._nombre
    
    def get_starred(self):
        return self._starred
    
    def get_length(self):
        return self._length
    
    def get_author(self):
        return self._author
    
    def set_nombre(self, nombre):
        self._nombre = nombre
    
    def set_starred(self,starred):
        self._starred = starred
    
    def set_lenght(self,lenght):
        self.lenght = lenght
    
    def set_author(self,author):
        self.author = author
    # guarda el objeto en un diccionario
    def ver_pista(self):
        dic = {}
        dic["Nombre"] = self._nombre
        dic["Starred"] = self._starred
        dic["Length"] = self._length
        dic["Author"] = self._author
        return dic 

    def author_pista(self):
        return f"el Autor de {self._nombre} es {self._author}"   



        

class ReproductorMusical:
    def __init__(self,playlist,where_listen_to,lyrics):
        self._playlist = playlist # guarda una lista con las pistas 
        self._where_listen_to = where_listen_to # guarda un string con el dispositivo en donde lo estas escuchando 
        self._lyrics = lyrics # guarda un string con fragmentos de la letra   
   
    def get_playlist(self):
        return self._playlist
    
    def set_playlist(self,lista):
        self._playlist = lista

    # agrega una pista nueva a la playlist
    #@plugin_add_lyric
    def add_track_to_playlist(self,track):
        lista = [self.get_playlist]
        lista.append(track)
        self.set_playlist(lista)


    # obtiene todas las canciones starred 
    #@plugin_add_where_listen_to
    def get_starred_playlist(self):
        list_starred= []
        for i in range(len(self._playlist)):
            if (self._playlist.Pista.get_starred == True):
                list_starred.append(self._playlist)

        return list_starred
    
    # obtiene las canciones por duracion
    def sort_length(self):
        sorted_length = self._playlist.sort(key= lambda k: (k[2]), reverse=True )
        return sorted_length
    
    #########################################ejercicio 2################################################
    # decorador para conocer a que dispositivo esta ordenando las pistas favoritas
    def plugin_add_where_listen_to(self,get_starred_playlist):
        def get_where_listen_to(self):
            return self._where_listen_to
        return get_where_listen_to
   
    # decorador para conocer añadir una lyric a la pista
    def plugin_add_lyric(self,get_starred_playlist):

        def get_lyric(self):
            return self.lyric
        return get_lyric
  
            
def main(): 

    #nombre = input("Nombre de la pista\n")
    #starred = bool(input("Su cancion es favorita? True o False\n"))
    #length = float(input("Duracion de la pista\n"))
    #author = input("Nombre del Autor\n")

    track = Pista("nombre",False,3.5,"author")

    disco = ReproductorMusical(track,"xbox","hola hola crayola")

    disco.add_track_to_playlist(track)

    lista = disco.get_starred_playlist()
    print(lista)


if __name__ == "__main__":
    main()