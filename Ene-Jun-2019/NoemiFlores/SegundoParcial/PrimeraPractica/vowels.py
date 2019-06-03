f = open('SPECS.md','r')
archivo = f.read().lower()
f.close()
print("A: {}\nE: {}\nI: {}\nO: {}\nU: {}".format(archivo.count('a'),archivo.count('e'),archivo.count('i'),archivo.count('o'),archivo.count('u')))