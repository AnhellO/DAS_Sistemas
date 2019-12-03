# 7-3. Multiples of Ten: Ask the user for a number, and then report whether the number is a multiple of 10 or not.

number = input("Tell me a number man :v  : ")
number = int(number)

if number % 10 == 0:
    print(str(number) + " is a multiple of 10.")
else:
    print(str(number) + " is not a multiple of 10.")