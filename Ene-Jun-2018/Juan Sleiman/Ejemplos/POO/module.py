#argumentos staticos
def print_n_times(n, *text):
    for i in range(0,n):
    print(text)

print_n_times(5, ':v')

#Argumentos variables
def print_n_times_variable(n, *text):
    for i in range (0, n):
        print(text)

def print_n_times_keyword(n, **text):
    for i in range(0, n):
        print(text)
