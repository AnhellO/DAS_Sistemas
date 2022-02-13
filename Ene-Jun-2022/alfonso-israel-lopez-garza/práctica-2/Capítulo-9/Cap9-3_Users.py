class User():
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self,**info):
        '''Describe al usuario'''
        profile = {}
        profile['Nombre'] = self.first_name
        profile['Apellido'] = self.last_name
        for key, value in info.items():
            profile[key] = value
        for key in profile:
            print(key +": " +profile[key])
    

    def greet_user(self):
        print("Hola, como estas " +self.first_name +" "+self.last_name)


'''Instanciando usuarios'''
first_user = User("Alfonso","Lopez")
first_user.describe_user(edad = "25",genero = "Masculino") ##Informacion extra
first_user.greet_user()

second_user = User("Juan","Calzoncit")
second_user.describe_user()
second_user.greet_user()