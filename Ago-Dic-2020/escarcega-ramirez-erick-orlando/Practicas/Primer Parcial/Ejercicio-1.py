class track(object):
  def __init__(self, name, starred, lenght, artist):
    self.name = name
    self.starred = starred
    self.lenght = lenght
    self.artist = artist

  def get_name(self):
    return self.name

  def get_starred(self):
    return self.starred

  def get_lenght(self):
    return self.lenght

  def get_artist(self):
    return self.artist

  def set_name(self, name):
    self.name = name

  def set_starred(self, starred):
    self.starred = starred

  def set_lenght(self, lenght):
    self.lenght = lenght

  def set_artist(self, artist):
    self.artist = artist

  def wizzard(self):
    print(f"The song {self.name.title()} which is {str(self.lenght)} minutes long, is really good!")

  def info(self):
    print(f"The song {self.name.title()} was performed by {self.artist.title()}")

class MusicApp(object):
  def __init__(self, playlist, data, score):
    self.songlist = playlist
    self.data = data
    self.score = score

  def add_song(self, song):
    self.songlist.append(song)

  def remove_song(self, song):
    self.songlist.remove(song)
