'''Try It Yourself'''
'''5-1. Conditional Tests: Write a series of conditional tests. Print a statement
describing each test and your prediction for the results of each test. Your code
should look something like this:
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
• Look closely at your results, and make sure you understand why each line
evaluates to True or False.
• Create at least 10 tests. Have at least 5 tests evaluate to True and another
5 tests evaluate to False.'''
car = 'Jetta'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("Is car == 'truck'? I predict True.")
print(car == 'truck')
print("Is car == 'Hummer'? I predict True.")
print(car == 'Hummer')
print("Is car == 'moto'? I predict True.")
print(car == 'moto')
print("Is car == 'Chevrolet'? I predict True.")
print(car == 'Chevrolet')
print("Is car == 'Volkswagen'? I predict False.")
print(car == 'Jetta')
print("Is car have == '4 doors'? I predict False.")
print(car == 'Jetta')
print("Is motor car == '2.0'? I predict False.")
print(car == 'Jetta')
print("The car is beautiful == 'yes'? I predict False.")
print(car == 'Jetta')
print("Is car == 'Jetta'? I predict False.")
print(car == 'Jetta')

'''5-2. More Conditional Tests: You don’t have to limit the number of tests you
create to 10. If you want to try more comparisons, write more tests and add
them to conditional_tests.py. Have at least one True and one False result for
each of the following:
• Tests for equality and inequality with strings
• Tests using the lower() function
• Numerical tests involving equality and inequality, greater than and
less than, greater than or equal to, and less than or equal to
• Tests using the and keyword and the or keyword
• Test whether an item is in a list
• Test whether an item is not in a list'''

comida = ['Hamburguesa', 'pizza']
if comida[0] == 'Hamburguesa':
    print(True)

if comida[1] != 'pizza':
    print(True)
else:
    print(False)

if comida[0] == 'hamburguesa':
    print(True)
else:
    comida[0].lower()
    print(f"Ahora si {comida[0]}")

numeros = [15, 78, 83, 1, 22, 34]

if numeros[0] == 15:
    print(True)

if numeros[-1] != 23:
    print(True)

if numeros[2] > numeros[0]:
    print(True)

if numeros[1] < 70:
    print(True)
else:
    print(False)

if numeros[3] >= numeros[0]:
    print(True)
else:
    print(False)

if sum(numeros) <= 100:
    print(True)
else:
    print(False)

PC = ['monitor', 'mause', 'CPU', 'HeadSet']

if 'mause' in PC:
    print(True)
else:
    print(False)

if 'teclado' not in PC:
    print("La PC es touch")
else:
    print("La PC no es touch")

if 'monitor' in PC:
    print("El monitor es curvo")
else:
    print("Te lo robaron")