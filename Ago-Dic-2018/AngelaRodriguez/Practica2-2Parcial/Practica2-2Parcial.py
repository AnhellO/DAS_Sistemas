import sqlite3
def main():
    conexion = sqlite3.connect('Cerveza.db')
    cursor = conexion.cursor()

    cursor.execute('''
    	CREATE TABLE CERVEZAS (
    		id INTEGER PRIMARY KEY,
    		name TEXT NOT NULL,
    		description TEXT,
    		image_url TEXT,
    		abv REAL,
            ph REAL,
    		attenuation_level INTEGER,
    		first_brewed DATE,
    		contributed_by VARCHAR,
    		tagline TEXT,
    		target_og INTEGER
    	)''')
if __name__ == "__main__":
    main()