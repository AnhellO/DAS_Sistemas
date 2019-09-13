import sqlite3

def main():

    conn = sqlite3.connect('Jikan.db')
    cur = conn.cursor()

    cur.execute('''
    CREATE TABLE IF NOT EXISTS Anime(
    ID INTEGER,
    Titulo TEXT,
    Episodios INTEGER,
    Estados TEXT)
    ''')
    conn.commit()

    cur.execute('''
    CREATE TABLE IF NOT EXISTS Manga(
    ID INTEGER,
    Titulo TEXT,
    Capitulos INTEGER,
    Estado TEXT)
    ''')
    conn.commit()

    cur.execute('''
    CREATE TABLE IF NOT EXISTS Personajes(
    ID INTEGER,
    Name TEXT,
    Name_kanji TEXT,
    Descripcion TEXT)
    ''')
    conn.commit()

    conn.close()

if  __name__== '_main_':
    main()