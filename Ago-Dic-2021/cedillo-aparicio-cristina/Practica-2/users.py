class Users:
    def __init__(self, first_name, last_name, username, email) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.login_attempts = 0

    def describe_user(self) -> str:
        print('\n######Datos del usuario#####\n', self.first_name, self.last_name,
        '\nUsuario:', self.username,'\nCorreo:', self.email)

    def greet_user(self) -> str:
        print('\nHola', self.username, '¡Bienvenido!.\n' )

    def increment_login_attempts(self) -> int:
        self.login_attempts += 1

    def reset_login_attempts(self) -> int:
        self.login_attempts = 0

class Admin(Users):
    def __init__(self, first_name, last_name, username, email):
        super().__init__(first_name, last_name, username, email)
        # self.priv = []
        self.privileges = privileges()

    # def show_privileges(self):
    #     print("\nPrivilegios:")
    #     for priv in self.priv:
    #         print(priv)

class privileges():
    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print("\nPrivilegios:")
        if self.privileges:
            for privilege in self.privileges:
                print("- " + privilege)
        else:
            print("Este usuario no tiene privilegios.")

print('\n-----------------9-3-------------------------')
usuario_1 = Users('América', 'Cedillo', 'a-cedillo','america@gmail.com')
usuario_1.describe_user()
usuario_1.greet_user()
usuario_2 = Users('Francisco','Perez','fco.perez','paco@gmail.com')
usuario_2.describe_user()
usuario_2.greet_user()
usuario_3 = Users('Margarita','Almaraz','almaraz70','mague@gmail.com')
usuario_3.describe_user()
usuario_3.greet_user()
print('\n-----------------9-5-------------------------')
usuario_1 = Users('América', 'Cedillo', 'a-cedillo','america@gmail.com')
usuario_1.describe_user()
usuario_1.greet_user()
usuario_1.increment_login_attempts()
usuario_1.increment_login_attempts()
usuario_1.increment_login_attempts()
usuario_1.increment_login_attempts()
usuario_1.increment_login_attempts()
print('Intentos:', str(usuario_1.login_attempts))
usuario_1.reset_login_attempts()
print('Intentos:', str(usuario_1.login_attempts))
print('\n-----------------9-7-------------------------')
usuario = Admin('América', 'Cedillo', 'a-cedillo','america@gmail.com')
usuario.describe_user()
usuario.priv = ['puede cambiar contraseñas','puede prohibir usuarios',]
# usuario.show_privileges()
print('\n-----------------9-8-------------------------')
user = Admin('América', 'Cedillo', 'a-cedillo','america@gmail.com')
user.describe_user()
user.privileges.show_privileges()
print("\nAgregar privilegios.")
user_privileges = ['puede cambiar contraseñas','puede suspender usuarios']
user.privileges.privileges = user_privileges
user.privileges.show_privileges()