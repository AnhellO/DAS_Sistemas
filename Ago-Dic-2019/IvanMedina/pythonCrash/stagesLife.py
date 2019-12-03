'''
Juan Ivan Medina Martinez
Exercise 5.6
'''
def stepLife(yourAge):
    if isinstance(yourAge,int):

        if(yourAge>=0):

            if(yourAge<2):
                print("Yo are an baby.")
            elif(4>yourAge>=2):
                print("You are an toddler.")
            elif(13>yourAge>=4):
                print("You are an kid.")
            elif(20>yourAge>=13):
                print("You are an teenager.")
            elif(65>yourAge>=20):
                print("You are an adult.")                               
            else:
                print("You are an elder.")	
        else:
            print("Sorry, only positives.")

    else:
        print("Sorry, only 'int'.")



if __name__ == '__main__':
    print(" *** Welcome to stageLife.py ***")
    age=input("Please enter your age: ")
    #if isinstance(age,int):
    #    stepLife(age)