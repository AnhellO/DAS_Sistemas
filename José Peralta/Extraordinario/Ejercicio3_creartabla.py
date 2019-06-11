import sqlite3

def crear_tabla_paises(archivo_bd = 'paises.db'):
    conexion = sqlite3.connect(archivo_bd)
    cursor = conexion.cursor()
    cursor.execute('''CREATE TABLE Paises (
    Nombre     STRING PRIMARY KEY,
    Lenguajes  STRING,
    Continente STRING,
    Capital    STRING,
    Zona       STRING)''')
    conexion.commit()
    conexion.close()

def main():
    crear_tabla_paises()

if __name__ == '__main__':
    main()
