import sqlite3

def main():
    conexion = sqlite3.connect('Chelas.db')
    cursor = conexion.cursor()


    cursor.execute('''
    	CREATE TABLE CHELAS (
    		id INTEGER PRIMARY KEY,
    		name TEXT NOT NULL,
    		description TEXT,
    		image TEXT,
    		abv REAL,
    		target_fg INTEGER,
    		tagline TEXT,
    		srm INTEGER,
    		ph REAL,
    		attenuation_level INTEGER
    	)''')

if __name__ == "__main__":
    main()
