class Usuario:
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