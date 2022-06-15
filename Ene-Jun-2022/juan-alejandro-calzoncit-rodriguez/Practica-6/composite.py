import abc

# Componente
class ArchivoComponent(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def imprimeEstructura(self):
        pass

    # Nombre del archivo
    def get_nombre(self):
        return self.nombre

    # Directorio o archivo
    def get_tipo(self):
        return self.tipo

class ArchivoLeaf(ArchivoComponent):

    def __init__(self, nombre) -> None:
        self.nombre = nombre
        self.tipo = 'Archivo'

    def imprimeEstructura(self) -> str:
        print(f"Nombre : '{self.get_nombre()}' , Tipo : '{self.get_tipo()}'")

class ArchivoComposite(ArchivoComponent):

    def __init__(self, nombre):
        self.nombre = nombre
        self.tipo = 'Directorio'
        self.__children = []        

    def add(self, child: ArchivoComponent):
        self.__children.append(child)

    def remove(self, child: ArchivoComponent):
        self.__children.remove(child)        

    def imprimeEstructura(self):                                   
        print(f"Nombre : '{self.get_nombre()}' , Tipo : '{self.get_tipo()}'")        
                
        for child in self.__children:                        
            child.imprimeEstructura()

def main():

    raiz = ArchivoComposite('/')
    
    etc = ArchivoComposite('/etc')
    bin = ArchivoComposite('/bin')
    var = ArchivoComposite('/var')
    log = ArchivoComposite('/log')
    mail = ArchivoComposite('/mail')
    usr = ArchivoComposite('/usr')
    lib = ArchivoComposite('/lib')
    include = ArchivoComposite('/include')
    local = ArchivoComposite('/local')    
    home = ArchivoComposite('/home')
    users = ArchivoComposite('/users')
    juan = ArchivoComposite('/juan')
    luis = ArchivoComposite('/luis')

    raiz.add(etc)
    raiz.add(var)
    raiz.add(bin)
    raiz.add(usr)
    raiz.add(home)

    var.add(log)
    var.add(mail)


    usr.add(lib)
    usr.add(include)
    usr.add(local)

    users.add(juan)
    users.add(luis)
    home.add(users)

    ejemplo1 = ArchivoLeaf('ejemplo1.py')
    ejemplo2 = ArchivoLeaf('ejemplo2.doc')
    juan.add(ejemplo1)
    juan.add(ejemplo2)
        
    raiz.imprimeEstructura()
 
if __name__ == '__main__':     
     
     main()