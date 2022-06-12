'''Clase que define al usuario'''
class User():
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self,**info):
        '''Describe al usuario'''
        profile = {}
        profile ['Numero de usuario'] = self.login_attempts
        profile['Nombre'] = self.first_name
        profile['Apellido'] = self.last_name
        for key, value in info.items():
            profile[key] = value
        for key in profile:
            print(key +": " +str(profile[key]))
        print() ##Salto de linea.
    

    def greet_user(self):
        print("Hola, como estas " +self.first_name +" "+self.last_name)

    
    def increment_login_attempts(self):
        '''Incrementando en 1 el numero de usuario'''
        self.login_attempts +=1

    
    def reset_login_attempts(self):
        '''Reiniciando el numero de usuario'''
        self.login_attempts = 0