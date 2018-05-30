from peewee import *

db = SqliteDatabase('Libreria_db.db')

class BaseModel(Model):
    class Meta:
        database = db

class Libros(BaseModel):
    id_libro = PrimaryKeyField(null=False)
    nombre_libro = TextField()
    autor_libro = ForeignKeyField(Autores, related_name="autor_detalle")
    editorial_libro = ForeignKeyField(Editoriales, related_name="editorial_detalle")

    def __str__(self):
        return "Libro: {} {}\nAutor: {} {}\nEditorial: {}".format(self.id_libro, self.nombre_libro, self.autor_libro.nombre_autor, self.editorial_libro.editorial)

class Autores(BaseModel):
    id_autor = PrimaryKeyField(null=False)
    nombre_autor = TextField()
    apellidos_autor = TextField()
    

    def __str__(self):
        return "ID:{}\nAutor:{} {}\nApellido:{}".format(self.id_autor, self.nombre_autor, self.apellidos_autor )


class Editoriales(BaseModel):
    id_editorial =PrimaryKeyField(null=False)
    editorial = TextField()
    pais_editorial =TextField()

    def __str__(self):
        return "ID: {}\neDitorial: {} {}\nPais: {}".format(self.id_editorial, self.editorial,self.pais_editorial)


################################ CREAR TABLAS ##################################
################################################################################
#db.create_tables([Libros, Autores, Editoriales])
################################################################################
################################################################################


########################### INSERTAR Libro##################################
################################################################################
#ins_lib = Libros.create(nombre_libro="",nombre_autor="",editorial_libro="")
#ins_lib2 =Libros.create(nombre_libro="",nombre_autor="",editorial_libro="")
################################################################################
################################################################################


########################### INSERTAR Autores #################################
################################################################################
#ins_au = Autores.create(id_autor="1", nombre_autor="", apellido_autor=")
#ins_au2 = Autores.create(id_autor="2", nombre_autor="", apellido_autor=")
################################################################################
##############################################################################


########################### INSERTAR Editoriales #################################
################################################################################
#ins_ed = Editoriales.create(id_editorial="1", editorial="", pais_editorial=")
#ins_ed2 = Editoriales.create(id_editorial="2", editorial="",pais_editorial=")
################################################################################
################################################################################


########################### SELECT POR ID Libro #############################
################################################################################
lib = Libros.get(Libros.id_libro == 1)
print(lib)
################################################################################
################################################################################


############################# SELECT POR ID PACIENTES ##########################
################################################################################
au = Autores.get(Autores.id_autor == 1)
print(au)
################################################################################
################################################################################


############################ SELECT POR ID CONSULTAS ###########################
################################################################################
ed = Editoriales.get(Editoriales.id_editorial == 1)
print(ed)
################################################################################
################################################################################


########################### MOSTRAR TODOS LOS DOCTORES #########################
################################################################################
for libs in Libros.select():
    print(libs)
################################################################################
################################################################################


########################## MOSTRAR TODOS LOS PACIENTES #########################
################################################################################
for au in Autores.select():
    print(aus)
################################################################################
################################################################################


######################### MOSTRAR TODAS LAS CONSULTAS ##########################
################################################################################
for ed in Editoriales.select():
    print(ed)
################################################################################
################################################################################