pizzas = ["Champiñones", "Mexicana", "Pastor"]

friend_pizzas = pizzas[:]

pizzas.append("Tres Quesos")

friend_pizzas.append("Peperoni")

print("Mis pizzas favoritas son:")
for i in pizzas:
    print(i)


print("Las pizzas favoritas de mi amigo son:")
for i in friend_pizzas:
    print(i)