def decorador(func):
    def funciondecorada(self):
        if get_formato == 'HTML':  
            print (f'<p style="color:blue;text-align:center;" >{self.titulo}</p' )
        elif get_formato == 'XML':
            print ('No me se el formato'  '<lki>')
        elif get_formato == 'JSON':
            print ('Lo anterior por dos' '<juikl>')
    return funciondecorada

class page (object):
    def __init__(self,**args):
        self.url = args.get('URL')
        self.carpeta = args.get('CARPETA')
        self.contenido = args.get("CONTENIDO")
        self.titulo = args.get('TITULO')
        self.etiqueta = args.get('ETIQUETA')
        self.formato = args.get('FORMATO')
    
    def set_url(self, url):
        self.url = url
    def get_url(self):
        return self.url
    def set_carpeta(self, carpeta):
        self.carpeta = carpeta
    def get_carpeta(self):
        return self.carpeta
    @decorador
    def set_contenido(self, contenido):
        self.contenido = contenido
    def get_contenido(self):
        return self.contenido
    def set_titulo(self, titulo):
        self.titulo = titulo
    def get_titulo(self):
        return self.titulo
    def set_etiqueta(self,etiqueta):
        self.etiqueta = etiqueta
    def get_etiqueta(self):
        return self.etiqueta
    def set_formato(self, formato):
        self.formato = formato
    def get_formato(self):
        return self.formato
    def almacenar (self):
        guarda = {'url:':self.url, 'carpeta':self.carpeta, 'titulo': self.carpeta,'etiqueta': self.etiqueta, 'formato':self.formato}
        return guarda
    def __str__(self):
        return f'url:{self.url}\nCarpeta:{self.carpeta}\nContenido:{self.contenido}\nTitulo:{self.titulo}\n Etiqueta de titulo:{self.etiqueta}\n Formato:{self.formato}'


class Strategy(metaclass=abc.ABCMeta):
	"""docstring for SortStrategy"""
	
	@abc.abstractmethod
	def sort(self):
		pass
class HTMLConcreteStrategy(Strategy):
	def sort(self):
		return 'imprmiendo con formato HTML'

class XMLConcreteStrategy(Strategy):
	def sort(self):
		return 'Imprimiendo con formato XML'
        
class JSONConcreteStrategy(Strategy):
	def sort(self):
		return 'Imprimiendo con formato JSON'

class respons(page):
    def __init__(self,pagina: page, strategy:Strategy = None):
        self.strategy = strategy
        self.pagina = page

    def sort_context(self):
        if page.get_formato == 'HTML':
            return f'Page:{self.url}\n,Type:{self.formato}\n, Content:{self.contenido}'
        elif page.get_formato == 'XML':
            return 0
        elif page.get_formato == 'JSON':
            return 1
    def set_strategy(self, strategy: Strategy):
        self.strategy = strategy

    def __str__(self):
        return f'Page: {self.url}\nType: {self.formato}\n,Content:{self.contenido}'

def main():
    pagina = page(URL ='htijsjkjdf', CARPETA = 'descragads',CONTENIDO ='text',TITULO ='habia una vez', ETIQUETA = '123456', FORMATO = 'HTML' )
    
    fromatos = HTMLConcreteStrategy()
    context = respons(pagina)

    formatos = XMLConcreteStrategy()
    context.set_strategy(formatos)
	
    fromatos1 = JSONConcreteStrategy()
    context.set_strategy(fromatos1)
    print(context.sort_context())


if __name__ == '__main__':
	main()
    








