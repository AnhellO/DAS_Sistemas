'''Instanciando Admin y utilizando los metodos de User,Admin y Privileges.'''
import Admin

#Instanciando
administrador = Admin.Admin('Alfonso','Lopez')
administrador.describe_user()
administrador.privileges.show_privileges()