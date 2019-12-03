"""4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these
pizza names in a list, and then use a for loop to print the name of each pizza.
• Modify your for loop to print a sentence using the name of the pizza
instead of printing just the name of the pizza. For each pizza you should
have one line of output containing a simple statement like I like pepperoni
pizza.
• Add a line at the end of your program, outside the for loop, that states
how much you like pizza. The output should consist of three or more lines
about the kinds of pizza you like and then an additional sentence, such as
I really love pizza!"""

pizzas = ['Tres carnes', 'Tres quesos', 'Peperoni']

# Imprimir todas las pizzas
for pizza in pizzas:
    print(pizza)

# Imprimir una oracion para cada pizza
for pizza in pizzas:
    print("I really love " + pizza + " pizza!")

print("\nI really love pizza!")