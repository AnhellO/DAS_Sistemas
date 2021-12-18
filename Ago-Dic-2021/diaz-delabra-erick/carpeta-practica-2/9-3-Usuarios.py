class Usuarios():
    def __init__(self, nombre, apellido, username, email, ubi):
        self.nombre = nombre.title()
        self.apellido = apellido.title()
        self.username = username
        self.email = email
        self.ubi = ubi.title()

    def descripcion(self):
        print("\nNombre: " + self.nombre+ " " + self.apellido)
        print("  Username: " + self.username)
        print("  Email: " + self.email)
        print("  Ubicacion: " + self.ubi)
        print("\n")

    def presentacion(self):
        print("Bienvenido: " + self.username)

u1 = Usuarios('Erick', 'Diaz', 'erickgames', 'erickdiaz@uadec.edu.mx', 'Saltillo')
u1.descripcion()
u1.presentacion()

u2 = Usuarios('Edson', 'Amaya', 'sexon123', 'edsonA123@gmail.com', 'Parras')
u2.descripcion()
u2.presentacion()