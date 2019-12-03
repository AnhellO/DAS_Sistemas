''' 
Juan Ivan Medina Martinez
Exercise 3.11
'''

if __name__ == "__main__":
    list=[]
    for x in range(1,10+1):
    	list.append(x)
    print(list)
    print("I need to print 10")
    try:
        print(list[10])
    except:
        print("[ERROR] exception saved you, you want to get item 10 in an array of 10?")
        print("THE ARRAY STARTS AT 0!")
    print(list[9])
    print("Yeah, print 'list[9]' ")