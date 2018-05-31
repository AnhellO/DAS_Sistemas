def print_n_veces(n, texto):
    for i in range(0, n):
        print(texto)

def print_n_veces_variable(n, *texto):
    for i in range(0, n):
        print(texto)

def print_n_veces_keyword(n, **texto):
    for i in range(0, n):
        print(texto)
