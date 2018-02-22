def logger(debug=False):
    def _logger(func):
        def inner(*args, **kwargs):
            if debug:
                print ("Estoy corriendo en modo debug")
            for i, arg in enumerate(args):
                print ("arg %d:%s" % (i, arg))
            func(*args, **kwargs)
        return inner
    return _logger

@logger(True)  # la decoracion esta en modo debug
def Yo_me_llamo(nombre, apellido):
    print ("Yo me llamo %s" % nombre)

Yo_me_llamo ("Ahmed")

# Imprime
# Estoy corriendo en modo debug
# arg 0:Ahmed
# Yo me llamo Ahmed
