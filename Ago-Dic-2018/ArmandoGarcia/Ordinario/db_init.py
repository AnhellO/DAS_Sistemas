import sqlite3
import os
class constructor_db():
    def baseladvd():
        conn = sqlite3.connect("Taqueria.db")
        cur = conn.cursor()
        if not os.path.isfile("Taqueria.db"):
            conn = sqlite3.connect("Taqueria.db")
        else:
            pass
        cur.execute('''CREATE TABLE IF NOT EXISTS Taquitos
            (id_taco Integer PRIMARY KEY,
            nombre Text,
            relleno Text,
            salsas text,
            condimentos Text,
            sasonadores Text,
            cubierta Text)
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
    constructor_db.baseladvd()
