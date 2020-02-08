''' 
Juan Ivan Medina Martinez
Exercise 3.10
'''

def listFunctions(the_list):
    print("Original List: ", the_list)
    the_list.append("MSI")
    print("after append: ", the_list)
    the_list.insert(0,"ACER")
    print("after insert [0]: ", the_list)
    the_list.insert((int)(len(the_list)/2),"SAMSUNG")
    print("after insert [len/2]: ", the_list)
    print("after sorted(): ",sorted(the_list))
    the_list.reverse()
    print("after reverse(): ",the_list)
    the_list.reverse()
    print("after reverse():",the_list)
    the_list.sort()
    print("after sort(): ",the_list)
    the_list.sort(reverse=True)
    print("after sort(reverse=True)",the_list)
    print("len list: ",len(the_list))
    del the_list[0]
    print("list after del[0]: ",the_list)
    print("len after del[0]: ", len(the_list))
    print("pop :",the_list.pop())
    print("pop :",the_list.pop())
    print("pop :",the_list.pop())
    print("list after 3 pops: ",the_list)
    print("len after 3 pops: ", len(the_list))
    try:
        the_list.clear()
        print("list after clear: ",the_list)
        print("len after clear: ", len(the_list))  #clear was added in Python 3.3
    except:
        print("Error... clear was added in Python 3.3, but dont worry ...")
        del the_list[:]#this replace clear on python 2.7
        print("list after 'del the_list[:] :' (replace of clear): ",the_list)
        print("len after del the_list[:]: ", len(the_list))  
    print("Now we del the_list... ")
    del the_list
    print("And print 'the_list' ...")
    try:
        print("list after del: ",the_list)
    except:
        print("error printing list after del")
    print("And print len 'the_list' ...")
    try:
        print("len list after del: ",the_list)
    except:
        print("error printing len list after del")



if __name__ == "__main__":
    the_list=["DELL","HP","APPLE","LENOVO","TOSHIBA"]
    listFunctions(the_list)
