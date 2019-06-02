import peewee
import os
from mailchimp3 import MailChimp

""" Como se pide en las especificaciones del proyecto, se utiliza
ORM para traer los datos de la base de datos creada en la parte 1.
En este caso utilizaremos peewee """

#Se hace la conexion a la base de datos
db = peewee.SqliteDatabase('AnimeMangaCharacter.db')

#Definomos un modelo de base de datos llamado Anime, que hereda de peewee.Model
class Anime(peewee.Model):
    #A continuacion especificamos los campos del modelo
    id = peewee.IntegerField()
    clave = peewee.IntegerField()
    title = peewee.CharField()
    rango = peewee.IntegerField()
    url = peewee.CharField()
    url_image = peewee.CharField()
    type = peewee.CharField()
    episodes = peewee.IntegerField()
    start_date = peewee.CharField()
    end_date = peewee.CharField()
    members = peewee.IntegerField()
    score = peewee.FloatField()

    class Meta:
        """En la Meta clase, definimos la referencia a la base de datos
        y el nombre de la tabla de la base de datos"""

        database = db
        db_table = 'animes'

class Manga(peewee.Model):

    id = peewee.IntegerField()
    clave = peewee.IntegerField()
    title = peewee.CharField()
    rango = peewee.IntegerField()
    url = peewee.CharField()
    url_image = peewee.CharField()
    type = peewee.CharField()
    volumes = peewee.IntegerField()
    start_date = peewee.CharField()
    end_date = peewee.CharField()
    members = peewee.IntegerField()
    score = peewee.FloatField()

    class Meta:

        database = db
        db_table = 'mangas'

class Character(peewee.Model):

    id = peewee.IntegerField()
    clave = peewee.IntegerField()
    title = peewee.CharField()
    name_kanji = peewee.CharField()
    rango = peewee.IntegerField()
    url = peewee.CharField()
    url_image = peewee.CharField()

    class Meta:

        database = db
        db_table = 'characters'

def agruparAnimes(lista):
    animes = []
    for i in lista:
        dic = {
        'id':i.id,
        'clave': i.clave,
        'title':i.title,
        'rango':i.rango,
        'url': i.url,
        'url_image': i.url_image,
        'type': i.type,
        'episodes': i.episodes,
        'start_date':i.start_date,
        'end_date':i.end_date,
        'members':i.members,
        'score':i.score
        }
        animes.append(dic)
    return animes

def agruparMangas(lista):
    mangas = []
    for i in lista:
        dic = {
        'id':i.id,
        'clave': i.clave,
        'title':i.title,
        'rango':i.rango,
        'url': i.url,
        'url_image': i.url_image,
        'type': i.type,
        'volumes': i.volumes,
        'start_date':i.start_date,
        'end_date':i.end_date,
        'members':i.members,
        'score':i.score
        }
        mangas.append(dic)
    return mangas

"""Se crean métodos para agrupar los resultados obtenidos de la base de datos
(animes, mangas y personajes).
La estructura que se eligió fue: una lista de diccionarios"""

def agruparCharacters(lista):
    characters = []
    for i in lista:
        dic = {
        'id':i.id,
        'clave': i.clave,
        'title':i.title,
        'name_kanji':i.name_kanji,
        'rango':i.rango,
        'url': i.url,
        'url_image': i.url_image
        }
        characters.append(dic)
    return characters

"""Se define un método para escribir el HTML, el cual recibe como parametro el string
del html y se guarda en el archivo index.html"""
def fileHTML(data):
        fname = "index.html"
        if os.path.isfile(fname):
            os.remove(fname)

        with open(os.path.join(fname), 'w',encoding='utf-8') as file:
            file.write(data)

""" Se crea una clase Chimp para poder utilizar algunos métodos de la API
que seran necesarios para esta tercera parte """

class Chimp():
    def __init__(self):
        #Se inicializa el cliente con la api generada en la pagina web y nuestro usuario
        self.client = MailChimp(mc_api='591cd04cce86613128dc359476d8ac99-us20', mc_user='kberlanga')

    def createCampaing(self):
        #Se defien este método para crear campañas que nos servirán para hacer marketing
        data = {"recipients":{"list_id":"4fe4d84e7a"},"type":"regular","settings":{"subject_line":"Animes - Proyecto Final","reply_to":"karla_berlanga28@hotmail.com","from_name":"Animes"}}
        self.client.campaigns.create(data)

    def getCampaings(self):
        #Con este método, se pueden ver las campañas que tenemos registradas en la cuenta
        return self.client.campaigns.all(get_all=False)

    def content(self, id, data):
        """Este método se utiliza para cargar el contenido que tendra la campaña, es decir, el HTML
        recibe como parametro el id de la campaña a la que vamos a agregar el contenido y por supuesto
        el contenido que se agregara(string)"""
        self.client.campaigns.content.update(campaign_id=id, data=data)

    def test(self, id, data):
        """Este metodo se define para enviar un test de email, para verificar que todo funcione bien
        antes de enviar la campaña de email a todos los contactos. Recibe como parametros, la campaña que
        será enviada y un diccionario con el siguiente formato:
        {"test_emails":["email_al_que_sera_enviado@example.com"],"send_type":"html"}"""
        self.client.campaigns.actions.test(campaign_id=id, data=data)

    def send(self, id):
        """Este método es para enviar la campaña a todos los contactos de cierta campaña,
        para saber cuál, este método recibe como parametro el id de la campaña"""
        self.client.campaigns.actions.send(campaign_id=id)

def main():
    animes = Anime.select()
    mangas = Manga.select()
    characters = Character.select()

    l_animes = agruparAnimes(animes)
    l_mangas = agruparMangas(mangas)
    l_characters = agruparCharacters(characters)


    print("*********Animes*********")
    for anime in animes:
        print('{} {}'.format(anime.clave, anime.title))

    print("*********Mangas*********")
    for manga in mangas:
        print('{} {}'.format(manga.clave, manga.title))

    print("*********Characters*********")
    for character in characters:
        print('{} {}'.format(character.clave, character.title))

    agregar_animes= ""
    for i in range(5):
        agregar_animes+="""<div class='col-md-4'><div class='single-blog'>
        <img class=img-small src='"""+l_animes[i]['url_image']+"""'>
        <h2><a href='"""+l_animes[i]['url']+"""' target="_blank">"""+l_animes[i]['title']+"""</a></h2>
        </div></div>"""+'\n'

    agregar_mangas= ""
    for i in range(5):
        agregar_mangas+="""<div class='col-md-4'><div class='single-blog'>
        <img class=img-small src='"""+l_mangas[i]['url_image']+"""'>
        <h2><a href='"""+l_mangas[i]['url']+"""' target="_blank">"""+l_mangas[i]['title']+"""</a></h2>
        </div></div>"""+'\n'

    agregar_personajes= ""
    for i in range(5):
        agregar_personajes+="""<div class='col-md-4'><div class='single-blog'>
        <img class=img-small src='"""+l_characters[i]['url_image']+"""'>
        <h2><a href='"""+l_characters[i]['url']+"""' target="_blank">"""+l_characters[i]['title']+"""</a></h2>
        <p class='blog-center' style='text-align: center;'>Name Kanji: <br>"""+l_characters[i]['name_kanji']+"""</p>
        </div></div>"""+'\n'



        data ={'html':"""
        <html>
<head>
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
<style>

body
{
    background-color: #B8E1F9 !important;
}

h1,h2,h3{
  text-align: center;
}

.single-blog
{
    box-shadow: 0px 0px 20px 1px rgba(0, 0, 0, 0.2);
    padding: 10px;
    background-color: #fff;
    margin: 5px 10px 20px 10px;
}


.single-blog img
{
    width: 100%;
}


.img-small
{
    width: 100%;
    position: relative;
    top: 0;
    left: 0;
}

.blog-meta
{
    font-size: 14px;
    margin-bottom: 2px;
}

.single-blog span
{
    float: right;
    font-size: 12px;
    color: cornflowerblue;
}

.blog-text
{
    font-size: 14px;
    text-align: justify;
}

.single-blog h2
{
    margin-top: 10px;
    font-size: 16px;
    color: #007bff;

}

  /* Style the container */
  .container {
    border-radius: 5px;
    background-color: #f2f2f2;
    padding: 10px;
  }


</style>
</head>
<body>
  <div class='container' style='background-color:rgba(123, 124, 124, 0.3)'>
    <h1 style="font-size: 5vw; font-family:fantasy;">My Anime List</h1>
    <h2 style="font-size: 3vw; font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif; color:rgba(75,82,88,0.5);">Animes | Mangas | Personajes</h2>
  </div>

    <div class='container' id="container">
        <div class="row" id="row1">"""+agregar_animes+agregar_mangas+agregar_personajes+"""</div>
    </div>



  </div>

  <div class="container" style='background-color:rgba(192, 252, 0, 0.3)'>
      <h2 style="font-size: 1.5vw;">¿Quieres saber más? Visita nuestra página</h2>
      <h2 style="font-size: 1.8vw;"><a href= "https://myanimelist.net">MyAnimeList</a></h2>
    </div>

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
</body>
</html>
        """}

    #Se genera el archivo HTML
    fileHTML(data)
    mc = Chimp()
    #Se crea una campaña
    mc.createCampaing()
    #Se imprime, para verificar que se haya creado
    print(mc.getCampaings())
    #Se carga el contenido
    mc.content('2ffbe77ed4',data)
    #Se envía un test de prueba
    mc.test('2ffbe77ed4',{"test_emails":["karla_berlanga28@hotmail.com"],"send_type":"html"})
    #Se envía la campaña
    mc.send('2ffbe77ed4')


if __name__ == '__main__':
    main()
