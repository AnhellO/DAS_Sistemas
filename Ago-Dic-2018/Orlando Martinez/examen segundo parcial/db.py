import sqlite3

def main():
    conexion = sqlite3.connect('Launch.db')
    cursor = conexion.cursor()


    cursor.execute('''
    	CREATE TABLE Launch (
    		id INTEGER PRIMARY KEY,
    		name TEXT NOT NULL,
    		countryCode TEXT,
    		abbrev TEXT,
    		infoURL TEXT,
            direccion TEXT

    	)''')

if __name__ == "__main__":
    main()
