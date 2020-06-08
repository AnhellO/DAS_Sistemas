import abc
#CLASE ABSTRACTA 
class Page(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def url(self):
        pass
    def folder(self):
        pass
    def link(self):
        pass
    def titulo(self):
        pass
    def desc(self):
        pass
    def fromato(self):
        pass

#CLASE BASE IMPLEMENTAMOS CLASE PAGE(COMPONENTE)
class justHTML(Page):
    def __init__(self, paragraph):
        self._paragraph = paragraph
        
    #funciones
    def url(self):
        return 'https://wikileaks.org/\n'
    def folder(self):
        return 'News\n'
    def link(self):
        return 'https://wikileaks.org/Amazon-Atlas-Press-Release.html\n'
    def titulo(self):
        return 'WikiLeaks - Amazon Atlas\n'
    #funcion que regresa el texto ingresado que queremos decorar
    def desc(self):
        return self._paragraph
    def formato(self):
        return '\nHTML'
#CLASE ABSTRACTA DE DECORADOR, IMPLEMENTA LA CLASE ABSTRACTA PAGE 
class decor(Page, metaclass=abc.ABCMeta):
    def __init__(self, parrafo):
        self.parrafo = parrafo
    def url(self):
        return 'https://wikileaks.org/\n'
    def folder(self):
        return 'News\n'
    def link(self):
        return 'https://wikileaks.org/Amazon-Atlas-Press-Release.html\n'
    def titulo(self):
        return 'WikiLeaks - Amazon Atlas\n'
    def desc(self):
        return self.parrafo.desc() + '\n'
    def formato(self):
        return 'HTML'
#IMPLEMENTA LA CLASE ABSTRACTA DECOR    
class Something(decor):
    def __init__(self, parrafo):
        decor.__init__(self, parrafo)
    #DECORA EL PARRAFO AGREGANDOLE COLOR Y ALIGN TEXT   
    def desc(self):
        #decora el parrado 
        return '<p style="color:blue; align-text: center">' + self.parrafo.desc() + '</p>\n'


    
def main():
    #OBJETO DE CLASE JUSTHTML E IMPRIMIMOS LA INFO
    justHtml = justHTML('This is a paragraph')
    print(justHtml.url(),justHtml.folder(),justHtml.link(),justHtml.titulo(),justHtml.desc(), justHtml.formato())
    
    print('------------------')
    
    #OBJETO DE CLASE JUSTHTML Y LO DECORAMOS 
    objDecorado = Something(justHTML('This is a paragraph'))
    print(objDecorado.url(),objDecorado.folder(),objDecorado.link(),objDecorado.titulo(),objDecorado.desc(), objDecorado.formato())
    
if __name__ == '__main__':
    main()