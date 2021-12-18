# ------- Ejercicio 9,11- Imported Admin -------
from user import User, Admin, Privileges

user_xyz = Admin('María', 'Mendoza', 765, 'Ayhola34')
user_xyz.describe_user()
user_xyz.privileges.show_privileges()
