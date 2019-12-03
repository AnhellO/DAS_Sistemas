#Este archivo usa peewee como ORM
import peewee
import pprint
import Episodios
import Locaciones
import Personaje

db = peewee.SqliteDatabase('Rick&Morty.db')
# tablitas = db.get_tables()
# print(tablitas)
# episodios = db.get_columns('episodios')
# pprint.pprint(episodios)
# datos = peewee.Select(episodios)
    
class locaciones(peewee.Model):
    fecha_creacion = peewee.TextField()
    dimension = peewee.TextField()
    id_locacion = peewee.TextField()
    nombre = peewee.TextField()
    residentes = peewee.TextField()
    tipo = peewee.TextField()
    url = peewee.TextField(unique=True)

    class Meta:
        database = db
        db_table = 'locaciones'

class episodios(peewee.Model):
    fecha_lanzamiento = peewee.TextField()
    personajes = peewee.TextField()
    fecha_creacion = peewee.TextField()
    episodio = peewee.TextField()
    id_episodio = peewee.TextField()
    nombre = peewee.TextField()
    url = peewee.TextField(unique=True)

    class Meta:
        database = db
        db_table = 'episodios'


class personajes(peewee.Model):

    fecha_creacion = peewee.TextField()
    episodios_apariciones_url = peewee.TextField()
    episodios_apariciones_numero = peewee.TextField()
    genero = peewee.TextField()
    id_personaje = peewee.TextField()
    imagen = peewee.TextField()
    locacion_name = peewee.TextField()
    locacion_url = peewee.TextField()
    nombre = peewee.TextField()
    origen_name = peewee.TextField()
    origen_url = peewee.TextField()
    especie = peewee.TextField()
    status = peewee.TextField()
    tipo = peewee.TextField()
    url = peewee.TextField()

    class Meta:
        database = db
        db_table = 'personajes'


# def create_conect():
#     db.connect()
#     db.create_tables([locaciones, episodios], safe=True)

# create_conect()

def get_episodios():
    query = episodios.select(episodios.fecha_lanzamiento, episodios.personajes, episodios.fecha_creacion, episodios.episodio, episodios.id_episodio, episodios.nombre, episodios.url)
    lista = []
    for epi in query:
        taco = Episodios.episodio(epi.fecha_lanzamiento, epi.personajes, epi.fecha_creacion, epi.episodio, epi.id_episodio, epi.nombre, epi.url)
        lista.append(taco)
    return lista

def get_locations():
    query = locaciones.select(locaciones.fecha_creacion, locaciones.dimension, locaciones.id_locacion, locaciones.nombre, locaciones.residentes, locaciones.tipo, locaciones.url)
    lista = []
    for loc in query:
        tamal = Locaciones.locacion(loc.fecha_creacion, loc.dimension, loc.id_locacion, loc.nombre, loc.residentes, loc.tipo, loc.url)
        lista.append(tamal)
    return lista

def get_personajes():
    query = personajes.select(personajes.fecha_creacion, personajes.episodios_apariciones_url, personajes.episodios_apariciones_numero, personajes.genero, personajes.id_personaje, personajes.imagen, personajes.locacion_name, personajes.locacion_url, personajes.nombre, personajes.origen_name, personajes.origen_url, personajes.especie, personajes.status, personajes.tipo, personajes.url)
    lista = []
    for per in query:
        burrito = Personaje.personaje(per.fecha_creacion, per.episodios_apariciones_url, per.episodios_apariciones_numero, per.genero, per.id_personaje, per.imagen, per.locacion_name, per.locacion_url, per.nombre, per.origen_name, per.origen_url, per.especie, per.status, per.tipo, per.url)
        lista.append(burrito)
    return lista

def get_episodio_especifico(id_epi):
    query = episodios.select(episodios.fecha_lanzamiento, episodios.personajes, episodios.fecha_creacion, episodios.episodio, episodios.id_episodio, episodios.nombre, episodios.url).where(episodios.id_episodio == id_epi)
    lista = []
    for epi in query:
        taco = Episodios.episodio(epi.fecha_lanzamiento, epi.personajes, epi.fecha_creacion, epi.episodio, epi.id_episodio, epi.nombre, epi.url)
        lista.append(taco)
    return lista

def get_locations_especifico(id_loc):
    query = locaciones.select(locaciones.fecha_creacion, locaciones.dimension, locaciones.id_locacion, locaciones.nombre, locaciones.residentes, locaciones.tipo, locaciones.url).where(locaciones.id_locacion == id_loc)
    lista = []
    for loc in query:
        tamal = Locaciones.locacion(loc.fecha_creacion, loc.dimension, loc.id_locacion, loc.nombre, loc.residentes, loc.tipo, loc.url)
        lista.append(tamal)
    return lista

def get_personaje_especifico(id_per):
    query = personajes.select(personajes.fecha_creacion, personajes.episodios_apariciones_url, personajes.episodios_apariciones_numero, personajes.genero, personajes.id_personaje, personajes.imagen, personajes.locacion_name, personajes.locacion_url, personajes.nombre, personajes.origen_name, personajes.origen_url, personajes.especie, personajes.status, personajes.tipo, personajes.url).where(personajes.id_personaje == id_per)
    lista = []
    for per in query:
        burrito = Personaje.personaje(per.fecha_creacion, per.episodios_apariciones_url, per.episodios_apariciones_numero, per.genero, per.id_personaje, per.imagen, per.locacion_name, per.locacion_url, per.nombre, per.origen_name, per.origen_url, per.especie, per.status, per.tipo, per.url)
        lista.append(burrito)
    return lista

##############################################################################################
#########################   Aqui empieza la creacion de HTML    ##############################
##############################################################################################

def Hacer_HTML_Tablas():
    tablitas = db.get_tables()
    content = """
        
        <h>Tablas:</h1>
        <br>
        <ul>
        <li><a href="Episodios/index.html">{}</a></li><br>
        <li><a href="Locaciones/index.html">{}</a></li><br>
        <li><a href="Personajes/index.html">{}</a></li>
        </ul>
        """.format(tablitas[0], tablitas[1], tablitas[2])
    archivo = open('index.html', 'w')
    archivo.write(content)
    archivo.close()

def Hacer_HTML_Episodios():
    episo = get_episodios()
    content = ''
    for i in range(0, len(episo)):

        cap = episo[i]
        dato = """
            <p>Id_Episodio: {} </p>
            <p>Nombre: <a href="capitulos/capitulo_{}.html">{}</a> </p> 

            <p>------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------</p>
            """.format(cap._Id_Episodio, (i+1), cap._Nombre)
        content += dato

    archivo = open('Episodios/index.html', 'w')
    archivo.write(content)
    archivo.close()

def Hacer_HTML_Episodios_Especs():
    episo = get_episodios()
    for i in range(0, len(episo)):

        cap = episo[i]
        content = """
            <p>Fecha de Lanzamiento: {} </p>
            <p>Personajes: {} </p> 
            <p>Fecha de Creacion: {} </p> 
            <p>Episodio: {} </p> 
            <p>Id_Episodio: {} </p>
            <p>Nombre: {} </p> 
            <p>Url: {} </p> 
            """.format(cap._FechaLanzamiento, cap._Personajes, cap._FechaCreacion, cap._CodEpisodio, cap._Id_Episodio, cap._Nombre, cap._URL)
        
        archivo = open('Episodios/capitulos/capitulo_{}.html'.format((i+1)), 'w')
        archivo.write(content)
        archivo.close()

def Hacer_HTML_Locaciones():
    loc = get_locations()
    content =''
    for i in range(0, len(loc)):
        lugar = loc[i]
        dato = """
            <p>Id_Locacion: {} </p>
            <p>Nombre: <a href="lugares/locacion_{}.html">{}</a> </p> 
            <p>------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------</p>
            """.format(lugar._Id_Locacion,(i+1), lugar._Nombre)
        content += dato
    archivo = open('Locaciones/index.html', 'w', encoding='utf-8')
    archivo.write(content)
    archivo.close()

def Hacer_HTML_Locaciones_Especs():
    loc = get_locations()
    for i in range(0,len(loc)):
        lugar = loc[i]
        content = """
            <p>Fecha_Creacion: {}</p>
            <p>Dimension: {}</p>
            <p>Id_Locacion: {}</p>
            <p>Nombre: {}</p>
            <p>Residentes: {}</p>
            <p>Tipo: {}</p>
            <p>URL: {}</p>
            """.format(lugar._FechaCreacion, lugar._Dimension, lugar._Id_Locacion, lugar._Nombre, lugar._Residentes, lugar._Tipo, lugar._URL)
        archivo = open('Locaciones/lugares/locacion_{}.html'.format((i+1)), 'w', encoding='utf-8')
        archivo.write(content)
        archivo.close()


def Hacer_HTML_Personajes():
    person = get_personajes()
    content =''
    for i in range(0, len(person)):
        character = person[i]
        dato = """
            <p>Id_Personaje: {} </p>
            <p>Nombre: <a href="personajes/personaje_{}.html">{}</a> </p> 
            <p>------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------</p>
            """.format(character._Id_Personaje,(i+1), character._Nombre)
        content += dato
    archivo = open('Personajes/index.html', 'w', encoding='utf-8')
    archivo.write(content)
    archivo.close()

def Hacer_HTML_Personajes_Especs():
    person = get_personajes()
    for i in range(0,len(person)):
        character = person[i]
        content = """
            <p>FechaDeCreacion: {}</p>
            <p>EpisodiosDondeAparece: {}</p>
            <p>NumeroEpisodiosDondeAparece: {}</p>
            <p>Genero: {}</p>
            <p>Id_Personaje: {}</p>
            <p>Imagen: {}</p>
            <p>Location_Name: {}</p>
            <p>Location_URL: {}</p>
            <p>Nombre: {}</p>
            <p>Origen_Name: {}</p>
            <p>Origen_URL: {}</p>
            <p>Especie: {}</p>
            <p>Status: {}</p>
            <p>Tipo: {}</p>
            <p>URL: {}</p>
            """.format(character._FechaDeCreacion, character._EpisodiosDondeAparece, character._NumeroEpisodiosDondeAparece, character._Genero, character._Id_Personaje, character._Imagen, character._Location_Name, character._Location_URL, character._Nombre, character._Origen_Name, character._Origen_URL, character._Especie, character._Status, character._Tipo, character._URL)
        archivo = open('Personajes/personajes/personaje_{}.html'.format((i+1)), 'w', encoding='utf-8')
        archivo.write(content)
        archivo.close()


    # print(tablitas)
# waa = get_episodios()
# waa = get_locations
# waa = get_personajes()
# print(len(waa))
# print(waa[2])

if __name__ == '__main__':
    Hacer_HTML_Tablas()
    Hacer_HTML_Episodios()
    Hacer_HTML_Episodios_Especs()
    Hacer_HTML_Locaciones()
    Hacer_HTML_Locaciones_Especs()
    Hacer_HTML_Personajes()
    Hacer_HTML_Personajes_Especs()
    # waa = get_episodio_especifico(2)
    # waa = get_locations_especifico(2)
    # waa = get_personaje_especifico(1)
    # print(waa[0])







#Pruebas Crear un HTML
#{
# waa = get_episodios()
# cap1 = waa[0]
# content = """
#         <p>Fecha de Lanzamiento: {} </p> <br>
#         <p>Personajes: {} </p> <br>
#         <p>Fecha de Creacion: {} </p> <br>
#         <p>Episodio: {} </p> <br>
#         <p>Id_Episodio: {} </p> <br>
#         <p>Nombre: {} </p> <br>
#         <p>Url: {} </p> <br>
#         """.format(cap1._FechaLanzamiento, cap1._Personajes, cap1._FechaCreacion, cap1._CodEpisodio, cap1._Id_Episodio, cap1._Nombre, cap1._URL)

# archivo = open('index.html', 'w')
# archivo.write(content)
# archivo.close()
#}
#Esto si funciona, es para hacer un html con los datos de 1 episodio :3