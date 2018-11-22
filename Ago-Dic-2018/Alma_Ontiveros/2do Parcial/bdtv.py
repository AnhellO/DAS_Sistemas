import sqlite3

def main():
	db = sqlite3.connect('Tvmaze.db')
	cursor = db.cursor()

	cursor.execute('''
		CREATE TABLE IF NOT EXISTS TVMAZE (
			id INTEGER PRIMARY KEY,
			name TEXT,
			runtime INTEGER,
			weight TEXT,
			officialSite TEXT,
			status TEXT
			)''')

if __name__ == '__main__':
	main()
