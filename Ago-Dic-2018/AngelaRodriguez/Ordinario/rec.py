import sqlite3
def main():
    conexion = sqlite3.connect('Recetas.db')
    cursor = conexion.cursor()
  
    cursor.execute('''
    	CREATE TABLE RECETA (
    		ID_TACO INTEGER PRIMARY KEY,
    		CONTRIBUIDOR TEXT,
            DESCRIPCION VARCHAR
            
    		
                	)''')
if __name__ == "__main__":
    main()