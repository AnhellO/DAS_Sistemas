import abc

#CLASE ABSTRACTA 
class Page(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def url(self):
        pass
    def ruta(self):
        pass
    def link(self):
        pass
    def titulo(self):
        pass
    def contenido(self):
        pass
    def formato(self):
        pass

#CLASE BASE IMPLEMENTAMOS CLASE PAGE(COMPONENTE)
class justHTML(Page):
    def __init__(self, paragraph):
        self._paragraph = paragraph
        
    #funciones
    def url(self):
        return 'https://www.rottentomatoes.com/\n'
    def ruta(self):
        return 'Series\n'
    def link(self):
        return 'https://www.rottentomatoes.com/tv/wandavision\n'
    def titulo(self):
        return 'WandaVision\n'
    
    def contenido(self):
        return self._paragraph
    def formato(self):
        return '\nHTML'

#CLASE ABSTRACTA DE DECORADOR 
class decor(Page, metaclass=abc.ABCMeta):
    def __init__(self, parrafo):
        self.parrafo = parrafo
    def url(self):
        return 'https://www.rottentomatoes.com/\n'
    def ruta(self):
        return 'Series\n'
    def link(self):
        return 'https://www.rottentomatoes.com/tv/wandavision\n'
    def titulo(self):
        return 'WandaVision\n'
    def contenido(self):
        return self.parrafo.contenido() + '\n'
    def formato(self):
        return 'HTML'

#CLASE ABSTRACTA DECOR    
class Something(decor):
    def __init__(self, parrafo):
        decor.__init__(self, parrafo)
    #DECORA EL PARRAFO AGREGANDOLE COLOR Y ALIGN TEXT   
    def contenido(self):
        #decora el parrado 
        return '<p style="color:blue; align-text: center">' + self.parrafo.contenido() + '</p>\n'


    
def main():
    #OBJETO DE CLASE JUSTHTML E IMPRIMIMOS LA INFO
    justHtml = justHTML('Parrafo')
    print(justHtml.url(),justHtml.ruta(),justHtml.link(),justHtml.titulo(),justHtml.contenido(), justHtml.formato())
    
    print('------------------')
    
    #OBJETO DE CLASE JUSTHTML Y LO DECORAMOS 
    objDecorado = Something(justHTML('Parrafo'))
    print(objDecorado.url(),objDecorado.ruta(),objDecorado.link(),objDecorado.titulo(),objDecorado.contenido(), objDecorado.formato())
    
if __name__ == '__main__':
    main()