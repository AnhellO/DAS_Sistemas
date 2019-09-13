import sqlite3

def main():
    conn = sqlite3.connect('Jikan.db')
    cur = conn.cursor()

    cur.execute('''
    CREATE TABLE IF NOT EXISTS Anime(
    id INTEGER,
    title TEXT,
    episodes INTEGER,
    status TEXT)
    ''')
    conn.commit()

    cur.execute('''
    CREATE TABLE IF NOT EXISTS Manga(
    id INTEGER,
    title TEXT,
    chapters INTEGER,
    status TEXT)
    ''')
    conn.commit()

    cur.execute('''
    CREATE TABLE IF NOT EXISTS Character(
    id INTEGER,
    name TEXT,
    image_url TEXT)
    ''')
    conn.commit()

    conn.close()

if __name__ == '__main__':
    main()
