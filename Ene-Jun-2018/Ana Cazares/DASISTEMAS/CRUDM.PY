import sqlite3
from peewee import *

class SQlite(AbstractRepo):
	 #conectar con bd
    def __init__(self):
        self.conexion = sqlite3.connect('Libreria_db.db')
        self.cursor = self.conexion.cursor()

    def GuardarLibros(self, libro):
        # Insertar libro
        l = (libro.nombre, libro.autor, libro.editorial)
        self.cursor.execute("INSERT INTO Libros (NOMBRE, AUTOR,EDITORIAL) VALUES (?,?,?)", v)
        self.conexion.commit()#guarda cambios
        libro.Id_libro = self.cursor.lastrowid

        # Insertar autores
        autores = []
        if libro.autores is not None:
            for au in libro.Autores:
                autores.append((libro.Id, au))
        if len(autores) < 1:
            autores.append((libro.Id, "sin autor"))
        self.cursor.executemany("INSERT INTO Autor (ID_AUTOR, NOMBRE_AUTOR, APELLIDO_AUTOR) VALUES (?,?, ?)", Autores)
        self.conexion.commit()
        return libro

         # Insertar categorias
        categorias = []
        if libro.categoria is not None:
            for ca in libro.Autores:
                categorias.append((libro.Id, au))
        if len(categorias) < 1:
            categorias.append((libro.Id, "sin categoria"))
        self.cursor.executemany("INSERT INTO EDITORIAL (ID_LIBRO, NOMBRE_LIBRO) VALUES (?, ?)", Autores)
        self.conexion.commit()
        return libro

    def MostrarLista(self):
        libro = []
        self.cursor.execute("SELECT * from Libros")
        for db_libros in self.cursor.fetchall():
            libro = Video(db_libro[1], db_libro[2], db_libro[3], db_libro[4], db_libro[5], db_libro[6], db_libro[7], id=db_libro[0], editoriales=[])
            print(db_video)
            self.cursor.execute("SELECT * from CATEGORIA where VIDEO_ID=?", (str(video.Id),))
            for row in self.cursor.fetchall():
                print(row)
                video.Categorias.append(row[2])

            videos.append(video)

        return videos

    def MostrarVideo(self, id):
        self.cursor.execute("SELECT * from Libro where id=?", str(id))
        db_libro = self.cursor.fetchone()
        libro = Libro(db_libro[1], db_libro[2], db_libro[3], db_libro[4], db_libro[5], db_libro[6], db_libro[7], id=db_libro[0], editoriales=[])

        self.cursor.execute("SELECT * from Editoriales where Libro_id=?", (str(id),))
        for row in self.cursor.fetchall():
            libro.Editoriales.append(row[2])

        return video


    def ModificarVideo(self, libro):
        t = (video.Nombre, video.Duracion, video.Canal, video.Fecha, video.Likes, video.Vistas, video.Descripcion, video.Id)
        self.cursor.execute("UPDATE Lbro SET NOMBRE=?, AUTOR=?, EDITORIAL=? where ID=?", t)
        self.conexion.commit()

        self.cursor.execute("DELETE from Editorial where Libros_ID=?", (str(libro.Id),))
        self.conexion.commit()
        # Insertar categorias
        editorial = []
        if libro.editorial is not None:
            for ed in libro.editorial:
                editorial.append((video.Id, cat))
        if len(categorias) < 1:
            categorias.append((video.Id, "sin categoria"))
        self.cursor.executemany("INSERT INTO CATEGORIA (VIDEO_ID, NOMBRE) VALUES (?, ?)", categorias)
        self.conexion.commit()
        return video


    def BorrarVideo(self, id_libro):
        self.cursor.execute("DELETE from Editorial where Libro_id=?", (str(id_libro),))
        self.cursor.execute("DELETE from Libro WHERE ID=?", (str(id_libro),))
        self.conexion.commit()
        return True

    def Close(self):
        self.conexion.close()

if __name__ == '__main__':
    v = Libro("id_libro 1", "nombre_libro  Cien años de soledad", "nombre_autor Gabrie",  "editorial_libro= Harper, Jonathan Cape", id=3, Editorial=['una', 'y dos'])

    ana_db = SQlite()

 
    libro = ana_db.MostrarLista()
    for lib in libro:
        print(lib.Id, lib.Nombre, lib.Editorialesditoriales)

    ana_db.Close()


