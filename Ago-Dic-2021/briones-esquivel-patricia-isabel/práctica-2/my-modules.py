# ------- Ejercicio 9,12- Multiple Modules -------
from user import User
from user import Admin, Privileges

user_xyz = Admin('María', 'Mendoza', 765, 'Ayhola34')
user_xyz.describe_user()
user_xyz.privileges.show_privileges()