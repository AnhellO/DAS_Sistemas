def decorator(f):
    def wrapper():
        return '<Los compas> \n' + f() + '\n<Que siempre la cotorrean>'
    return wrapper

@decorator
def díHola():
    return 'Un tremendo saludote :v'

#print(díHola())

#díHola = decorator(díHola)

print (díHola())
