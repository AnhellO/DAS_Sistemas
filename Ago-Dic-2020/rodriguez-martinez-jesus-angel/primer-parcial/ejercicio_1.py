# Class that serves as a song.
class Pista():
    def __init__ (self, name: str, starred: bool, duration: int, release: str):
        self.name = name
        self.starred = starred
        self.duration = duration
        self.release = release
        self.stars = list()
    # Returns the song info.
    def get_info(self):
        return f"Name: {self.name} \nStarred: {self.is_favorite()} \nDuration: {self.duration} \nRelease: {self.release}"
    # Checks if the song is favorite and returns a message depending on the case.
    def is_favorite(self):
        if self.starred:
            return 'This is one of your favorite songs'
        return 'This is not one of your favorite songs'
    # Adds a new star to the stars list
    def add_star(self):
    # Remove the last star to the stars list
        self.stars.append('★')
    def remove_star(self):
        self.stars.pop()
    # Returns the stars list
    def get_stars(self):
        return 'Stars: ' + ''.join(self.stars)

# Class that serves as a music player.
class ReproductorMusical():
    def __init__(self, theme: str, background: str, duration: int):
        self.playlist = list()
        self.theme = theme
        self.background = background
        self.duration = duration

    # Getters.
    def get_duration(self):
        return self.duration
    def get_background(self):
        return self.background
    # Adds a new song to the playlist.
    def add_song(self, song):
        self.playlist.append(song)
    # Removes the last song from the playlist.
    def remove_last_song(self):
        self.playlist.pop()
    # Gets the songs that have been starred and order them.
    def get_favorite_songs(self):
        ordered_songs = list()
        for song in self.playlist:
            # Checks if the song is starred.
            if song.starred:
                ordered_songs.append(song)
        # Orders the song by duration.
        ordered_songs.sort(key=lambda song: song.duration, reverse=False)
        return ', '.join([song.name for song in ordered_songs])

if __name__ == "__main__":

    # Songs.
    # Naruto.
    naruto_opening = Pista('Naruto opening 5', True, 100,'2020-01-01')
    naruto_opening.add_star()
    naruto_opening.add_star()
    naruto_opening.add_star()
    print(naruto_opening.get_info())
    print(naruto_opening.get_stars())
    naruto_opening.remove_star()
    print(naruto_opening.get_stars())
    naruto_ending = Pista('Naruto shippuden opening 6',False, 50,'2020-02-02')
    # Saint seiya.
    saint_seiya_opening = Pista('Saint seiya lost canvas opening', True, 10,'2019-01-01')
    # Zankyou no terror ... VON ...
    zankyou_no_terror_ending = Pista('Zankyou no terror ending', True, 1050,'2030-01-01')

    # Reproductor.
    reproductor = ReproductorMusical('Icelandic', 'https://i.ytimg.com/vi/uVFGmjzQgW4/maxresdefault.jpg', 911)
    reproductor.add_song(naruto_opening)
    reproductor.add_song(naruto_ending)
    reproductor.add_song(saint_seiya_opening)
    reproductor.add_song(zankyou_no_terror_ending)
    ordered_songs = reproductor.get_favorite_songs()
    print(ordered_songs)