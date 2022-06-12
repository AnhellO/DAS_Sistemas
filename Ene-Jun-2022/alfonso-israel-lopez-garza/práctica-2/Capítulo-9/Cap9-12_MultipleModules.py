'''Creando instancia de la clase Admin'''
import AdminPrivileges

#Instanciando
administrador = AdminPrivileges.Admin('Juan','Perez')
administrador.describe_user()
administrador.privileges.show_privileges()