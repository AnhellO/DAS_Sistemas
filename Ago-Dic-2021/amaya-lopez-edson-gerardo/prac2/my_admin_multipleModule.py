
from Admin_multiple_module import Admin


print('Ejercicio 9.12'.center(100,"="))
admin2 = Admin('Mario','amlaguer',21,'male',83334858343,'single')
print(admin2.describe_user())

admin2_privileges =["can add post","can delete post","can ba user"]
admin2.privileges.privileges = admin2_privileges
admin2.privileges.show_privileges()
print('='.center(100,"="),'\n')