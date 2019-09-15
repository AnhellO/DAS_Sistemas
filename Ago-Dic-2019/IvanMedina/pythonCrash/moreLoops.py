'''
Juan Ivan Medina Martinez
4.12
'''

if __name__ == "__main__":
    my_foods= ['pizza','hamburguer','chocolae cake']
    friend_foods=my_foods[:]
    my_foods.append('Lasagne')
    friend_foods.append('ica cream')
    print("My favorite foods are:")
    for food in my_foods:
        print("\t* {}".format(food))
    print("My friend's favorite foods are:")
    for food in friend_foods:
        print("\t* {}".format(food))