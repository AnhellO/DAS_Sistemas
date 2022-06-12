'''Programa que suma 2 numeros, usando  el try exception'''

num1 = input("Ingrese el primer numero: ")
num2 = input("Ingrese el segundo numero: ")
try:
    resultado = int(num1) + int(num2)
except ValueError:
    print("No se pueden sumar letras/caracteres.")
else:
    print(resultado)