""" 10-6. Addition: One common problem when prompting for numerical input 
occurs when people provide text instead of numbers. When you try to convert 
the input to an int, you'll get a TypeError. Write a program that prompts for 
two numbers. Add them together and print the result. Catch the TypeError if 
either input value is not a number, and print a friendly error message. Test
your program by entering two numbers and then by entering some text instead
of a number. """

print("--------------------------------")
print("| Enter two number to sum them |")
print("--------------------------------")
try:
    first_number = int(input("- Enter the first number: "))
    second_number = int(input("- Enter the second number: "))
    numbers_sum = first_number + second_number
except ValueError:
    print("It's not possible to perform the sum, please enter only numbers")
else:
    print(f"\nThe result of the sum is: "
          + f"{first_number} + {second_number} = {str(numbers_sum)}")
