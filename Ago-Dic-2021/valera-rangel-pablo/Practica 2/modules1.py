from admin import Admin
admin1 = Admin('Antonio', 'Perez', '25', 'Monterrey, Nuevo Leon')
admin1.privileges = ['Edit', 'Delete', 'Ban']
print(admin1.describe_User())
admin1.show_privileges()