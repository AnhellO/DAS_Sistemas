from bs4 import BeautifulSoup
import requests
from Usuario import Usuario
from StackEntryFeed  import *
import feedparser
from orm import *
import time

####################################################################


#############~ OBTENER EL SOUP Y EL FEED DE LA PREGUNTA

#~ Los url de las preguntas

#~ url = "https://stackoverflow.com/questions/89228/calling-an-external-command-in-python?rq=1"
#~ url = 'https://stackoverflow.com/questions/43120445/scraping-a-webpage-that-has-javascript-with-beautifulsoup'







class SetAll():
    

    def __init__(self,url):
        self.__url = url


    def set_all(self):

        #~ El soup
        soup = BeautifulSoup(requests.get(self.__url).text,'lxml')

        #~ El url del feed para extraer los datos
        url_feed = soup.find(id ='feed-link-text')
        url_feed = 'https://stackoverflow.com' + url_feed.a['href']

        #~ Creamos el feedparser
        feed = feedparser.parse(url_feed)

        #~ Feed para usuarios  y pregunta
        e = feed.entries

        #~ Feed para respuestas
        r = feed.entries


        print('PROCEDIMIENTO DE AGREGADO A BASE DE DATOS')

        #~ PRIMERO SE DEBEN AGREGAR LOS USUARIOS, DESPUÉS LAS PREGUNTAS Y POR ÚLTIMO LAS
        #~ RESPUESTAS

        #~ Para agregar usuarios a la base de datos, creamos un objeto de la clase Usuario
        #~ para obtener la biografía y las comunidades, y del feed se obtiene nombre, idusuario y
        #~ el link del usuario

        #~ nombre,biografia,comunidades,idusuario,linkuser -> atributos clase Usuario


        #########################################################

        lista_users = []
        print(len(e))
        for i in range(len(e)):
            if e[i].author not in lista_users:
                lista_users.append(e[i].author)
            else:
                e.remove(e[i])

        print(len(e))

        for i in e:
            print(i.author_detail.name)

        #nombre,biografia,comunidades,idusuario,linkuser -> Atributos ORM clase User
        orm = OrmFactory()
        for usuario in e:
            u = StackEntryFeed(usuario)
            us = Usuario(u.get_user_uri(),u.get_username(),u.get_user_id())
            orm.agregaUsuario(u.get_username(),us.get_bio(),''.join(us.get_comunidades()),u.get_user_id(),u.get_user_uri())


        ################################################################


        #########################~ AGREGAR PREGUNTA

        #~ id,pregunta,explicacion,userid,linkpregunta -> atributos de pregunta

        #~ Agregar pregunta

        pregunta = StackEntryFeed(e[0])
        orm.agregaPregunta(pregunta.get_id(),pregunta.get_title(),pregunta.get_summary_detail(),pregunta.get_user_id(),feed.feed.link)


        #######################################################################

        #~ ######################AGREGANDO RESPUESTAS

        #~ Esta variable es para las respuestas (el foreign key que conecta las respuestas
        #~ con las preguntas
        preguntaid = pregunta.get_id()

        #~ idpregunta,respuesta,fecha,idusuario,linkrespuesta -> Atributos de la clase Answer
        #~ Loop para agregar respuestas

        a = 0
        for entry in r:
            print('AGREGANDO RESPUESTA')
            res = StackEntryFeed(entry)
            orm.agregaRespuesta(preguntaid,res.get_summary_detail(),res.get_fecha_publicacion(),res.get_user_id(),res.get_entry_link())
            time.sleep(3)
