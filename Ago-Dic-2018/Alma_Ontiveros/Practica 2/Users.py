class User():

    def __init__(self, first_name, last_name, edad, correo, direccion, telefono):
        self.first_name = first_name
        self.last_name = last_name
        self.edad = edad
        self.correo = correo
        self.direccion = direccion
        self.telefono = telefono

    def describe_user(self):
        print("\n" + self.first_name + " " + self.last_name)
        print("Edad: " + self.edad)
        print("Correo: " + self.correo)
        print("Direccion: " + self.direccion)
        print("Telefono: " + self.telefono)

    def greet_user(self):
        print("\nQue onda! ¿Cómo estás?, " + self.first_name + " "  + self.last_name)

Usuario1 = User('Alma Daniela', 'Ontiveros Perales', '21 años', 'dany-adop@hotmail.com', 'Jesús R. González #777 Colonia. La Libertad', '8443572026')
Usuario1.describe_user()
Usuario1.greet_user()

Usuario2 = User('Alma Victoria','Perales Sifuentes', '29 años', 'alvyhol@hotmail.com', 'Jesús R. González #777 Colonia. La Libertad', '8443181068')
Usuario2.describe_user()
Usuario2.greet_user()

Usuario3 = User('Ricardo Arturo','Gonzalez Moreno', '27 años', 'ricardo_gon@hotmail.com', 'Zafiro #239 Colonia. Toreo', '8443467456')
Usuario3.describe_user()
Usuario3.greet_user()
