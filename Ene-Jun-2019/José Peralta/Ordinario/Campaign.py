from peewee import *

db = SqliteDatabase('AniManga.db')
class Anime(Model):
    id = IntegerField()
    title = TextField()
    episodes = TextField()
    duration = TextField()
    rating = TextField()
    url = TextField()
    image = TextField()
    trailer = TextField()

    class Meta:
        database = db
        db_table = 'Anime'

    def __str__(self):
        return "Title: {}\nEpisodes: {}\nDuration: {}\nRating: {}\nLink: {}\nPoster: {}\nTrailer: {}".format(self.title,
        self.episodes, self.duration, self.rating, self.url, self.image, self.trailer)

class Manga(Model):
    id = IntegerField()
    title = TextField()
    type = TextField()
    volumes = TextField()
    chapters = TextField()
    url = TextField()
    image = TextField()

    class Meta:
        database = db
        db_table = 'Manga'

    def __str__(self):
        return "Title: {}\nType: {}\nVolumes: {}\nChapters: {}\nLink: {}\nCover: {}".format(self.title, self.type,
        self.volumes, self.chapters, serlf.url, self.image)

class Character(Model):
    id = IntegerField()
    name = TextField()
    image = TextField()

    class Meta:
        database = db
        db_table = 'Characters'

    def __str__(self):
        return 'Name: {}\nPhoto: {}'.format(self.name, self.image)

anime_list = []
# [125056, 90291, 417, 71, 22037, 2075, 24596, 41402, 4004, 85, 77605, 118739, 148622, 81367, 138441]
# for id in [1535, 1575, 14719, 30276, 31964, 1, 2001, 10087, 5114, 5081, 23273, 17265, 31478, 33352, 33255]:
#     anime_list.append(Anime.get(Anime.id == id))
#

if __name__ == '__main__':
    print(Anime.get(Anime.title == 'Death Note'))
