'''
Juan Ivan Medina Martinez
4.11
'''
from pizzas import list_pizza






if __name__ == "__main__":

    friend_pizzas=[]
    friend_pizzas=list_pizza[:]
    list_pizza.append("Three meat pizza")
    friend_pizzas.append("Cheese pizza")
    print("My favorite pizza are: ")
    for pizza in list_pizza:
    	print("\t* {}".format(pizza))
    print("My friend's favorite pizzas are: ")
    for pizza in friend_pizzas:
        print("\t* {}".format(pizza))
