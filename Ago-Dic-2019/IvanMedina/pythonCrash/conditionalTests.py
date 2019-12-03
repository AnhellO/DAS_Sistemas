'''
Juan Ivan Medina Martinez
Exercise 5.1
'''
def multiConditionalTests(elements):
    i=0
    for element in elements:
        print("* element[{}] == {}?".format(i,element[0]))
        r=element[0]==element[1]
        print("My prediction is '{}'".format(element[1]))
        if(element[1]==r):
            print("[+] Yes, is {}\n".format(r))
        else:
            print("[+] No, is {}\n".format(r))


if __name__=='__main__':
	print "" 
	list=[]
	list.append(('airplane',True))
	list.append(('bicycle',True))
	list.append(('laptop',False))
	list.append(('city',True))
	list.append(('day',False))
	list.append(('school',False))
	list.append(('shoes',True))
	list.append(('airplane',True))
	list.append(('Nurse',False))
	list.append(('New York',True))
	list.append (('Boat',True))
	multiConditionalTests(list)

