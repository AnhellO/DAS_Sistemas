'''
Juan Ivan Medina Martinez
Exercise 5.2
'''
from conditionalTests import multiConditionalTests

def stringEqual(str1,str2):
    return str1==str2

def thereLower(str1):
    return str1==str1.lower()

def numericalEqual(num1,num2):
    if num1>num2:
        return ("Greater")
    elif num1<num2:
        return ("Less")
    else:
        return("Equal")

def andCondition(var1,var2,cond):
    return var1==cond and var2==cond

def orCondition(var1,var2,cond):
    return var1==cond or var2==cond     

def onList(var,list0101):
    return var in list01

if __name__=='__main__':
    print "" 
    print "Prediction test"
    list01=[]
    list01.append(('airplane',True))
    list01.append(('bicycle',True))
    list01.append(('laptop',False))
    list01.append(('city',True))
    list01.append(('day',False))
    list01.append(('school',False))
    list01.append(('shoes',True))
    list01.append(('airplane',True))
    list01.append(('Nurse',False))
    list01.append(('New York',True))
    list01.append (('Boat',True))
    multiConditionalTests(list01)

    print"\n[+]String Equal\n"
    equalTo="airplane"
    for element in list01:
        
        print("{}=={}?: {}".format(element[0],equalTo,stringEqual(element[0],equalTo)))

    print"\n[+]Lower Test\n"
    for element in list01:
        print("'{}' is lower case?: {}".format(element[0],thereLower(element[0])))

    print("[!] DELATING LIST ...")
    del list01
    print("[!] CREATING NUMERICAL LIST...")
    list01=range(0,11)
    print(list01)


    print"\n[+]Numerical Equal\n"
    equalTo=5
    for element in list01:
        print("{}=={}?: {}".format(element,equalTo,numericalEqual(element,equalTo)))
    
    print"\n[+]AND Test\n"
    cond=5
    list01Test=range(0,11)
    list01Test[1]=5
    list01Test[8]=5
    i=0
    for element in list01:
        var2=i
        print("{} AND {}=={}?: {}".format(element,list01Test[i],cond,andCondition(element,list01Test[i],cond)))
        i=i+1

    print"\n[+]OR Test\n"
    cond=5
    list01Test=range(0,11)
    list01Test[1]=5
    list01Test[8]=5
    i=0
    for element in list01:
        var2=i
        print("{} OR {}=={}?: {}".format(element,list01Test[var2],cond,orCondition(element,list01Test[var2],cond)))
        i=i+1

    print"\n[+]onList Test\n"
    cond=5
    print("{} in list01?: {}".format(cond,onList(cond,list01)))
    cond=20
    print("{} in list01?: {}".format(cond,onList(cond,list01)))



