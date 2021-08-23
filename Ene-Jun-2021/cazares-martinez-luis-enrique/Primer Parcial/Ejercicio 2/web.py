from PaginaWeb import PaginaWeb
from SitioWeb import SitioWeb

#Se crea decorador el cual recibe la funcion buscador la cual manda la pagina a buscar y el objeto sitio web
def buscarD(f):
    def new_function(a, b):
        paginas = []
        for i in range(0, len(b.paginas)):
            paginas.append(b.paginas[i].titulo)

        return a in paginas

    return new_function

#Se implementa el decorador nativo
@buscarD
def buscador(a, b):
    return a in b

#Se crean las paginas para el sitio web
def main():
    pagina_1 = PaginaWeb(url='https://www.youtube.com/watch?v=DF7NZ2eliDs',
                         ruta='por ahi anda',
                         formato='HTML',
                         contenido='<p>Reparacion de celular...</p>',
                         titulo='Cuidado cuando lleves a reparar tu celular 😱 descubro nueva e$t@fa!',
                         slug='cuidado-cuando-lleves-a-reparar-tu-celular-😱-descubro-nueva-e$t@fa!',
                         meta_tags='<meta name ="description" content = "Navarretes Show">')

    pagina_2 = PaginaWeb(url='https://www.youtube.com/watch?v=TXPibmw5I1A',
                         ruta='por ahi anda',
                         formato='HTML',
                         contenido='<p>Mataba Viejitas como luchadora</p>',
                         titulo='La mata Viejitas =(',
                         slug='la-mata-viejitas-=(',
                         meta_tags='<meta name ="description" content = "Leyendas Legendarias">')

    pagina_3 = PaginaWeb(url='https://www.youtube.com/watch?v=o2cWrtaElmg',
                         ruta='por ahi anda',
                         formato='HTML',
                         contenido='<p>El inicio de una Leyenda</p>',
                         titulo='Las Poquianchis',
                         slug='las-poquianchis',
                         meta_tags='<meta name ="description" content = "Leyendas Legendarias">')

    pagina_4 = PaginaWeb(url='https://www.youtube.com/watch?v=euUwzVnIMps&t=1s',
                         ruta='por ahi anda',
                         formato='HTML',
                         contenido='<p>A que equipo le debo de ir en el fucho mexicano</p>',
                         titulo='Efecto OXXO GAS',
                         slug='efecto-oxxo-gas',
                         meta_tags='<meta name ="description" content = "Leyendas Legendarias">')

    sitio_1 = SitioWeb(dominio='Leyendas Legendarias.com',
                       categoria='Misterio, Comedia, Paranormal, Necrofilia',
                       paginas=[pagina_1, pagina_2, pagina_3, pagina_4])

    print(buscador('Las Poquianchis', sitio_1))


if __name__ == '__main__':
    main()

