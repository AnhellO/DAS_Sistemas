

def addition():
    try:
        print("Give me two numbers please :3 \n")
        number_1 = int(input("number 1: "))
        number_2 = int(input("number 2: "))
    except ValueError:
        print("Insert only numbers please n.n!")

    else: 
        sum = number_1 + number_2
        print("The answer is: " + str(sum))



addition()