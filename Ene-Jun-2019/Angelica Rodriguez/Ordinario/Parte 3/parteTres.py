import peewee
import datetime
from mailchimp3 import MailChimp


db = peewee.SqliteDatabase('db_otaku.db') # usamos orm peewee

class Animes(peewee.Model):
    # animes
    title = peewee.TextField()
    episodes = peewee.IntegerField()
    duration = peewee.TextField()
    rating = peewee.TextField()
    synopsis = peewee.TextField()
    image_url = peewee.TextField()
    status = peewee.TextField()

    class Meta:
        database = db
        db_table = 'ANIME'

class Mangas(peewee.Model):
    # mangas
    title = peewee.TextField()
    status = peewee.TextField()
    image_url = peewee.TextField()
    synopsis = peewee.TextField()
    chapters = peewee.IntegerField()

    class Meta:
        database = db
        db_table = 'MANGA'

class Characters(peewee.Model):
    name = peewee.TextField()
    about = peewee.TextField()
    image_url = peewee.TextField()

    class Meta:
        database = db
        db_table = 'CHARACTERS'


def main():

    list_of_animes = [] # lista para guardar animes
    animes = Animes.select(Animes.title, Animes.episodes, Animes.duration, Animes.rating, Animes.synopsis, Animes.image_url, Animes.status)

    for anime in animes:
        anime_dictionary = {}
        anime_dictionary['title'] = anime.title
        anime_dictionary['episodes'] = anime.episodes
        anime_dictionary['duration'] = anime.duration
        anime_dictionary['rating'] = anime.rating
        anime_dictionary['synopsis'] = anime.synopsis
        anime_dictionary['image_url'] = anime.image_url
        anime_dictionary['status'] = anime.status
        list_of_animes.append(anime_dictionary) # guardamos anime


    list_of_mangas = [] # lista para guardar mangas
    mangas = Mangas.select(Mangas.title, Mangas.status, Mangas.image_url, Mangas.synopsis, Mangas.chapters)
    for manga in mangas:
        manga_dictionary = {}
        manga_dictionary['title'] = manga.title
        manga_dictionary['status'] = manga.status
        manga_dictionary['image_url'] = manga.image_url
        manga_dictionary['synopsis'] = manga.synopsis
        manga_dictionary['chapters'] = manga.chapters
        list_of_mangas.append(manga_dictionary) # guardamos manga


    list_of_characters = [] # lista para guardar personajes
    personajes = Characters.select(Characters.name, Characters.about, Characters.image_url)
    for personaje in personajes:
        character_dictionary = {}
        character_dictionary['name'] = personaje.name
        character_dictionary['about'] = personaje.about
        character_dictionary['image_url'] = personaje.image_url
        list_of_characters.append(character_dictionary) # guardamos personaje


        # empezamos a crear el archivo html extrayendo información de las listas creadas anteriormente
    string_html = """<!DOCTYPE html>
        <html>
            <head>
                <meta charset="UTF-8" name="viewport" content="width=device-width, initial-scale=1">
                    <title>Marketing</title>
                    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
                    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.0/jquery.min.js"></script>
                    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
                    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
                    <script>
                    document.getElementsByClassName('texto').replace(/(?:\\[rn])+/g, "<br>");
                    </script>
            </head>

            <body style="background-color:white;">
            <br><h1 align="center">Otaku site</h1>
            <br><p align="center" style="font-size:17px;">We invite you to be an <i>otaku</i>!! Here you can see the new animes, mangas and know interesting facts
            about some characters that appear on them!!</p>
            <br><br><br><table align="center" style="width:80%" class="table table-striped">
                <thead style="background-color:indigo; color:white;" class="thead-black">
                    <tr>
                        <th>Anime</th>
                        <th>Information</th>
                    </tr>
                </thead>"""
    for anime in list_of_animes:
        string_html += "<tbody><tr><td>"+anime['title']+"<img class='rounded-lg' src='" + anime['image_url'] + "'></td><td style='text-align:justify' class='texto'><b>Episodes:</b> " + str(anime['episodes']) + "<br><b>Duration:</b> " + anime['duration'] + "<br><b>Rating:</b> " + anime['rating'] + "<br><b>Synopsis:</b> " + anime['synopsis'] + "<br><b>Status:</b> " + anime['status'] + "</td></tr>"

    string_html += """</tbody></table><br><br><br><table align="center" style="width:80%" class="table table-striped">
    <thead style="background-color:indigo; color:white;" class="thead-black">
            <tr>
                <th>Manga</th>
                <th>Information</th>
            </tr>
        </thead>"""

    for manga in list_of_mangas:
        string_html += "<tbody><tr><td>" + manga['title'] + "<img class='rounded-lg' src='" + manga['image_url'] + "'></td><td style='text-align:justify' class='texto'><b>Status: </b>"+manga['status'] +"<br><b>Chapters: </b>" + str(manga['chapters']) + "<br><b>Synopsis: </b>"+ manga['synopsis'] + "</td></tr>"

    string_html += """</tbody></table><br><br><br><table align="center" style="width:80%" class="table table-striped">
        <thead style="background-color:indigo; color:white;" class="thead-black">
            <tr>
                <th>Character</th>
                <th>Information</th>
            </tr>
        </thead>"""

    for character in list_of_characters:
        string_html += "<tbody><tr><td>" + character['name']  + "<img class='rounded-circle' src='" + character['image_url'] + "'></td><td style='text-align:justify; class='texto'>"+character['about'] +"</td></tr>"

    string_html += "</tbody></table></body></html>"
    f = open("otaku_marketing.htm", "a")
    f.write(string_html)
    f.close()

    client = MailChimp(mc_api='3094e19582b69b6cfc001555b6ef170b-us20', mc_user='angiie_rdzc')

    client.campaigns.create(data={"type": "regular",
                                  "recipients":  {
                                     "list_id": "8dbaa21fc4"
                                     },
                                     "settings":
                                    {
                                    "subject_line": "none",
                                    "from_name": "Angelica Rodriguez",
                                    "reply_to": "angelica_marc@hotmail.com",
                                    "preview_text": "hola"
                                    },
                                    "content_type": "html",
                                    "segment_text": "hola",})
    print(client.campaigns.all(get_all=True))

    client.campaigns.actions.send(campaign_id='3cc60f4b52')

if __name__ == "__main__":
    main()
