'''Clase de administrador, importando User y privileges'''
from User import User
import Privileges

class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges.privileges()
