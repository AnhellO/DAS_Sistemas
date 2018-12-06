import sqlite3

def main():
    conexion = sqlite3.connect('Taqueria.db')
    cursor = conexion.cursor()



    cursor.execute('''CREATE TABLE Tacos
                    (ID_TACO integer,
                    NOMBRE_TACO TEXT PRIMARY KEY,
                    SUBRECETAS TEXT,
                    CONTRIBUIDORES TEXT


                )''')

    cursor.execute('''CREATE TABLE Clientes
                    (ID_CLIENTE integer PRIMARY KEY,
                    NOMBRE_CLIENTE TEXT,
                    GENERO TEXT,
                    DIRECCION TEXT,
                    CELULAR REAL


                    )''')

    cursor.execute('''CREATE TABLE Ordenes
                    ( id_orden   INTEGER PRIMARY KEY,
                    id_taco    INTEGER REFERENCES Tacos (ID_TACO),
                    id_cliente INTEGER REFERENCES Clientes (ID_CLIENTE)

                    )''')





if __name__ == "__main__":
    main()
