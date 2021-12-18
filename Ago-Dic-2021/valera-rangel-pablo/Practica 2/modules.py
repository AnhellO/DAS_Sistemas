from restaurant import Restaurant
rest1 = Restaurant('Alitas y Costillas', 'BBQ')
print(rest1.describe_restaurant())
print(rest1.open_restaurant())

from user import Admin

admin1 = Admin('Antonio', 'Perez', '25', 'Monterrey, Nuevo Leon')
admin1.privileges = ['Edit', 'Delete', 'Ban']
print(admin1.describe_User())
admin1.show_privileges()