import sqlite3
from Videojuegos import *

#conexio
con=sqlite3.connect('Videojuegos_db.db')
cur=con.cusor()

#db = SqliteDatabase('Videojuegos_db.db')

class BaseModel(Model):
    class Meta:
        database = db

class Videojuego(BaseModel):
    id_videojuego = PrimaryKeyField(null=False)
    nombre_videojuego = TextField()
    Trama = TextField()

    def __str__(self):
        return "ID: {}\nVideojuego: {} {}\nTrama: {}".format(self.id_videojuego, self.nombre_videojuego, self.Trama)


class Consola(BaseModel):
    id_Consola = PrimaryKeyField(null=False)
    nombre_Consola = TextField()
    empresa = TextField()

    def __str__(self):
        return "ID:{}\nConsola:{} {}\nEmpresa:{}".format(self.id_Consola, self.nombre_Consola, self.empresa)


################################ CREAR TABLAS ##################################
################################################################################
#db.create_tables([Videojuego, Consola])
################################################################################
################################################################################

########################### INSERTAR Videojuegos ##################################
################################################################################
#ins_vid = Videojuego.create(nombre_videojuego="Assassin's",Trama="Accion")
#ins_vid2 = Videojuego.create(nombre_videojuego="Mario car",Trama="Autos")
#ins_vid3 = Videojuego.create(nombre_videojuego="Kirby",Trama="Aventur")
################################################################################
################################################################################


########################### INSERTAR Consola #################################
################################################################################
#ins_con = Consola.create(nombre_consola="PSP", empresa=Playstation)
#ins_con2 = Consola.create(nombre_consola="Xbox 360", empresa=Xbox)
#ins_con3 = Consola.create(nombre_consola="NES", empresa=Nintendo)
#ins_con4 = Consola.create(nombre_consola="PS4", empresa=Playstation)
################################################################################
 
########################### SELECT POR ID Videojuego #############################
vid = Videojuego.get(Videojuego.id_videojuego == 1)
print(vid)

############################# SELECT POR ID Consola ##########################
con = Consola.get(Consola.id_Consola == 1)
print(con)

########################### MOSTRAR TODOS LOS Videojuegos #########################
for vids in Videojuegos.select():
    print(vids)

########################## MOSTRAR TODAS LAS CONSOLAS#########################
for cons in CONSOLAS.select():
    print(cons)

########################## ACTUALIZA#########################
Videojuego =('fifa' , 'Deportes')
cur.excecute('INSERTAR into Videojuegos(nombre_videojuego , Trama)', Videojuego)
con.commit()

########################## Elimina#########################
Videojuegos =('fifa' , 'Deportes')
cur.excecute('delete from Videojuego where id=?',('1'))
con.commit()



