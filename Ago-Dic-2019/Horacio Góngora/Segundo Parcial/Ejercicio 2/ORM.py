import sqlite3
from objArtBand import artista

def mostrarArtistas():
    try:
        conexion = sqlite3.connect('baseBandas.db')
        cursor = conexion.cursor()
        uMostrar = cursor.execute("SELECT * from artistas").fetchall()
        art = []

        for u in uMostrar:
            u = artista(id=u[0],area=u[1],typeC=u[2],nombre=u[3],sort=u[4],idd=u[5],extScore=u[6])
            art.append(u)
        conexion.commit()
        cursor.close()

        for i in art:
            print(i)

    except sqlite3.Error as error:
        print('Error con la conexión!', error)
    finally:
        if (conexion):
            conexion.close()

def numeroArtistas():
    try:
        conexion = sqlite3.connect('baseBandas.db')
        cursor = conexion.cursor()
        uMostrar = cursor.execute("SELECT * from artistas").fetchall()
        art = []

        for u in uMostrar:
            u = artista(id=u[0],area=u[1],typeC=u[2],nombre=u[3],sort=u[4],idd=u[5],extScore=u[6])
            art.append(u._nombre)
        conexion.commit()
        cursor.close()

        return len(art)

    except sqlite3.Error as error:
        print('Error con la conexión!', error)
    finally:
        if (conexion):
            conexion.close()

def main():
    print(mostrarArtistas())
    print(numeroArtistas())

if __name__ == '__main__':
    main()