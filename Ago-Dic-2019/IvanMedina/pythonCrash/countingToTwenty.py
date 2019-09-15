'''
Juan Ivan Medina Martinez
4.3
'''

def makeList(nElementsList):
    list=[]
    i=1
    while(i<=nElementsList):
        list.append(i)
        i=i+1
    return list

def printList(list):

	for element in list:
		print element


if __name__ == "__main__":

    list=makeList(20)
    printList(list)