
from tryityourself import Restaurant
#9.10
R4 = Restaurant("Dominos", "Comida rica", 0)

print(R4.describe_restaurante(R4))

#9.11
from tryityourself import Admin

admin3 = Admin("Sub", "Zero", 100, 95, 190, 10,["Puede agregar publicación", "Puede eliminar publicación", "Puede prohibir usuario"])

admin3.privi.show_privileges()
