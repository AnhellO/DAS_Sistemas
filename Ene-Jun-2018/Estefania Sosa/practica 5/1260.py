trees = {}
cas=[]
cases = int(input())

vacio = input()

for x in range(cases):

    trees.clear()
    todos = 0

    while True:
        
        in_trees = input()

        if in_trees == "":
            break
        
        
        if trees.get(in_trees):
            trees[in_trees] += 1
        
        
        else:
            trees[in_trees] = 1
        
        
        todos += 1

   
    if x<(cases-1):
        print("")


    for arbol, porciento in sorted(trees.items()):
        porciento = 100+(porciento/todos-1)*100
        cas.insert("%s %.4f" %(arbol,porciento))
    
for x in cas:
    print(cas[x])
