import sqlite3
import os
def main():
    conn = sqlite3.connect("DBGT.db")
    cur = conn.cursor()
    if not os.path.isfile("DBGT.db"):
        conn = sqlite3.connect("DBGT.db")
    else:
        pass
    cur.execute('''CREATE TABLE IF NOT EXISTS Pedido
        (id_taco Integer PRIMARY KEY,
        Nombre Text,
        capa_base Text,
        salsas text,
        condimentos Text,
        sasonadores Text,
        capas Integer)
        ''')
    conn.commit()
    cur.execute('''CREATE TABLE IF NOT EXISTS Users
        (id_user Integer PRIMARY KEY,
        name Text,
        email Text,
        phone Text,
        picture Text,
        location Text)
        ''')
    conn.commit()
    cur.execute('''CREATE TABLE IF NOT EXISTS Orden
        (id_orden Text,
        total Text,
        fecha Text,
        tipo Text,
        id_taco Integer,
        id_user Integer
        )
        ''')
    conn.commit()
    conn.close()
if __name__ == '__main__':
    main()
