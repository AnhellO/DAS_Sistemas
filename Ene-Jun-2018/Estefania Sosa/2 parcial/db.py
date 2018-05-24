
import sqlite3

class SQlite():

    #conectar con bd
    def __init__(self):
        self.conexion = sqlite3.connect('Parcial.db')
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

if __name__ == '__main__':
    v = JUEGO(1,"MARIO","INFANTIL","A")

    db = SQlite.connect('test.db')
    db.row_factory = SQlite.Row
    
