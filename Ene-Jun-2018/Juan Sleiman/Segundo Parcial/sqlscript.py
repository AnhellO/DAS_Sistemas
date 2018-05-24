import sqlite3
conn = sqlite3.connect('videogames.db')
c = conn.cursor()

#CREAR
def createTables():
    c.execute('''CREATE TABLE Consolas
                (nombre text, generacion text, compañia text)''')
    c.execute('''CREATE TABLE Videojuegos
                (nombre text, costo real, desarrolladora text)''')

def insertarDatos():
    print("Insertando datos a la tabla Consolas...")
    c.execute("INSERT INTO Consolas VALUES ('Juegosfera','infinita','Galaxy')")
    c.execute("INSERT INTO Consolas VALUES ('Play Station 7','7','Sony')")

    print("Insertando datos a la tabla Videojuegos")
    c.execute("INSERT INTO Videojuegos VALUES ('Battlefield 5',1399,'EA')")
    c.execute("INSERT INTO Videojuegos VALUES ('Left 4 Dead 3',1000,'Valve')")

def imprimirTablas():
    for row in c.execute('SELECT * FROM Consolas'):
        print(row)
    for row in c.execute('SELECT * FROM Videojuegos'):
        print(row)

def delFromTable():
    c.execute("DELETE FROM Consolas WHERE generacion = '7'")

def dropTables():
    c.execute("DROP TABLE Consolas")
    c.execute("DROP TABLE Videojuegos")

print("Creando tablas...")
createTables()
conn.commit()
print("Insertando los datos de las tablas...")
insertarDatos()
conn.commit()

print("Estas son las bellas tablas...")
imprimirTablas()

print("Borrando rows de la tabla...")
delFromTable()
conn.commit()
imprimirTablas()

print("Borrando tablas para nueva corrida")
dropTables()
conn.commit()
