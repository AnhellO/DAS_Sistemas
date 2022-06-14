
def addition():

    while True:

        try:
            print("Give me two numbers please :3 \n")
            print("Just press enter to exit")

            number_1 = int(input("number 1: "))
            if "":
                break
            number_2 = int(input("number 2: "))
            if "":
                break
            
        except ValueError:
            print("Insert only numbers please n.n!")

        else: 
            sum = number_1 + number_2
            print("The answer is: " + str(sum))