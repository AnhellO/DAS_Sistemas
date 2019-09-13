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

class admin(usuario):
    def __init__(self, nombre, apellido, edad, genero):
        super(admin, self).__init__(nombre, apellido, edad, genero)
        self.privilegios = []

    def obtener_privilegios(self, *lista_privilegios):
        self.privilegios = lista_privilegios

    def imprime_privilegios(self):
        print("Los Privilegios del Admin son: ")
        for priv in self.privilegios:
            print("- " + priv)

usuario_nuevo = usuario('Luis', 'Ornelas', 21, 'M')
print(usuario_nuevo.descripcion_usuario())
usuario_nuevo.greet_usuario()
administrador_nuevo = admin('Jose', 'Perez', 25, 'M')
print(administrador_nuevo.descripcion_usuario())
administrador_nuevo.obtener_privilegios('Puede Agregar Publicaciones', 'Puede Eliminar Publicaciones', 'Puede Darte Ban')
administrador_nuevo.imprime_privilegios()