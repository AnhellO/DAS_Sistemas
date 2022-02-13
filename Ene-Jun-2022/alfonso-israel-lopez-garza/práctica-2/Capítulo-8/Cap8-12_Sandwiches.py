def sandwich(*ingredientes):
    '''Ingredientes que una persona quiere en su sandwich.'''
    print("El sandwich contiene los siguientes ingredientes:")
    for ingrediente in ingredientes:
        print("- "+ingrediente)

sandwich('lechuga', 'jamon','mayonesa')
sandwich('huevo','aguacate','mayonesa','lechuga','')
sandwich('jamon','huevo')

