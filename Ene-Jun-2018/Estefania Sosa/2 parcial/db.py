
import sqlite3

class SQlite():

    #conectar con bd
    def __init__(self):
        self.conexion = sqlite3.connect('2p.db')
        self.cursor = self.conexion.cursor()

    def C(self):
        y=(1,"w","r","t")
        self.cursor.execute("INSERT INTO JUEGO (ID,NOMBRE,GENERO,CATEGORIA) VALUES (?,?,?,?)",y)
        self.conexion.commit()
        for row in self.cursor.execute("SELECT * from JUEGO "):
            print(row)

    def R(self,id):
        self.cursor.execute("SELECT * from JUEGO WHERE ID = ?",str(id))
        print(self.cursor.fetchone())

    def u(self):
        a=(3,"tqf")
        self.cursor.execute("UPDATE JUEGO SET ID = ? WHERE NOMBRE = ?",a)
        self.conexion.commit()
        for row in self.cursor.execute("SELECT * from JUEGO "):
            print(row)

    def D(self, id):
        self.cursor.execute("DELETE from JUEGO where ID=?", (str(id),))
        self.conexion.commit()
        for row in self.cursor.execute("SELECT * from JUEGO "):
            print(row)
    def C1(self):
        y=(7,"XBOX","MICROSOF")
        self.cursor.execute("INSERT INTO CONSOLA (ID,NOMBRE,MARCA) VALUES (?,?,?)",y)
        self.conexion.commit()
        for row in self.cursor.execute("SELECT * from CONSOLA "):
            print(row)

    def R2(self,x):
        self.cursor.execute("SELECT * from CONSOLA WHERE ID = ?",x)
        print(self.cursor.fetchone())

    def u3(self,x,y):
        self.cursor.execute("UPDATE CONSOLA SET ID = ? WHERE NOMBRE = ?",x,y)
        self.conexion.commit()
        for row in self.cursor.execute("SELECT * from CONSOLA "):
            print(row)

    def D4(self, id):
        self.cursor.execute("DELETE from CONSOLA where ID=?", (str(id),))
        self.conexion.commit()
        for row in self.cursor.execute("SELECT * from CONSOLA "):
            print(row)


    def Close(self):
        self.conexion.close()

if __name__ == '__main__':
    x=SQlite()
    db = sqlite3.connect('2p.db')
    x.C()
    x.R(1)
    x.u()
    x.D(1)

'''Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>>
 RESTART: C:\Users\sombr\Documents\GitHub\diseño y arquitectura de software\DAS_Sistemas\Ene-Jun-2018\Estefania Sosa\2 parcial\db.py
(1, 'w', 'r', 't')
(2, 'MARIO', 'INFANTIL', 'A')
(3, 'MARIO', 'INFANTIL', 'A')
(4, 'MARIO', 'INFANTIL', 'A')
(5, 'MARIO', 'INFANTIL', 'A')
(6, 'MARIO', 'INFANTIL', 'A')
(8, 'w', 'r', 't')
(11, 'w', 'r', 't')
(54, 'w', 'r', 't')
(56, 'w', 'r', 't')
(74, 'w', 'r', 't')
(79, 'w', 'r', 't')
(554, 'w', 'r', 't')
(1, 'w', 'r', 't')
(1, 'w', 'r', 't')
(2, 'MARIO', 'INFANTIL', 'A')
(3, 'MARIO', 'INFANTIL', 'A')
(4, 'MARIO', 'INFANTIL', 'A')
(5, 'MARIO', 'INFANTIL', 'A')
(6, 'MARIO', 'INFANTIL', 'A')
(8, 'w', 'r', 't')
(11, 'w', 'r', 't')
(54, 'w', 'r', 't')
(56, 'w', 'r', 't')
(74, 'w', 'r', 't')
(79, 'w', 'r', 't')
(554, 'w', 'r', 't')
(2, 'MARIO', 'INFANTIL', 'A')
(3, 'MARIO', 'INFANTIL', 'A')
(4, 'MARIO', 'INFANTIL', 'A')
(5, 'MARIO', 'INFANTIL', 'A')
(6, 'MARIO', 'INFANTIL', 'A')
(8, 'w', 'r', 't')
(11, 'w', 'r', 't')
(54, 'w', 'r', 't')
(56, 'w', 'r', 't')
(74, 'w', 'r', 't')
(79, 'w', 'r', 't')
(554, 'w', 'r', 't')'''
