import peewee
import episodio
import ubicacion
import personaje

db = peewee.SqliteDatabase('Ordinario/BaseDatos/rickandmorty.db')

class personajes(peewee.Model):
    Id = peewee.TextField(unique=True)
    Nombre = peewee.TextField()
    Status = peewee.TextField()
    Species = peewee.TextField()
    Origin = peewee.TextField()
    Type = peewee.TextField()
    Location = peewee.TextField()
    id_locacion = peewee.TextField()
    Episode = peewee.TextField()
    id_episodio = peewee.TextField()
    Url = peewee.TextField()

    class Meta:
        database = db
        db_table = 'personajes'

class locaciones(peewee.Model):
    Id = peewee.TextField(unique=True)
    Nombre = peewee.TextField()
    Type = peewee.TextField()
    Dimension = peewee.TextField()
    Residents = peewee.TextField()
    id_personaje = peewee.TextField()
    Url = peewee.TextField()

    class Meta:
        database = db
        db_table = 'locaciones'

class episodios(peewee.Model):
    Id = peewee.TextField(unique=True)
    Nombre = peewee.TextField()
    air_date = peewee.TextField()
    Episode = peewee.TextField()
    Character = peewee.TextField()
    id_personaje = peewee.TextField()
    Url = peewee.TextField()

    class Meta:
        database = db
        db_table = 'episodios'

def base_datos():
    db.connect()
    db.create_tables([personajes,locaciones,episodios],safe=True)

def traer_personaje():
    query = personajes.select(personajes.Id,personajes.Nombre,personajes.Status,personajes.Species,personajes.Origin,personajes.Type,personajes.Location,personajes.id_locacion,personajes.Episode,personajes.id_episodio,personajes.Url)
    listaPer = []
    for per in query:
        perso = personaje.characters(per.Id,per.Nombre,per.Status,per.Species,per.Origin,per.Type,per.Location,per.id_locacion,per.Episode,per.id_episodio,per.Url)
        listaPer.append(perso)

    return listaPer

def traer_locacion():
    query = locaciones.select(locaciones.Id,locaciones.Nombre,locaciones.Type,locaciones.Dimension,locaciones.Residents,locaciones.id_personaje,locaciones.Url)
    listaLoc = []
    for loc in query:
        local = ubicacion.ubicaciones(loc.Id,loc.Nombre,loc.Type,loc.Dimension,loc.Residents,loc.id_personaje,loc.Url)
        listaLoc.append(local)

    return listaLoc

def traer_episodio():
    query = episodios.select(episodios.Id,episodios.Nombre,episodios.air_date,episodios.Episode,episodios.Character,episodios.id_personaje,episodios.Url)
    listaEpi = []
    for epi in query:
        epis = episodio.episodios(epi.Id,epi.Nombre,epi.air_date,epi.Episode,epi.Character,epi.id_personaje,epi.Url)
        listaEpi.append(epis)

    return listaEpi

if __name__ == '__main__':
    #traer_personaje()
    traer_locacion()
    #traer_episodio()