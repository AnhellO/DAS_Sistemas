def sum():
    try:
        x = input('Type a number : ')
        y = input('Type another number: ')
        
        x = int(x)    
        y = int(y)

    except ValueError:
            print("That's not a number")


    else:    
        print(f"Sum : {x + y} ")

for x in range(5):
    sum()