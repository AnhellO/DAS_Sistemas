import sqlite3
def main():
    conexion = sqlite3.connect('NBA.db')
    cursor = conexion.cursor()

    cursor.execute('''
    	CREATE TABLE nba2 (
    		name INTEGER PRIMARY KEY,
    		gameId INTEGER,
    		eventName TEXT,
    		points INTEGER,
            teamId INTEGER
    	)''')
if __name__ == "__main__":
    main()