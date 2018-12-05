import sqlite3
import os

def main():
    conn = sqlite3.connect("BDTacos.db")
    cur = conn.cursor()
    if not os.path.isfile("BDTacos.db"):
        conn = sqlite3.connect("BDTacos.db")
    else:
        pass
    cur.execute('''CREATE TABLE IF NOT EXISTS TACOS
        (id_taco Integer PRIMARY KEY,
        name Text,
        ingprincipal Text,
        salsas text,
        condimentos Text,
        seasonings Text,
        cubierta Integer)
        ''')
    conn.commit()

    cur.execute('''CREATE TABLE IF NOT EXISTS CLIENTE
        (id_cliente Integer PRIMARY KEY,
        name Text,
        email Text,
        location Text,
        phone Text,
        picture Text)
        ''')
    conn.commit()

    cur.execute('''CREATE TABLE IF NOT EXISTS ORDEN
        (id_orden Text,
        id_taco Integer,
        id_cliente Integer,
        total Text,
        fecha Text
        )
        ''')
    conn.commit()

    conn.close()
if __name__ == '__main__':
    main()
