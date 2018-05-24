import sqlite3

class SQlite():

    #conectar con bd
    def __init__(self):
        self.conexion = sqlite3.connect('bd.db')
        self.cursor = self.conexion.cursor()

    def C(self, juego):
        # Insertar juego
        self.cursor.execute("INSERT INTO VIDEO (ID,NOMBRE,GENERO,CATEGORIA) VALUES (?,?,?,?)", J)
        self.conexion.commit()#guarda cambios
        return self.cursor.lastrowid

    def R(self,x):
        self.cursor.execute("SELECT * from JUEGO WHERE ID = ?",row['ID'],row[tr(x)])
        return self.cursor.fetchone()

    def u(self, id):
        self.cursor.execute("UPDATE JUEGO SET ID = ? WHERE NOMBRE = ?", str(id))
        self.conexion.commit()
        return self.cursor.lastrowid

    def D(self, id):
        self.cursor.execute("DELETE from JUEGO where ID=?", (str(id),))
        self.conexion.commit()
        if self.cursor.lastrowid == None:
            return "borrado"
        else:
            return self.cursor.lastrowid

    def Close(self):
        self.conexion.close()

def main():
    conexion = sqlite3.connect('bd.db')
    cursor = conexion.cursor()

    #crear tabla VIDEOJUEGO
    cursor.execute('''CREATE TABLE JUEGO
                    (ID integer PRIMARY KEY,
                    NOMBRE TEXT NOT NULL,
                    GENERO TEXT NOT NULL,
                    CATEGORIA TEXT NOT NULL)''')

    #crear tabla CONSOLA
    cursor.execute('''CREATE TABLE CONSOLA
                    (ID integer PRIMARY KEY,
                    NOMBRE INTEGER NOT NULL,
                    MARCA TEXT NOT NULL)''')

    conexion.close()

if __name__ == '__main__':
    v = JUEGO(1,"MARIO","INFANTIL","A")

    db = SQlite()
    db.c()  
