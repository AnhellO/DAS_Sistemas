import sqlite3
import os
class databaseConst():
    def main():
        conn = sqlite3.connect("Tako_db.db")
        cur = conn.cursor()
        if not os.path.isfile("Tako_db.db"):
            conn = sqlite3.connect("Tako_db.db")
        else:
            pass
        cur.execute('''CREATE TABLE IF NOT EXISTS Takos
            (id_tako Integer PRIMARY KEY,
            nombre Text,
            principal Text,
            salsas text,
            condimentos Text,
            sasonadores Text,
            shell Integer)
            ''')
        conn.commit()
        cur.execute('''CREATE TABLE IF NOT EXISTS Clientes
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
            id_tako Integer,
            id_user Integer
            )
            ''')
        conn.commit()
        conn.close()
if __name__ == '__main__':
    databaseConst.main()
