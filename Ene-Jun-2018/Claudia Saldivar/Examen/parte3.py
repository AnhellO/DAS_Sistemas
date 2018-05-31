import sqlite3

conexion = sqlite3.connect('consultas_db.db')
cursor = conexion.cursor()

def crear_tablas():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS consola
        (
            id_consola INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            nombre_consola TEXT NOT NULL,
            tipo_consola TEXT NOT NULL,
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS videojuegos
        (
            id_videojuego INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            nombre_videojuego TEXT NOT NULL,
            tipo_videojuego TEXT NOT NULL,
        )
    """)
    cursor.close()
    conexion.commit()
    conexion.close()

def insertar_datos_consola():
    cursor.execute("INSERT INTO consola VALUES(1, 'XBOX','Las consolas de salón')")
    cursor.execute("INSERT INTO doctores VALUES(2, 'PLAY STATION', 'Las consolas de salón)")
    cursor.close()
    conexion.commit()
    conexion.close()

def insertar_datos_videojuegos():
    cursor.execute("INSERT INTO videojuegos VALUES(1, 'HALO','GUERRA')")
    cursor.execute("INSERT INTO videojuegos VALUES(2, 'FIFA','DEPORTES')")
    cursor.close()
    conexion.commit()
    conexion.close()

def eliminar_datos_videojuegos():
	cursor.execute("DELETE FROM videojuegos WHERE id_videojuego=1")
	cursor.close()
	conexion.commit()
	conexion.close()

def actualizar_datos_videojuegos():
	cursor.execute("UPDATE videojuegos set tipo_videojuego=BOLSILLO WHERE id_videojuego=2")
	cursor.close()
	conexion.commit()
	conexion.close()

def consultar_tablas_videojuegos():
    cursor.execute("SELECT * FROM videojuegos")
    videojuegos = cursor.fetchall()
    for vid in videojuegos:
        print(vid)
    cursor.close()
    conexion.commit()
    conexion.close()

#crear_tablas()
#consultar_tablas_videojuegos()
#insertar_datos_consola()
insertar_datos_pacientes()
eliminar_datos_videojuegos()
actualizar_datos_videojuegos()
