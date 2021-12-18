"""Try it yourself 9-7 """

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

usuario1 = usuarios("Antonio","Gonzales",25,"Técnico","chrysler")
usuario1.describe_users()
usuario1.greet_user()

usuario2 = usuarios("Alex","Mata",40,"Ingeniero ","chrysler")
usuario2.describe_users()
usuario2.greet_user()

usuario3 = usuarios("Juanita","Ortiz",30,"Oficinista","chrysler")
usuario3.describe_users()
usuario3.greet_user()

class Admin(usuarios):
    def __init__(self, first_name, last_name, age, job, company):
        super().__init__(first_name, last_name, age, job, company)
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print("\n Los privilegios son los siguientes:")
        for i in range(len(self.privileges)):
            print(i+1, self.privileges[i])

admin = Admin("Alex","Mata",40,"Ingeniero ","chrysler")
print(admin.describe_users())
admin.show_privileges()