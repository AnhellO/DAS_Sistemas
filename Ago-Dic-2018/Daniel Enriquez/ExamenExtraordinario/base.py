import sqlite3

#Creacion de las tablas
def main():
    conexion = sqlite3.connect('Cervecitas.db')
    cursor = conexion.cursor()
    cursor.execute('''
        CREATE TABLE INFOPRINCIPAL (
    		id INTEGER PRIMARY KEY,
    		name TEXT NOT NULL,
    		description TEXT

    	)''')
    cursor.execute('''
        CREATE TABLE INFOSECUNDARIA (
        	id INTEGER PRIMARY KEY,
        	image TEXT,
    		first_brewed TEXT,
    		target_fg INTEGER

    	)''')
    cursor.execute('''
        CREATE TABLE INFOEXTRA (
            id INTEGER PRIMARY KEY,
            srm INTEGER,
            abv REAL,
            ph REAL,
            tagline TEXT,
            attenuation_level INTEGER
         )''')

if __name__ == "__main__":
    main()

#name, description,image_url,abv y food_pairing
