import sqlite3

def CREATE_DB():
    conexion = sqlite3.connect('AOE2.db')
    cursor = conexion.cursor()

    cursor.execute('''
                CREATE TABLE IF NOT EXISTS CIVILIZACIONES (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre VARCHAR(20),
                    expansion VARCHAR(30),
                    tipo VARCHAR(50)
                );
                ''');
    
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS UNIDADES (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre VARCHAR(20),
                    descripcion VARCHAR(80),
                    expansion VARCHAR(30),
                    edad VARCHAR(30),
                    rango INTEGER,
                    ataque INTEGER
                );
                ''')
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS ESTRUCTURAS (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre VARCHAR(20),
                    expansion VARCHAR(30),
                    edad VARCHAR(50),
                    tiempo FLOAT
                );
                ''')
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS TECNOLOGIAS (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre VARCHAR(20),
                    descripcion VARCHAR(80),
                    expansion VARCHAR(30),
                    edad VARCHAR(30)
                );
            ''')

