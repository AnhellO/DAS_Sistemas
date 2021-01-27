pizza=['Peperoni','Carne','Pastor']

friend_pizza=pizza[:]

pizza.append('Champiñon')

friend_pizza.append('Mexicana')

print("Mis pizzas favoritas son: ")

for i in range(len(pizza)):

    print(pizza[i])

print("Las pizzas favoritas de mis amigos son: ")

for j in range(len(friend_pizza)):

    print(friend_pizza[j])