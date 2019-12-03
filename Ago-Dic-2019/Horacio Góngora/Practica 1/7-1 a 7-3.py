'''Try It Yourself'''
'''7-1. Rental Car: Write a program that asks the user what kind of rental car they
would like. Print a message about that car, such as “Let me see if I can find you
a Subaru.”'''
carro = input("Que tido de carro te gustaria rentar: ")
print(f"Dejame ver si tenemos un {carro}")

'''7-2. Restaurant Seating: Write a program that asks the user how many people
are in their dinner group. If the answer is more than eight, print a message saying
they’ll have to wait for a table. Otherwise, report that their table is ready.'''
mesa = int(input("Buenas Noches mesa para cuantos? "))
if mesa > 8:
    print("Espere porfavor a que se desocupe una mesa tan grande")
else:
    print("Siganqme su mesa los espera")

'''7-3. Multiples of Ten: Ask the user for a number, and then report whether the
number is a multiple of 10 or not.'''
numero = int(input("Dime un numero: "))
if numero % 10 == 0:
    print(f"Es {numero} multiplo de 10")
else:
    print("No es multiplo de 10 ")