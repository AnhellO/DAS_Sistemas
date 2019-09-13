pizzas= ['Hawaiana','Peperoni','Queso','Champiñon']
friend_pizzas=pizzas[:]
pizzas.append('Chorizo')
friend_pizzas.append('Salami')

print("Mis pizzas favoritas son:")
for pizza in pizzas:
    print(pizza.title())

print()

print("Las pizzas favoritas de mis amigos son:")
for friend_pizza in friend_pizzas:
    print(friend_pizza.title())
