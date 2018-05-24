import sqlite3
conn = sqlite3.connect('Tienda.db')
c = conn.cursor()

#CREAR
def crearTablas():
    c.execute('''CREATE TABLE Consolas
                (nombre text, generacion text, compañia text)''')
    c.execute('''CREATE TABLE Videojuegos
                (nombre text, genero text, desarrolladora text)''')

def insertarDatos():
    print("Insertando datos a la tabla Consolas...")
    c.execute("INSERT INTO Consolas VALUES ('Play Station 4', '7','Sony Computer Entertainment)")
    c.execute("INSERT INTO Consolas VALUES ('Xbox One','8','Microsoft')")

    print("Insertando datos a la tabla Videojuegos")
    c.execute("INSERT INTO Videojuegos VALUES ('assassins creed','Accion','Ubisoft Montreal')")
    c.execute("INSERT INTO Videojuegos VALUES ('Final Fantasy XIII-2','Rol','Square Enix')")

def imprimir():
    for row in c.execute('SELECT * FROM Consolas'):
        print(row)
    for row in c.execute('SELECT * FROM Videojuegos'):
        print(row)

def eliminarReg():
    c.execute("DELETE FROM Consolas WHERE nombre = 'Play Station 4'")

def eliminarTablas():
    c.execute("DROP TABLE Consolas")
    c.execute("DROP TABLE Videojuegos")


print("Creando tablas.")
crearTablas()
conn.commit()
print("Insertando datos a las tablas.")
insertarDatos()
conn.commit()

print("Estas son las tablas creadas.")
imprimir()

print("Borrando registros de la tabla.")
eliminarReg()
conn.commit()
imprimir()

print("Borrando tablas")
eliminarTablas()
conn.commit()