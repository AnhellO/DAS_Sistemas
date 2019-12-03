"""7-3. Multiples of Ten: Ask the user for a number, and then report whether the
number is a multiple of 10 or not."""

numero = input("Inserte un numero: ")
numero = int(numero)

if numero % 10 == 0:
    print(str(numero) + " es un multiplo de 10.")
else:
    print(str(numero) + " no es un multiplo de 10.")