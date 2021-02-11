
class Component(object):
    """Abstract class"""

    def __init__(self, *args, **kwargs):
        pass

    def component_function(self):
        pass
class Child(Component): #hereda de la clase abstracta , component
    """concrete class"""

    def __init__(self, *args, **kwargs):
        Component.__init__(self, *args, **kwargs)

        #Aqui es donde almacenamos el nombre de nuestro articulo hoja o hijo
        self.name = args[0]

    def component_function(self):
        #imprime el nombre de tu hijo aqui
        print("{}".format(self.name))

class Composite(Component): #Hereda de la clase abstracta, Component
    """Concrete class and maintains the tree recursive structure"""

    def __init__(self, *args, **kwargs):
        Component.__init__(self, *args, **kwargs)

        #Aqui almacenamos el nombre del objeto composite
        self.name = args[0]

        #Aqui mostramos los articulos o hijos
        self.children = []

    def append_child(self, child):
        """Method to add a new child item"""
        self.children.append(child)

    def remove_child(self, child):
        """Method to remove a child item"""
        self.children.remove(child)

    def component_function(self):

        #Mostrar el nombre del objeto composite
        print("{}".format(self.name))

        #Iterar en el objeto hijo e invocar la funcion de sus componentes imprimiendo sus nombres

        for i in self.children:
            i.component_function()

#Construye un submenu 1 de composite
sub1 = Composite("submenu1")

#Haz un nuevo hijo sub_submenu 11
sub11 = Child("sub_submenu 11")
#Haz un nuevo hijo sub_submenu 12
sub12 = Child("sub_submenu 12")

#Agrega sub_submenu 11 a submenu 1
sub1.append_child(sub11)
#Agrega sub_submenu 12 a submenu 1
sub1.append_child(sub12)

#Construye un top-level composite menu
top = Composite("top_menu")

#Construye un submenu 2 que no es un composite
sub2 = Child("submenu2")

#Add the composite submenu 1 a top-level composite menu
top.append_child(sub1)

#Agrega submenu2 a top level composite menu
top.append_child(sub2)

#Prueba si el modelo Composite funciona
top.component_function()

