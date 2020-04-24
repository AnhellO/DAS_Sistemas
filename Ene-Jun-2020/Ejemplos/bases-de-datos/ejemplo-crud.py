import sqlite3
import sys

def insert(datos, conexion):
	select = f"SELECT nombre FROM pokemon WHERE nombre = '{datos['nombre']}'"
	if conexion.execute(select).fetchone():
		print(f'El pokemon "{datos["nombre"]}" ya existe!')
		return

	insert_prueba = f"""
		INSERT INTO pokemon (nombre, tipos, imagen)
		VALUES ('{datos['nombre']}', '{datos['tipos']}', '{datos['imagen']}')
		"""

	return cursor.execute(insert_prueba)

# Crea y conéctate a la DB
conexion = sqlite3.connect('pokemon.db')
cursor = conexion.cursor()

def main():
	# Crea la tabla si no existe
	cursor.execute(
		'''
			CREATE TABLE IF NOT EXISTS pokemon (
				id INTEGER PRIMARY KEY AUTOINCREMENT,
				nombre VARCHAR(50),
				tipos VARCHAR(200),
				imagen VARCHAR(350)
			);
		'''
	);

	# Inserta un par de registros
	charmander = {
		'nombre': 'Charmander',
		'tipos': 'Fuego',
		'imagen': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/4.png'
	}

	charmeleon = {
		'nombre': 'Charmeleon',
		'tipos': 'Fuego',
		'imagen': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/4.png'
	}

	print(insert(charmander, conexion))
	print(insert(charmeleon, conexion))

	# Obtén todos los registros e imprimelos
	select = 'SELECT * FROM pokemon';
	resultados = cursor.execute(select)

	for resultado in resultados.fetchall():
		print(f"ID: {resultado[0]}\nNombre: {resultado[1]}\nTipos: {resultado[2]}\nimagen: {resultado[3]}\n")

	# Salva los cambios
	conexion.commit()
	# *Siempre* cierra la conexión
	conexion.close()


if __name__ == '__main__':
	main()