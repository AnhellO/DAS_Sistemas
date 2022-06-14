from Ejercicio_8_privileges import admin,privileges,user


privileges = ['add User', 'Delete User', 'delete Archives', 'Create Archives']
pedro = admin('pedro', 'casas', '8441234567', '22', 'pedro@potato.com', privileges)
pedro.show_privileges()