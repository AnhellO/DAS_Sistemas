import sqlite3
def main():
    conexion = sqlite3.connect('Recetas.db')
    cursor = conexion.cursor()
   
    cursor.execute('''
    	CREATE TABLE USUARIOS (
            ID INTEGER PRIMARY KEY,
    		FIRST TEXT,
    		LAST TEXT,
            EMAIL VARCHAR,
            ADDRESS VARCHAR,
            BALANCE VARCHAR
            
    		
                	)''')
if __name__ == "__main__":
    main()