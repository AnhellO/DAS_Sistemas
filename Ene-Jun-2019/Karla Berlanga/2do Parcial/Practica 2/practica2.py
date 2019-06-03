from slugify import *
import argparse

parser = argparse.ArgumentParser(description= 'Nombres en diferentes formatos')
parser.add_argument('nombre', help='Primer y/o segundo nombre de la persona')
parser.add_argument('apellido', help='Primer y/o segundo apellido de la persona')
parser.add_argument('-slug', '--slug',action='store_true',help='Conversion del nombre a un slug valido')
parser.add_argument('-mayus', '--mayus', action='store_true', help='Conversion del nombre a mayusculas')
parser.add_argument('-minus', '--minus', action='store_true', help='Conversion del nombre a minusculas')
parser.add_argument('-ascii', '--ascii', action='store_true', help='Conversion del nombre a codigo ASCII')
parser.add_argument('-reverse', '--reverse', action='store_true', help='Invertir el nombre')
args = parser.parse_args()

def toSlug(nombre, apellido):
    completo = nombre+' '+ apellido
    return 'Su valor en slug es: '+slugify(completo)

def toUpper(nombre, apellido):
    completo = nombre+' '+ apellido
    return 'Su valor en mayusculas es: '+completo.upper()

def toLower(nombre, apellido):
    completo = nombre+' '+ apellido
    return 'Su valor en minusculas es: '+completo.lower()

def toAscii(nombre, apellido):
    completo = nombre + ' '+ apellido
    sum=0
    for letra in completo:
        sum+=ord(letra)
    return 'Su valor en codigo ASCII es: '+str(sum)

def toReverse(nombre, apellido):
    completo = nombre + ' '+ apellido
    invertido=completo[::-1]
    return 'Su valor invertido es: '+invertido

if __name__ == '__main__':
    slug = toSlug(args.nombre, args.apellido)
    mayus = toUpper(args.nombre, args.apellido)
    minus = toLower(args.nombre, args.apellido)
    ascii = toAscii(args.nombre, args.apellido)
    reverse = toReverse(args.nombre, args.apellido)
    print('El nombre proporcionado es *'+args.nombre + ' '+ args.apellido+'*')
    if args.slug:
        print(slug)
    if args.mayus:
        print(mayus)
    if args.minus:
        print(minus)
    if args.ascii:
        print(ascii)
    if args.reverse:
        print(reverse)
