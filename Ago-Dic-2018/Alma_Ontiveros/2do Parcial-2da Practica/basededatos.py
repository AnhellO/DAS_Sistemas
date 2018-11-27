import sqlite3

def main():
    conexion = sqlite3.connect('Cervezas.db')
    cursor = conexion.cursor()

    cursor.execute('''
    	CREATE TABLE CERVEZAS (
    		id INTEGER PRIMARY KEY,
    		name TEXT NOT NULL,
    		description TEXT,
    		image TEXT,
			first_brewed TEXT,
			target_fg INTEGER,
			srm INTEGER,
    		abv REAL,
			ph REAL,
    		tagline TEXT,
    		attenuation_level INTEGER
    	)''')

if __name__ == "__main__":
    main()