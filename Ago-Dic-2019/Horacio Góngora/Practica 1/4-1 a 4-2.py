'''Try It Yourself'''
'''4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these
pizza names in a list, and then use a for loop to print the name of each pizza.
• Modify your for loop to print a sentence using the name of the pizza
instead of printing just the name of the pizza. For each pizza you should
have one line of output containing a simple statement like I like pepperoni
pizza.
• Add a line at the end of your program, outside the for loop, that states
how much you like pizza. The output should consist of three or more lines
about the kinds of pizza you like and then an additional sentence, such as
I really love pizza!'''

pizzas = ['Pepperoni', 'Carne', '3 Quesos', 'Champiñones', 'La que tiene los 4 ingredientes', 'Orilla rellena de queso con todo lo anterior']

for i in pizzas:
    print(i)

for pizza in pizzas:
    print(f"Me encanta la pizza de {pizza} son lo mejor <3, estan de limon")
print("Mi top 3 es el siguiente: ")
print(pizzas[-1])
print(pizzas[-2])
print(pizzas[0])
print("Realmente me encanta la pizza, la comida italiana es de lo mejor :D")

'''4-2. Animals: Think of at least three different animals that have a common characteristic.
Store the names of these animals in a list, and then use a for loop to
print out the name of each animal.
• Modify your program to print a statement about each animal, such as
A dog would make a great pet.
• Add a line at the end of your program stating what these animals have in
common. You could print a sentence such as Any of these animals would
make a great pet!'''

pets = ['Mastin Tibetano', 'Aguila', 'Tigre']

for i in pets:
    print(i)

for i in pets:
    print(f"Tener como mascota a {i} es genial dado que son Increibles o_o")
print("Lo que tienes en comun es que son raros tenerlos como mascotas y el tenerlos lo hace genial")
print(f"Un {pets[0]} lo hace una gran mascota ya que son increibles guardianes y podrias montar uno como un caballo y tienen mucho pelo y seria un buen lugar para dormir")
print(f"Una {pets[1]} lo que lo hace un gran mascta seria su capacidad de espionaje y ataques aereos")
print(f"Un {pets[-1]} lo que lo hace una gran mascota es su gran poder para cuidar la casa y montar un {pets[2]} es Increible")