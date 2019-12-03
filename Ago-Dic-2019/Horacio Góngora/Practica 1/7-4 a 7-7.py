'''Try It Yourself'''
'''7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of
pizza toppings until they enter a 'quit' value. As they enter each topping,
print a message saying you’ll add that topping to their pizza.'''
msj="Que ingrediente quiere en su pizza? "
msj+="\nCuando termine escribe 'quit'. "

ingredientes=""
while ingredientes != 'quit':
    ingredientes = input(msj)
    print(f"Agregaste este {ingredientes} tu pizza")
    if ingredientes == 'quit':
        break

'''7-5. Movie Tickets: A movie theater charges different ticket prices depending on
a person’s age. If a person is under the age of 3, the ticket is free; if they are
between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is
$15. Write a loop in which you ask users their age, and then tell them the cost
of their movie ticket.'''
x = 0
while x < 1:
    edad = int(input(f'Que edad tienes? '))
    if edad < 3:
        print('Tu entrada es gratis')
    elif edad >=3 and edad <= 12:
        print("Tu boleto vale $10")
    else:
        print("Tu boleto vale $15")

'''7-6. Three Exits: Write different versions of either Exercise 7-4 or Exercise 7-5
that do each of the following at least once:
• Use a conditional test in the while statement to stop the loop.
• Use an active variable to control how long the loop runs.
• Use a break statement to exit the loop when the user enters a 'quit' value.'''
msj = "Que ingrediente quiere en su pizza? "
msj += "\nCuando termine escribe 'quit'. "

ingredientes = ""
while ingredientes != 'quit':
    ingredientes = input(msj)
    print(f"Agregaste este {ingredientes} a tu pizza")
    if ingredientes != 'quit':
        print(ingredientes)

print("Conditional")

active = True
while active:
    mensaje = input(msj)
    if mensaje == 'quit':
        active = False
    else:
        print(input)

print("Break")

while True:
    mensaje = input(msj)
    if mensaje == 'quit':
        break
    else:
        print(f"Agregaste este {ingredientes} a tu pizza")

'''7-7. Infinity: Write a loop that never ends, and run it. (To end the loop, press
ctrl-C or close the window displaying the output.)'''
x = 0
while x < 1:
    print(x)