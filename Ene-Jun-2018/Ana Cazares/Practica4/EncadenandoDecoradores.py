AUTHENTICATED = True

def autenticado(f):
    def inner(*args, **kwargs):
        print ("Yo autentico")
        if AUTHENTICATED:
            f(*args, **kwargs)
        else:
            raise Exception
    return inner

def aviso(f):
    def inner(*args, **kwargs):
        print ("Yo aviso")
        f(*args, **kwargs)
        print ("Se ejecuto %s" % f.__name__)
    return inner

@autenticado
@aviso
def abrir_puerta():
    print ("Abrir la puerta")

@aviso
@autenticado
def cerrar_puerta():
    print ("Cerrar la puerta")

abrir_puerta()

cerrar_puerta()

# Yo autentico
# Yo aviso
# Abrir la puerta
# Se ejecuto abrir_puerta
# Yo aviso
# Yo autentico
# Cerrar la puerta
# Se ejecuto inner
