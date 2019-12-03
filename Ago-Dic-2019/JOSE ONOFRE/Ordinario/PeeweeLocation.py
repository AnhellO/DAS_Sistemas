from Peewee import *
##Creacion de la tabla Location usando Peewee
class LocationP(BaseModel):
    id = TextField(unique=True)
    name = TextField()
    type = TextField()
    dimension = TextField()
    residents = TextField()
    url = TextField()
    created = TextField()

#db.connect()
#db.create_tables([LocationP])

#Insertar datos Location
def InsertarLocation(Location): 
    LocationP.create( #Insertamos los datos usando metodo create() de peewee
        id = Location._id,
        name = Location._nameLoc,
        type = Location._typeLoc,
        dimension = Location._dimensionLoc,
        residents = Location._residentsLoc,
        url = Location._urlLoc,
        created = Location._createdLoc
    )
    
def MostrarLocation():
    for location in LocationP.select():
        print('\n----------Locacion----------\n')
        print('Id: {}\nName: {}\nType: {}\nDimension: {}\nResidents: {}\nUrl: {}\nCreated: {}'.format(location.id, location.name, location.type, location.dimension, location.residents, location.url, location.created))
        