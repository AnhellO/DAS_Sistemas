import sqlite3

def main():
    conn = sqlite3.connect("Paises.db")
    cur = conn.cursor()
    cur.execute('''CREATE TABLE Paises (
    Nombre STRING PRIMARY KEY,
    Capital  STRING,
    Region STRING,
    Lenguajes STRING,
    Bandera STRING)''')
    conn.commit()
    conn.close()

if __name__ == '__main__':
    main()
