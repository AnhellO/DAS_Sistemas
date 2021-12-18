"""Try it yourself 9-5 """

class usuarios():
    def __init__(self,first_name,last_name,age,job,company):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age
        self.job = job
        self.company = company
        self.login_attempts = 0

    def describe_users(self):
        print("\n Hola mi nombre es: " + self.first_name + " " +  self.last_name)
        print(f'Tengo {self.age} de edad')
        print("Trabajo en: " + self.company + " y soy un " + self.job)
    
    def greet_user(self):
        print(f'\n Bienvenido {self.first_name}')
    
    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


usuario1 = usuarios("Antonio","Gonzales",25,"Técnico","chrysler")
#probaremos 4 incrementos
print("Intentos actuales de sesión: " + str(usuario1.login_attempts))
usuario1.increment_login_attempts()
usuario1.increment_login_attempts()
usuario1.increment_login_attempts()
usuario1.increment_login_attempts()
print("Intentos de sesión luego del incremento: " + str(usuario1.login_attempts))

#Reseteamos los intentos de login
usuario1.reset_login_attempts()
print("Intentos despues del reset: " + str(usuario1.login_attempts))

