# Suponga que tiene un sistema de archivos tipo UNIX. El funcionamiento de
# este tipo de sistema de archivos es comúnmente representado por medio de
# una estructura de datos de tipo árbol jerárquico. Cada directorio puede
# contener 0 o varios directorios, pero también 0 o varios archivos. El
# principal objetivo es moverse a través del sistema de archivos de manera
# sencilla, mientras se puede tener ubicado cada archivo a través de una
# ruta, justo como ser haría si te movieses dentro de la misma terminal.

class Component(object):
    """Clase abstracta"""

    def __init__(self, *args, **kwargs):
        pass

    def component_function(self):
        pass

class Child(Component):
    """Hereda de la clase abstracta Component"""

    def __init__(self, *args, **kwargs):  # constructor
        Component.__init__(self, *args, **kwargs)
        self.name = args[0] # aquí guardamos el nombre de nuestro objeto composite

    def component_function(self):
        """Imrpime el nombre de nuestro child item"""
        print("{}".format(self.name))

class Composite(): # Inherits from the abstract class, component
    """Hereda de la clase abstracta Component"""

    def __init__(self, *args, **kwargs):  # constructor
        Component.__init__(self, *args, **kwargs)
        self.name = args[0]  # aquí guardamos el nombre de nuestro objeto composite
        self.children = []  # aquí guardamos nuestros child items

    def append_child(self, child):
        """Método para agregar un nuevo child item"""
        self.children.append(child)

    def remove_child(self, child):
        """Método para eliminar un child item"""
        self.children.remove(child)

    def component_function(self):
        """Imprime el nombre del objeto composite"""
        print("{}".format(self.name))

        # Itera através de los objetos child e invoca la función componente imprimiendo sus nombres
        for i in self.children:
            i.component_function()

# Eon el patrón composite podemos construir objetos complejos a partir de
# otros más simples y similares entre sí, gracias a la composición recursiva
# y a una estructura en forma de árbol.

def main():
    top = Composite("top")  # Nodo raíz del árbol

    # Nodos padres
    var = Composite("/var")
    user = Composite("/user")
    home = Composite("/home")
    users = Composite("/users")

    # Nodos terminales u hoja que no tienen hijos o ramificaciones
    etc = Child("/etc")
    bin = Child("/bin")
    log = Child("/log")
    mail = Child("/mail")
    lib = Child("/lib")
    include = Child("/include")
    local = Child("/local")
    juan = Child("/juan")
    luis = Child("/luis")

    # ÁRBOL A CREAR:
    # (1)top
    #   (2)etc
    #   (2)var
    #       (3)log
    #       (3)mail
    #   (2)bin
    #   (2)user
    #       (3)lib
    #       (3)include
    #       (3)local
    #   (2)home
    #       (3)users
    #           (4)juan
    #           (4)luis

    # (2)
    top.append_child(etc)
    top.append_child(var)
    top.append_child(bin)
    top.append_child(user)
    top.append_child(home)

    # (3)
    var.append_child(log)
    var.append_child(mail)
    user.append_child(lib)
    user.append_child(include)
    user.append_child(local)
    home.append_child(users)

    # (4)
    users.append_child(juan)
    users.append_child(luis)

    # Impimir todo el árbol!!!!!!!!!
    top.component_function()

if __name__ == "__main__":
    main()
