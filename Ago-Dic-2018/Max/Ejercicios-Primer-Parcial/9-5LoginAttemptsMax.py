class user: #creo la clase usuario
    def __init__(self, first_name, last_name, age, sex, civil_status): #doy los atributos
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.civil_status = civil_status
        self.login_attempts = 0

    def describe_user(self): #creo la descripcion la cual nos dara todos los datos organizados
        Date_user = "Name: " + self.first_name + " " + self.last_name + "\nAge: " + self.age + "\nSex: " + self.sex + "\nCivil status: " + self.civil_status
        print(Date_user)

    def greet_user(self): #Mensaje personalizado para el usuario
        print("Bienbenido " + self.first_name + " a un dia mas (°w°)/ !!! ")

    def increment_login_attempts(self): #permite incrementar el numero de intentos de ingresar
        self.login_attempts += 1

    def reset_login_attempts(self): #restablece el numero de intentos a 0
        self.login_attempts = 0

User_1 = user('Max', 'Garcia', '22', 'Man', 'Single')
User_1.greet_user()
User_1.describe_user()
print("\n")
print("Prueba")
User_1.increment_login_attempts() #incremento el numero de intentos en 1
User_1.increment_login_attempts() #incremento el numero de intentos en 1
print("Intentos: " + str(User_1.login_attempts)) #imprimo los resultados

print("Restablecer intentos...") #restablesco los intentos a 0
User_1.reset_login_attempts()
print("Intentos de inicio de sesion: " + str(User_1.login_attempts))
