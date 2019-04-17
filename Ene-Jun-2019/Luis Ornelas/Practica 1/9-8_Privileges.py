class usuario(object):
    def __init__(self, nombre, apellido, edad, genero):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.genero = genero

    def descripcion_usuario(self):
        print("Nombre: " + self.nombre.title() + "\nApellido: " + self.apellido.title() + "\nEdad: " + str(self.edad) + "\nGenero: " + self.genero)

    def greet_usuario(self):
        print("Bienvenido: " + self.nombre.title() + " " + self.apellido.title())

class privilegios(object):
    def __init__(self):
        self.privilegios = []

    def obtener_privilegios(self, *list_privilegios):
        self.privilegios = list_privilegios

    def imprime_privilegios(self):
        print("Los Privilegios del Admin son: ")
        for priv in self.privilegios:
            print("- " + priv)

class admin(usuario):
    def __init__(self, nombre, apellido, edad, genero):
        super(admin, self).__init__(nombre, apellido, edad, genero)
        self.privilegios = privilegios()


administrador_n = admin('Rosa', 'Sanchez', 18, 'F')
print(administrador_n.descripcion_usuario())
administrador_n.privilegios.obtener_privilegios('Puede Agregar Publicaciones', 'Puede Eliminar Publicaciones')
administrador_n.privilegios.imprime_privilegios()