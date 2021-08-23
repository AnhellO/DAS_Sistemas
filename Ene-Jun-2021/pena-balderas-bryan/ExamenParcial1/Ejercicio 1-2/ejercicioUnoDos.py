import abc


#Cree la clase de objeto de pagina web que contiene los diferentes atributos pedidos ademas de su str para imprimir 
#la propia pagina
class PaginaWeb():
    def __init__(self,url:str,ruta,formato,contenido,titulo,slug,meta_tags:list):
        self.url=url
        self.ruta=ruta
        self.formato=formato
        self.contenido=contenido
        self.titulo=titulo
        self.slug=slug
        self.meta_tags=meta_tags

    def __str__(self)->str:
        return f'''
            Propiedades de la pagina: 
                Url: {self.url} 
                Ruta: {self.ruta} 
                Formato: {self.formato} 
                Contenido: {self.contenido}
                Titulo: {self.titulo} 
                Slug: {self.slug}
                Tags: {len(self.meta_tags)}
                    {', '.join([str(i) for i in self.meta_tags])}
                '''


#para el decorador se necesita una interface, en este caso aqui se declara
class Interface_Web_Component(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def buscar(self):
        pass

#despues se crea la clase SitioWeb que implementa nuestra interface para poder aplicar las funciones que cree
class SitioWeb(Interface_Web_Component):
    def __init__(self,dominio,categoria,paginas:list):
        self.dominio=dominio
        self.categoria=categoria
        self.paginas=paginas

    #esta funcion es la que va a buscar la pagina que le digamos, retorna la propia lista de paginas para poder
    #evaluarla dentro del decorador
    def buscar(self):
        return self.paginas


    def __str__(self):
        return f"Dominio: {self.dominio}\n\nCategoria: {self.categoria}\nPaginas: {len(self.paginas)}\n {''.join([str(i) for i in self.paginas])}"



#se crea la clase decorador que es de la que las demas clases implementaran
class Decorator(Interface_Web_Component):

    def __init__(self, componente:Interface_Web_Component):
        self.componente=componente

    @abc.abstractmethod
    def buscar(self):
        return self.componente.buscar()


#Este es el decorador del buscador, este es el que nos hara la funcion de buscar, a la hora de llamar al self.componente.buscar
#ya esta retornando la lista de paginas por lo que ya sabe donde buscar
class BuscadorConcreteDecorator(Decorator):
    def buscar(self,paginaw:PaginaWeb):
        if paginaw in self.componente.buscar():
            return "Pagina Existe"
        else:
            return "No Existe"
    
    

        

if __name__=="__main__":
    pagina=PaginaWeb("www.pagina.com","/pagina","html","test","Titulo","titulo",["tec","inforatica"])
    listapaginas=[]
    listapaginas.append(pagina)
    sitio=SitioWeb("pagina","tecnologia",listapaginas)
    print(sitio)
