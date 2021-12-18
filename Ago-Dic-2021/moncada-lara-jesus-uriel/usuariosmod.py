class Usuarios():
    def __init__(self,first_name,last_name,age,job,company):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age
        self.job = job
        self.company = company

    def describe_users(self):
        print("\n Hola mi nombre es: " + self.first_name + " " +  self.last_name)
        print(f'Tengo {self.age} de edad')
        print("Trabajo en: " + self.company + " y soy un " + self.job)
    
    def greet_user(self):
        print(f'\n Bienvenido {self.first_name}')

