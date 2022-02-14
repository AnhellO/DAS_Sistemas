""" 10-7. Addition Calculator: Wrap your code from Exercise 10-6 in a while
loop so the user can continue entering numbers even if they make a mistake
and enter text instead of a number. """

while True:
    print("\n--------------------------------")
    print("| Enter two number to sum them |")
    print("--------------------------------")
    print("(Enter 'leave' at any time to leave)")

    try:
        first_number = input("- Enter the first number: ")
        if first_number == "leave":
            break

        second_number = input("- Enter the second number: ")
        if second_number == "leave":
            break

        numbers_sum = int(first_number) + int(second_number)
    except ValueError:
        print("It's not possible to perform the sum, please enter only numbers.")
    else:
        print(f"\nThe result of the sum is: "
              + f"{first_number} + {second_number} = {str(numbers_sum)}")
