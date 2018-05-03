#snake_case
#camelCase
#StudlyCase
#kebab-case o slug

# Clase A
    # Clase B
    # Clase C

# Cliente utiliza Clase A o un contenedor con objetos tipo Clase A
# e.g. lista = [] de solo tipo Clase A

from typing import List

class Grupo:

    """docstring for Banda"""
    def __init__(self, **args):
        self.nombre = args.get('nombre')
        self.integrantes = args.get('integrantes', [])
        self.numIntegrantes = len(self.integrantes)

    def agregarIntegrante(self, integrantes):
        if type(integrantes) is list:
            self.integrantes += integrantes
            self.numIntegrantes += len(integrantes)
            return self

        if type(integrantes) is str:
            self.integrantes.append(integrantes)
            self.numIntegrantes += 1
            return self

        print('Tipo invalido para integrantes!')
        return self

    def getPropiedades(self):
        return "Nombre: {}\nNúmero de Integrantes: {}\nIntegrantes: {}\nTipo: {}\n".format(self.nombre,
                self.numIntegrantes,
                self.integrantes,
                self.__class__.__name__)


class GrupoMusical(Grupo):

    """docstring for Banda"""
    def __init__(self, **args):
        super().__init__(**args)
        self.genero = args.get('genero')
        self.logo = args.get('logo')

    def getPropiedades(self):
        propiedades = super().getPropiedades()
        return (propiedades + "Género: {}\nLogo: {}\n").format(self.genero, self.logo)

    def retornaX(self):
        return 'X!'

class GrupoBaile(Grupo):

    """docstring for Banda"""
    def __init__(self, **args):
        super().__init__(**args)
        self.categoria = args.get('categoria')

    def getPropiedades(self):
        propiedades = super().getPropiedades()
        return (propiedades + "Categoria: {}\n").format(self.categoria)


integrantes = ['Ana', 'Claudia', 'Sleiman', 'Irving', 'Raul']
grupo = Grupo(nombre="Diseño y Arquitectura de Software Sistemas UAdeC", integrantes=integrantes[:])
#print(grupo.agregarIntegrante('Carielo').getPropiedades())

grupoMusical = GrupoMusical(nombre="Los Misticos", integrantes=integrantes[:], genero='metal')
#print(grupoMusical.getPropiedades())

grupoBaile = GrupoBaile(nombre="Los Danzoneros", integrantes=integrantes[:], categoria='flamenco')
#print(grupoBaile.getPropiedades())

grupos = [grupo] # type: List[Grupo]
grupos.append(grupoMusical)
grupos.append(grupoBaile)

for grupo in grupos:
    if type(grupo) is GrupoMusical:
        print(grupo.retornaX())
    else:
        print(type(grupo))
