from slugify import slugify
import argparse

parser = argparse.ArgumentParser(description= 'convertir a diferentes formatos')
parser.add_argument('name', metavar='str', nargs='*')
parser.add_argument('-slug', '--slug',action='store_true',help='Convertir a slug')
parser.add_argument('-mayus', '--mayus', action='store_true', help='Convertir a mayusculas')
parser.add_argument('-minus', '--minus', action='store_true', help='Convertir a minusculas')
parser.add_argument('-ascii', '--ascii', action='store_true', help='Convertir a codigo ascii')
parser.add_argument('-reverse', '--reverse', action='store_true', help='Nombre invertido')
args = parser.parse_args()

def Slug(name):
    nombre = name
    return 'Nombre --> Slug: '+slugify(nombre)

def Mayus(name):
    nombre = name
    return 'Nombre --> Mayus: '+nombre.upper()

def Minus(name):
    nombre = name
    return 'Nombre --> Minus: '+nombre.lower()

def Ascii(name):
    nombre = name
    sum=0
    for letra in nombre:
        sum+=ord(letra)
    return 'Nombre --> ASCII: '+str(sum)

def Invertido(name):
    nombre = name
    invertido=nombre[::-1]
    return 'Nombre --> Invertido: '+invertido

if __name__ == '__main__':
    slug = Slug(args.name)
    mayus = Mayus(args.name)
    minus = Minus(args.name)
    ascii = Ascii(args.name)
    inv = Invertido(args.name)
    print('El nombre proporcionado es *'+args.name+ '*')
    if args.slug:
        print(slug)
    if args.mayus:
        print(mayus)
    if args.minus:
        print(minus)
    if args.ascii:
        print(ascii)
    if args.inv:
        print(inv)