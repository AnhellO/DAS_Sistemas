class Usuario():
    def __init__(self, nombre, apellido, email, edad, ciudad):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.edad = edad
        self.ciudad = ciudad
    
    def describe_usuario(self):
        print(self.nombre + " " + self.apellido + "\nE-mail: " + self.email + "\nEdad: " + str(self.edad)
              + "\nCiudad: " + self.ciudad)
    
    def usuario_saludos(self):
        print(self.nombre + " les desea un feliz Día del Amor y la Amistad =)")

class Administrador(Usuario):
    def __init__(self, nombre, apellido, email, edad, ciudad):
        super().__init__(nombre, apellido, email, edad, ciudad)
        self.privilegios = ["Puedes agregar una publicación", "Puedes borrar una publicación", 
                       "Puedes prohibir una publicación"]
    
    def mostrar_privilegios(self):
        for x in (self.privilegios):
            print(x)

admin = Administrador("Luis", "Carielo", "luis@carielo.com", 34, "Saltillo")
admin.mostrar_privilegios()

#user = Usuario("Luis", "Carielo", "luis@carielo.com", 34, "Saltillo")
#user.describe_usuario()
#user.usuario_saludos()