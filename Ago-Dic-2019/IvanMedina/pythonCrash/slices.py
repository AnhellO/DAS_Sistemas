'''
Juan Ivan Medina Martinez
4.10
'''
from countingToTwenty import makeList
from countingToTwenty import printList





if __name__ == "__main__":

    list=makeList(10)
    print(list)
    print(list[0:3])
    print(list[(len(list)/2)-1:(len(list)/2)+2])
    print(list[len(list)-3:])
    