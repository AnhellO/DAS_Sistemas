for j in [6,11,4,19,61,100,1001,5001,55556,777778]:
    print(' '.join([str(i) for i in range(1,j)]),end='' if j==777778 else '\n')
