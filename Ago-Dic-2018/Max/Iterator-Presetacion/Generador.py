def gen_primos():
    """ Generador de números primos."""
    contador = 1
    lista_primos=[]
    # Comienza un ciclo infinito.
    while True:
        es_primo = True
        contador += 1
        if len(lista_primos) > 0:
            for primo in lista_primos:
                if contador % primo == 0:
                    es_primo = False
                    break
        if es_primo:
            lista_primos.append(contador)
            yield contador
            print(contador)

generador = gen_primos()
getattr(generador, "__next__")
#next(generador)
#next(generador)
#next(generador)
for i in range(0, 20000):
    next(generador)
