'''
Juan Ivan Medina Martinez
4.5
'''
from countingToTwenty import makeList
from countingToTwenty import printList



if __name__ == "__main__":

    list=makeList(1000000)
    print("[ MIN ] : {}".format(min(list)))
    print("[ MAX ] : {}".format(max(list)))
    print("[ SUM ] : {}".format(sum(list)))