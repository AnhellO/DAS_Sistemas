import sqlite3

conexion = sqlite3.connect('RandUser.db')
cursor = conexion.cursor()

cursor.execute('''
    CREATE TABLE Users(
    Gender TEXT NOT NULL,
    First TEXT NOT NULL,
    Last TEXT NOT NULL,
    Location TEXT NOT NULL,
    Email TEXT NOT NULL)
    ''')

conexion.close()
