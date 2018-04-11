"""Suponga que tiene un sistema de archivos tipo UNIX. El funcionamiento de este tipo de sistema de archivos
es comúnmente representado por medio de un árbol jerárquico. Cada directorio puede contener 0 o varios directorios,
pero también 0 o varios archivos. El principal objetivo es moverse a través del sistema de archivos de manera sencilla,
 mientras se puede tener ubicado cada archivo a través de una ruta

*Implemente el patrón Composite en python para ilustrar este ejemplo
*Agregue los respectivos diagramas UML de clases que reflejen la solución"""
from abc import ABC, abstractmethod

NOT_IMPLEMENTED = "You should implement this."

class Root(ABC):
    @abstractmethod
    def print(self):
        raise NotImplementedError(NOT_IMPLEMENTED)

class Folder(Root):
    def __init__(self,name):
        self.folders = []
        self.name = name

    def print(self):
        for fold in self.folders:
            fold.print()
            print("Folder:", self.name)

    def add(self, fo):
        self.folders.append(fo)

    def remove(self, fo):
        self.folders.remove(fo)

class Files(Root):
    def __init__(self, name):
        self.name = name

    def print(self):
        print("File name:", self.name)



if __name__ == '__main__':

    foto1 = Files("vacaciones.jpg")
    video1 = Files("tornado.mp4")
    tarea1 = Files("parcial.txt")
    saludo = Files("saludo.py")

    carpetaroot = Folder("/root")
    carpetaimagenes = Folder("Imagenes")
    carpetavideos = Folder("Videos")
    carpetatrabajos = Folder("Trabajos")

    carpetaimagenes.add(foto1)
    carpetavideos.add(video1)
    carpetatrabajos.add(tarea1)

    carpetaroot.add(carpetavideos)
    carpetaroot.add(carpetaimagenes)
    carpetaroot.add(carpetatrabajos)
    carpetaroot.add(saludo)

    carpetaroot.print()

"""
'Ejemplo de output'
File name: tornado.mp4 -> este archivo
Folder: Videos -> tornado.mp4 está dentro de esta carpeta
Folder: /root -> Videos está dentro de esta carpeta

File name: vacaciones.jpg
Folder: Imagenes
Folder: /root

File name: parcial.txt
Folder: Trabajos
Folder: /root

File name: saludo.py
Folder: /root
"""
