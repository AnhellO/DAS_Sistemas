def decorar(func):
    print("Decorando la función %s..." %func.__name__)
    def wrapper(*args,**kwargs):#*args y **kwargs te permiten pasar un numero variable de argumentos a una función
        print("Llamando a la función enredada con argumentos:", args)
        if func.__name__ == 'resta':
            a, b = args
            args = (a*a, b*b)
        return func(*args, **kwargs)
    print ("Fin!")
    return wrapper

@decorar
def suma(a, b):
    return a + b

@decorar
def resta(a,b):
    return a - b

s = suma(3,4)
r = resta(3,4)
print (s)
print(r)
