class Usuario():
    def __init__(self, nombre, apellido, username, email, ubi):
        self.nombre = nombre.title()
        self.apellido = apellido.title()
        self.username = username
        self.email = email
        self.ubi = ubi.title()

    def desc(self):
        print("\nNombre: " + self.nombre + " " + self.apellido)
        print("  Username: " + self.username)
        print("  Email: " + self.email)
        print("  Ciudad: " + self.ubi)

    def bienvenida(self):
        print("\nBienvenido: " + self.username)