from peewee import *

db = SqliteDatabase('Jikan.db')

class Anime(Model):
    id = IntegerField()
    title = TextField()
    episodes = IntegerField()
    status = TextField()

    class Meta:
        database = db
        db_table = 'Anime'

    def __str__(self):
        return 'Titulo: {} \nEpisodios: {} \nEstatus: {}\n'.format(self.title, self.episodes, self.status)

class Manga(Model):
    id = IntegerField()
    title = TextField()
    chapters = IntegerField()
    status = TextField()

    class Meta:
        database = db
        db_table = 'Manga'


    def __str__(self):
        return 'Titulo: {} \nCapitulos: {} \nEstatus: {}\n'.format(self.title, self.chapters, self.status)

class Personaje(Model):
    id = IntegerField()
    name = TextField()
    image_url = TextField()

    class Meta:
        database = db
        db_table = 'Character'

    def __str__(self):
        return 'Nombre: {} \nImagen: {} \n'.format(self.name, self.image_url)

class main():
    animes = []
    animes.append(Anime.get(Anime.title == 'Cowboy Bebop'))
    animes.append(Anime.get(Anime.title == 'Cowboy Bebop: Tengoku no Tobira'))
    animes.append(Anime.get(Anime.title == 'Trigun'))
    animes.append(Anime.get(Anime.title == 'Witch Hunter Robin'))
    animes.append(Anime.get(Anime.title == 'Bouken Ou Beet'))
    animes.append(Anime.get(Anime.title == 'Naruto'))
    animes.append(Anime.get(Anime.title == 'Neon Genesis Evangelion'))
    animes.append(Anime.get(Anime.title == 'Aa! Megami-sama! (TV)'))
    animes.append(Anime.get(Anime.title == 'Chrno Crusade'))
    animes.append(Anime.get(Anime.title == 'Mobile Suit Gundam'))
    print(animes)

    mangas = []
    mangas.append(Manga.get(Manga.title == 'Monster'))
    mangas.append(Manga.get(Manga.title == '20th Century Boys'))
    mangas.append(Manga.get(Manga.title == 'Yokohama Kaidashi Kikou'))
    mangas.append(Manga.get(Manga.title == 'Full Moon wo Sagashite'))
    mangas.append(Manga.get(Manga.title == 'Tsubasa: RESERVoir CHRoNiCLE'))
    mangas.append(Manga.get(Manga.title == 'xxxHOLiC'))
    mangas.append(Manga.get(Manga.title == 'Angelic Layer'))
    mangas.append(Manga.get(Manga.title == 'Prism Palette'))
    mangas.append(Manga.get(Manga.title == 'Air Gear'))
    mangas.append(Manga.get(Manga.title == 'Bleach'))
    print(mangas)


    personajes = []
    personajes.append(Personaje.get(Personaje.name == 'Spike Spiegel'))
    personajes.append(Personaje.get(Personaje.name == 'Faye Valentine'))
    personajes.append(Personaje.get(Personaje.name == 'Jet Black'))
    personajes.append(Personaje.get(Personaje.name == 'Ein'))
    personajes.append(Personaje.get(Personaje.name == 'Ichigo Kurosaki'))
    personajes.append(Personaje.get(Personaje.name == 'Rukia Kuchiki'))
    personajes.append(Personaje.get(Personaje.name == 'Orihime Inoue'))
    personajes.append(Personaje.get(Personaje.name == 'Hevn'))
    personajes.append(Personaje.get(Personaje.name == 'Silva Zoldyck'))
    personajes.append(Personaje.get(Personaje.name == 'Rei Ayanami'))
    print(personajes)

if __name__ == '__main__':
    main()
