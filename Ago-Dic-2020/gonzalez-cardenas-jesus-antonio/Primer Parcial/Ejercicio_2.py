import sys
from Ejercicio_1 import Pista
def plugin_decorator(func):
    def get_lastfm_url(self,track:Pista):
        track_name = track.nombre.replace(" ", "+")
        track_artist = track.artist.replace(" ", "+")
        print(f"https://www.last.fm/music/{track_artist}/_/{track_name}")
        return func(self,track)
    return get_lastfm_url

def plugin_decorator2(func):
    def get_lyrics_url(self,track:Pista):
        track_name = track.nombre.replace(" ", "-")
        track_artist = track.artist.replace(" ", "-")
        print("lyrics:\n")
        print(f"https://genius.com/{track_artist}-{track_name}-lyrics")
        return func(self,track)
    return get_lyrics_url



class ReproductorMusical(object):
    def __init__(self, player_name: str, play_list: [], player_version: str):
        self.name = player_name
        self.track_list = play_list
        self.version = player_version
    
    
    @plugin_decorator2
    def add_pista(self, track:Pista):
        self.track_list.append(track)
    
    @plugin_decorator
    def remove_pista(self, track:Pista):
        isit = track in self.track_list
        self.track_list.remove(track)

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
        print(ply_listy[counter].get_nombre())
        print(ply_listy[counter].get_starred())
        print(ply_listy[counter].get_lenght())
        print(ply_listy[counter].get_artist() + "\n")
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
    
        

