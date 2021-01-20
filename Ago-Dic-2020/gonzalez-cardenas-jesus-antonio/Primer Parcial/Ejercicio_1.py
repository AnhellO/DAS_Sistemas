import random

class Pista(object):
    def __init__(self, nombre:str, starred:bool, lenght:str, artist: str):
        self.nombre = nombre
        self.starred = starred
        self.lenght = lenght
        self.artist = artist

    def set_nombre(self,name_input:str):
        self.nombre = name_input
    
    def set_starred(self, starred_input:bool):
        self.starred = starred_input

    def set_lenght(self, lenght_input:str):
        self.lenght = lenght_input

    def set_artist(self, artist_input:str):
        self.artist = artist_input
    
    def get_nombre(self):
        return self.nombre

    def get_starred(self):
        return self.starred

    def get_lenght(self):
        return self.lenght

    def get_artist(self):
        return self.artist

    def add_genre(self, genre:str):
        self.nombre = f"{self.nombre} - {genre}"
        print(f"Se añadió el genero al track")

    def get_review(self):
        stars = random.randint(0,10)
        if stars < 6:
            return f"La canción apesta"
        else:
            return f"La canción es muy buena"



class ReproductorMusical(object):
    def __init__(self, player_name: str, play_list: [], player_version: str):
        self.name = player_name
        self.track_list = play_list
        self.version = player_version

    def add_pista(self, track:Pista):
        self.track_list.append(track)
        
    def remove_pista(self, track:Pista):
        is_in = track in self.track_list
        if is_in:
            self.track_list.remove(track)
        else:
            return f"No se puede borrar ese track, no esta en la playlist"
        pass

    def get_starred_tracks(self):
        aux_list = []
        counter = 0
        for i in self.track_list:
            if self.track_list[counter].get_starred():
                aux_list.append(self.track_list[counter])
            counter = counter+1
        
        return aux_list

    

def print_pistas(ply_listy: []):
    counter = 0
    for i in ply_listy:
        print(f"{ply_listy[counter].get_nombre()} - {ply_listy[counter].get_artist()} - {ply_listy[counter].get_lenght()} - Favorita = {ply_listy[counter].get_starred()}")
        counter = counter + 1
    print("----------------------------------------------------------------------------------------------------------")


def main():
    track1 = Pista("Come together", False, "4:19", "The Beatles")
    track2 = Pista("Something", True, "3:02", "The Beatles")
    track3 = Pista("Maxwell's Silver Hammer", False, "3:27", "The Beatles")
    track4 = Pista("Oh! Darling", False, "3:27", "The Beatles")
    track5 = Pista("Octopus Garden", True, "2:51", "The Beatles")
    
    music_list = []
    music_list.append(track1)
    music_list.append(track2)
    music_list.append(track3)
    music_list.append(track4)
    music_list.append(track5)
     
    music_plyr = ReproductorMusical("Python Player", music_list, "1.0")
    print_pistas(music_plyr.track_list)
    starred_music_list = music_plyr.get_starred_tracks()
    print_pistas(starred_music_list)
    
    track6 = Pista("I Want You (She's So Heavy)", True, "7:47", "The Beatles")
    music_plyr.add_pista(track6)
    music_plyr.remove_pista(track3)
    print_pistas(music_plyr.track_list)
    
if __name__=="__main__":
    main()
    