def memoize(fn):#funcion hace cahing de los resultados de una funcion
    cache = {}#diccionario que almacena los resultados de fibonacci para cada n
#La pasamos a memoize la funcion que vamos a decorar
    def wrapper(*args, **kwargs):
        if args not in cache:#argumentos que se le pasan a la funcion para meterlos dentro del cache
            cache[args] = fn(*args, **kwargs)
        return cache[args]# si no existe lo guardamos y si existe regresamos lo que este en el cahe(diccionario)
    return wrapper
