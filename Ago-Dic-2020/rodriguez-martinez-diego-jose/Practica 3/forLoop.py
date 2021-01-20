# crean un iterador concreto de un iterable concreto con el metodo iter() 
# (en nuestro caso seria la interfaz)

iterable = [1,2,3,4,5,6,7,8,9]
iterador = iter(iterable)

# loop infinito
while True:
    try:
        # consigue el siguiente elemento desde el iterador concreto
        i = next(iterador)

        # codigo dentro del for
        print(i)
    except StopIteration:
        # se rompe el loop cuando StopIteration sea aventado
        break