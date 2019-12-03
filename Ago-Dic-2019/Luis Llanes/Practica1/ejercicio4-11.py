pizzas = ["triple carne", "extra queso", "suprema"]
friend_pizzas = ["triple carne", "extra queso", "suprema"]

pizzas.append("baggel")
friend_pizzas.append("hawaiana")

print("Mis pizzas favoritas son:")
for i in range(0,len(pizzas)):
    print(pizzas[i])

print()

print("Las pizzas favoritas de mi amigo son:")
for i in range(0,len(friend_pizzas)):
    print(friend_pizzas[i])


