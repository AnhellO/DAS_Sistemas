def decorator(f):
    def wrapper():
        return '<Hola> \n' + f() + '\n<Pinsheputita>'
    return wrapper

@decorator
def díHola():
    return 'Que hongos prro? :v'

#print(díHola())

#díHola = decorator(díHola)

print (díHola())
