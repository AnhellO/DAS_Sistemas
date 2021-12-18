from users import Admin

print('\n-----------------9-11-------------------------')
user = Admin('América', 'Cedillo', 'a-cedillo','america@gmail.com')
user.describe_user()
user_privileges = ['puede cambiar contraseñas','puede prohibir usuarios',]
user.privileges.privileges = user_privileges
print("\nEl administrador " + user.username + " tiene estos privilegios: ")
user.privileges.show_privileges()