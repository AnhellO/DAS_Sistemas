Pizzas=['Hawainna','Peperoni', 'Mexicana', '3 quesos']
Pizzas.append('Especias')
print(Pizzas)
friend_pizzas=Pizzas[:]
friend_pizzas.append('Carnes frias')
print(friend_pizzas)

for pizza in Pizzas:
    print("Mi pizza favorita es la "+ pizza.title())

for pizza in friend_pizzas:
    print("La mizza favorita de mi amigo es: " +pizza.title())
