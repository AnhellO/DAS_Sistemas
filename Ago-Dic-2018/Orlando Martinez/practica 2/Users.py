class User():

    def __init__(self, first_name, last_name, edad, correo, ciudad):
        self.first_name = first_name
        self.last_name = last_name
        self.edad = edad
        self.correo = correo
        self.ciudad = ciudad

    def describe_user(self):
        print("\n" + self.first_name + " " + self.last_name)
        print("Edad: " + self.edad)
        print("Correo: " + self.correo)
        print("Ciudad: " + self.ciudad)

    def greet_user(self):
        print("\nHola, " + self.first_name + " "  + self.last_name)

Usuario1 = User('Juan', 'Lopez Rodriguez', '19 años', 'juan_rdz@hotmail.com', 'Saltillo')
Usuario1.describe_user()
Usuario1.greet_user()

Usuario2 = User('Ana','Gonzalez Torres', '22 años', 'ana_gonzalez@hotmail.com','Monterrey')
Usuario2.describe_user()
Usuario2.greet_user()
