class usuarios():
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

class Admin(usuarios):
    def __init__(self, first_name, last_name, age, job, company):
        super().__init__(first_name, last_name, age, job, company)
        self.privileges = Privileges()

    

class Privileges():
    def __init__(self,privileges=[]):
        super().__init__()
        self.privileges = privileges

    def show_privileges(self):
        print("\n Estos son tus privilegios:")
        if self.privileges:
            for i in range(len(self.privileges)):
                print(i+1, self.privileges[i])
        else:
            print("\n Este usuario no tiene ningun privilegio")