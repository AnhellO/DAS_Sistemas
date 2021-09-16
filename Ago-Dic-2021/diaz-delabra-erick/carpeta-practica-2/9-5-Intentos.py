class Usuario():
    def __init__(self, nombre, apellido, username, email, ubi):
        self.nombre = nombre.title()
        self.apellido = apellido.title()
        self.username = username
        self.email = email
        self.ubi = ubi.title()
        self.intentos_de_entrada = 0

    def describe_Usuario(self):
        print("\nNombre: " + self.nombre + " " + self.apellido)
        print("  Username: " + self.username)
        print("  Email: " + self.email)
        print("  Ciudad: " + self.ubi)

    def Bienvenida(self):
        print("\nBienvenido: " + self.username)

    def incrementar(self):
        self.intentos_de_entrada += 1

    def reinicio(self):
        self.intentos_de_entrada = 0

u1 = Usuario('Erick', 'Diaz', 'erickgames', 'erickdiaz@uadec.edu.mx', 'saltiyork')
u1.describe_Usuario()
u1.Bienvenida()
u1.incrementar()
u1.incrementar()
u1.incrementar()
u1.incrementar()
u1.incrementar()
print(" Intentos de login (5):  " + str(u1.intentos_de_entrada))
u1.reinicio()
print("\n Intentos de login (0):  " + str(u1.intentos_de_entrada))