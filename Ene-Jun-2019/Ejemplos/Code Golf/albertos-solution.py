for j in [5,10,3,18,60,99,1000,5000,55555,777777]:
    a=' '.join([str(i) for i in range(1,j+1)])
    print(a) if j != 777777 else print(a,end='')
