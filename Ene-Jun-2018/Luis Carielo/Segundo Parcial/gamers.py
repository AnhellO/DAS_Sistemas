import sqlite3
from consola import Consola
from video_juego import VideoJuego

conexion = sqlite3.connect("gamer_db.db")

cursor = conexion.cursor()

cursor.execute("""
	CREATE TABLE IF NOT EXISTS consolas
	(
		id_consola INTEGER PRIMARY KEY NOT NULL,
		nombre_consola TEXT,
		precio_consola INTEGER
	)
""")


cursor.execute("""
	CREATE TABLE IF NOT EXISTS video_juegos
	(
		id_videojuego INTEGER PRIMARY KEY NOT NULL,
		nombre_videojuego TEXT,
		precio_videojuego INTEGER
	)
""")


def insertar_consolas(consola):
	with conexion:
		cursor.execute("INSERT INTO consolas VALUES(:id_consola, :nombre_consola, :precio_consola)", {'id_consola': consola.id_consola, 'nombre_consola': consola.nombre_consola, 'precio_consola': consola.precio_consola})
		print("Se agregó la consola")

def insertar_juegos(juego):
	with conexion:
		cursor.execute("INSERT INTO video_juegos VALUES(:id_videojuego, :nombre_videojuego, :precio_videojuego)", {'id_videojuego': juego.id_videojuego, 'nombre_videojuego': juego.nombre_videojuego, 'precio_videojuego': juego.precio_videojuego})
		print("Se agregó el video juego")

def consultar_consolas():
	cursor.execute("SELECT * FROM consolas")
	return cursor.fetchall()

def consultar_juegos():
	cursor.execute("SELECT * FROM video_juegos")
	return cursor.fetchall()

def modificar_consolas(consola, precio_consola):
	with conexion:
		cursor.execute("UPDATE consolas SET precio_consola = :precio_consola WHERE id_consola = :id_consola", {'precio_consola': precio_consola, 'id_consola': consola.id_consola})
		print("Se actualizó el precio de la consola:", consola.nombre_consola)

def modificar_juegos(juego, precio_videojuego):
	with conexion:
		cursor.execute("UPDATE video_juegos SET precio_videojuego = :precio_videojuego WHERE id_videojuego = :id_videojuego", {'precio_videojuego': precio_videojuego, 'id_videojuego': juego.id_videojuego})
		print("Se actualizó el precio del video juego:", juego.nombre_videojuego)

def eliminar_consolas(consola):
	with conexion:
		cursor.execute("DELETE FROM consolas WHERE id_consola = :id_consola", {'id_consola': consola.id_consola})
		print("Se eliminó la consola:", consola.nombre_consola)

def eliminar_juegos(juego):
	with conexion:
		cursor.execute("DELETE FROM video_juegos WHERE id_videojuego = :id_videojuego", {'id_videojuego': juego.id_videojuego})
		print("Se eliminó el video juego:", juego.nombre_videojuego)


#----------------------------------------------------------------------------#
cons_1 = Consola(1, 'xbox', 5000)
cons_2 = Consola(2, 'ps', 5200)


insertar_consolas(cons_1)
insertar_consolas(cons_2)

cns_consola = consultar_consolas()
print(cns_consola)

modificar_consolas(cons_1, 5100)
eliminar_consolas(cons_2)
#----------------------------------------------------------------------------#
#----------------------------------------------------------------------------#
game_1 = VideoJuego(1, 'fifa', 800)
game_2 = VideoJuego(2, 'The King of Fighters', 1400)

insertar_juegos(game_1)
insertar_juegos(game_2)

cns_juego = consultar_juegos()
print(cns_juego)

modificar_juegos(game_2, 700)
eliminar_juegos(game_1)
#----------------------------------------------------------------------------#
conexion.close()