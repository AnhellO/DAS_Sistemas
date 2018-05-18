from peewee import *

db = SqliteDatabase('DAS.db')

class Usuarios(Model):
    id = IntegerField()
    nombre = TextField()
    edad = IntegerField()

    class Meta:
        database = db # This model uses the "DAS.db" database.

    def __str__(self):
        return "Nombre:{}\nEdad:{}\n".format(self.nombre, self.edad)

sujeto = Usuarios.get(Usuarios.id == 666)
print(sujeto)

sujeto.edad = 18
sujeto.save()
print(sujeto)

#sujeto2 = Usuarios.create(id=9818, nombre='Claudia', edad=18)

for usuario in Usuarios.select():
    print(usuario)
