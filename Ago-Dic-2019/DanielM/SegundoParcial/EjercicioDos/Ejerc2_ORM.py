import sqlite3
from Ejerc1_Obj_Band_Artist import artista

def mostrarArtistas():
    try:
        conexion = sqlite3.connect('bd_Bandas.db')
        cursor = conexion.cursor()
        aMostrar = cursor.execute("SELECT * from artistas").fetchall()
        art = []

        for a in aMostrar:
            a = artista(id=a[0],area=a[1],typeC=a[2],nombre=a[3],sort=a[4],idd=a[5],extScore=a[6])
            art.append(a)
        conexion.commit()
        cursor.close()

        for i in art:
            print(i)

    except sqlite3.Error as error:
        print('Error con la conexión crack :(', error)
    finally:
        if (conexion):
            conexion.close()

#--------------------------------------------------------------------------------------------------------------

def numeroArtistas():
    try:
        conexion = sqlite3.connect('bd_Bandas.db')
        cursor = conexion.cursor()
        aMostrar = cursor.execute("SELECT * from artistas").fetchall()
        art = []

        for a in aMostrar:
            a = artista(id=a[0],area=a[1],typeC=a[2],nombre=a[3],sort=a[4],idd=a[5],extScore=a[6])
            art.append(a._nombre)
        conexion.commit()
        cursor.close()

        return len(art)

    except sqlite3.Error as error:
        print('Error con la conexión crack :(', error)
    finally:
        if (conexion):
            conexion.close()

def main():
    print(mostrarArtistas())
    print(numeroArtistas())

if __name__ == '__main__':
    main()