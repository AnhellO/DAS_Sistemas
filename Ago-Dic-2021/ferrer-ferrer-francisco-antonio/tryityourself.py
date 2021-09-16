  
from abc import abstractstaticmethod
from typing import NoReturn

#9.1
class Restaurant:
     def __init__(self, restaurant_name, cuisine_type, number_served)->None:
        #inicializar nombre del restaurante y tipo de cocina
        #Variable de instancia
        self.restaurant_name = restaurant_name 
        self.cuisine_type = cuisine_type
        self.number_served = number_served

     def describe_restaurante(self,R):
         print(R.restaurant_name)
         print(R.cuisine_type)
         

     def abierto_cerrado(self):
        print("**Abierto**")

     def set_number_served (self,R):
        sn = 10
        R.number_Served = sn
    
     def increment_number_served(self,R, i):
        R.number_served = i
       

R1 = Restaurant("Pizzas castillo","Cocina casera", 0 )      

print(R1.restaurant_name)
print(R1.cuisine_type)
print(R1.describe_restaurante(R1))
print(R1.abierto_cerrado())


            #9.2
R2 = Restaurant("Dominos", "Comida rica", 0)
R3 = Restaurant("Little caesar's", "Comida congelada", 0)
print(R2.describe_restaurante(R2))
print(R3.describe_restaurante(R3))

class IceCreamStand(Restaurant):
     def __init__(self,restaurant_name, cuisine_type, number_served, flavors:list) -> None:
         super(IceCreamStand, self).__init__(restaurant_name, cuisine_type, number_served)
         self.flavors = flavors


     def flavorName(self): # I es iceCream
          print(str(self.flavors))

Ice = IceCreamStand("Paleteria La michocana", "Postres", 19, ["Fresa", "Chocolate", "Vainilla", "Pistache"])
 
Ice.flavorName()

#9.3 y 9.5
class Usuario:
     def __init__(self,nombre, apellido, edad, peso, altura, login_attempts)->None:
         self.nombre = nombre
         self.apellido = apellido
         self.edad = edad
         self.peso = peso
         self.altura = altura
         self.login_attempts = login_attempts
    
     def describe_user(self,u):
       return(u.nombre, u.apellido, u.edad, u.peso, u.altura)
     
     def greet_user(self,u):
      if u == u1:
          return("eres el numero 1")
      
      elif u == u2:
          return("Eres de los mejores")  

      else:
          return("Puedes mejorar")
     
     def increment_login_attempts(self, u):
         u.login_attempts += 1
         print(f'se incremento el login en "{u.login_attempts}"')

     def reset_login_attempts(self, u):
         u.login_attempts = 0
         print(f'login se reseteo a "{u.login_attempts}"')

class Privileges:
    def __init__(self,privileges:list):
        self.privileges = privileges

    def show_privileges(self):
         n=0
         for i in self.privileges:
             print(str(f'"{1+n}".- "{self.privileges[n]}"'))
             n+=1


#9.7
class Admin(Usuario):
    def __init__(self,nombre, apellido, edad, peso, altura, login_attempts, privileges:list)->None:
        super(Admin,self).__init__(nombre, apellido, edad, peso, altura, login_attempts)
        self.privileges = privileges
        self.privi = Privileges(privileges)

admin = Admin("Sub", "Zero", 100, 95, 190, 10,["Puede agregar publicación", "Puede eliminar publicación", "Puede prohibir usuario"])
#admin.show_privileges()
admin.privi.show_privileges()


user = Usuario("Desconocido", "Misterio", 100, 100, 100, 0)
u1 = Usuario("Francisco", "Ferrer", 21, 80, 180, 0)
u2 = Usuario("Antonio", "Ferrer", 21, 80, 180, 0)
u3 = Usuario("Atlas", "Lopez", 21, 80, 180, 0)

print(u1.describe_user(u1))
print(u1.greet_user(u1))
print(u2.describe_user(u2))
print(u2.greet_user(u2))
print(u3.describe_user(u3))
print(u3.greet_user(u3))


 
#9.4
restaurant = Restaurant("Pizza hot", "Comida...", 10)
print(restaurant.number_served)
print(R1.set_number_served(R1))
print(R2.set_number_served(R2))
print(R3.set_number_served(R3))

(R1.increment_number_served(R1,10))
(R2.increment_number_served(R2,9))
(R3.increment_number_served(R3,24))

for i in range(1,3):
    user.increment_login_attempts(user)
 
(user.reset_login_attempts(user))

 