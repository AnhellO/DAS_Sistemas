class Users:

    def __init__(self, first_name='', last_name='', user_age='', user_id='', user_phone=''):
        self.first_name = first_name
        self.last_name = last_name
        self.user_age = user_age
        self.user_id = user_id
        self.user_phone = user_phone

    def describe_user(self):
        print('El nombre del usuario es: ', self.first_name)
        print('El apellido del usuario es: ', self.last_name)
        print('La edad del usuario es: ', self.user_age)
        print('El id del usuario es: ', self.user_id)
        print('El numero telefonico del usuario es: ', self.user_phone)

    def greet_user(self):
        print('Hola! ', self.first_name, 'Que tal como estais, todo bien, todo correcto, y io que me alegro!')

usuario_1 = Users('Ernesto', 'Vela', '21 años', '12345', '8641087890')
usuario_1.describe_user()
usuario_1.greet_user()

usuario_1 = Users('Panchito', 'Vazquez', '18 años', '2342', '684687468')
usuario_1.describe_user()
usuario_1.greet_user()

usuario_1 = Users('El chapo', 'Guzman', '40 años', '15478', '8441253698')
usuario_1.describe_user()
usuario_1.greet_user()

usuario_1 = Users('Malcom', 'El del medio', '15 años', '987412', '8452158745')
usuario_1.describe_user()
usuario_1.greet_user()
