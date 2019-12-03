import sqlite3
from ObjetoArtista import Artista

def showArt():
    try:
        conexion = sqlite3.connect('musicBrainzDB.db')
        cursor = conexion.cursor()
        uMostrar = cursor.execute("SELECT * from Artistas").fetchall()
        Art = []

        for u in uMostrar:
            u = Artista(id=u[0],area=u[1],TypeC=u[2],name=u[3],sort=u[4],id2=u[5],extScore=u[6])
            Art.append(u)
        conexion.commit()
        cursor.close()

        for i in Art:
            print(i)

    except sqlite3.Error as error:
        print('Error con la conexión!', error)
    finally:
        if (conexion):
            conexion.close()

def NArt():
    try:
        conexion = sqlite3.connect('musicBrainzDB.db')
        cursor = conexion.cursor()
        uMostrar = cursor.execute("SELECT * from Artistas").fetchall()
        Art = []

        for u in uMostrar:
            u = Artista(id=u[0],area=u[1],TypeC=u[2],name=u[3],sort=u[4],id2=u[5],extScore=u[6])
            Art.append(u._name)
        conexion.commit()
        cursor.close()

        return len(Art)

    except sqlite3.Error as error:
        print('Error con la conexión!', error)
    finally:
        if (conexion):
            conexion.close()

def main():
    print(showArt())
    print(showArt())

if __name__ == '__main__':
    main()