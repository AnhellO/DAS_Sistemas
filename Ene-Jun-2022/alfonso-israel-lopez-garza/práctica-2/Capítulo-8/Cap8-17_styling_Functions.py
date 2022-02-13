def make_sandwich(*ingredientes,bread_type = 'Integral'):
    '''Ingredientes que una persona quiere en su sandwich.'''
    print("El sandwich contiene los siguientes ingredientes:")
    print('- ' +bread_type)
    for ingrediente in ingredientes:
        print("- "+ingrediente)


make_sandwich('lechuga', 'jamon','mayonesa')
make_sandwich('huevo','aguacate','mayonesa','lechuga')
make_sandwich('jamon','huevo')

