"""Try it yourself 9-8 """

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
"""""
usuario1 = usuarios("Antonio","Gonzales",25,"Técnico","chrysler")
usuario1.describe_users()
usuario1.greet_user()

usuario2 = usuarios("Alex","Mata",40,"Ingeniero ","chrysler")
usuario2.describe_users()
usuario2.greet_user()

usuario3 = usuarios("Juanita","Ortiz",30,"Oficinista","chrysler")
usuario3.describe_users()
usuario3.greet_user() """

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


admin = Admin("Alex","Mata",40,"Ingeniero ","chrysler")
admin.describe_users()

admin.privileges.show_privileges()

print("\n Añadimos los privilegios a nuestro usuario")
admin_privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    ]
admin.privileges.privileges = admin_privileges
admin.privileges.show_privileges()
