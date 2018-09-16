class Users:
    
     def __init__(self, first_name='', last_name='',age='', email='', phone=''):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.phone = phone
        
     def describe_user(self):
        print('Tu nombre es: ', self.first_name)
        print('Tu apellido es: ', self.last_name)
        print('Tu edad es: ', self.age)
        print('Tu correo es: ', self.email)
        print('Tu numero telefonico es: ', self.phone)
        
     def greet_user(self):
        print('Hola! ', self.first_name, 'La informacion Proporcionada esta bien?')

usuario_1 = Users('Andres', 'Lopez', '22 años', 'andrelomeza@gmail.com', '8442863199')
usuario_1.describe_user()
usuario_1.greet_user()

usuario_1 = Users('Abril', 'Valenciano', '22 años', 'vacm6996@gmai.com', '8342155323')
usuario_1.describe_user()
usuario_1.greet_user()
