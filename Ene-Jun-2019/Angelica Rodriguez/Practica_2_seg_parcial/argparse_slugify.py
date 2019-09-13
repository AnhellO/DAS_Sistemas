import argparse
from slugify import slugify

parser = argparse.ArgumentParser(description='Process some names.')
parser.add_argument('names', metavar='str', nargs='*')
parser.add_argument('--slug', dest='slugify', action='store_const', const=str)
parser.add_argument('--mayus',dest='mayusculas', action='store_const', const=str)
parser.add_argument('--minus', dest='minusculas', action='store_const',const=str)
parser.add_argument('--ascii', dest='codigo_ascii', action='store_const',const=str)
parser.add_argument('--reverse', dest='invertir', action='store_const', const=str)

def transform(list):
    a = ""
    for i in list:
        a = a + i + " "
    return a

if __name__ == '__main__':
    args = parser.parse_args()
    list = args.names
    text = transform(list)

    print("El nombre proporcionado es *{}*:".format(text.rstrip()))
    if args.slugify:
        print("- Su valor en slug es: {}".format(slugify(text)))

    if args.mayusculas:
        print("- Su valor en mayúsculas es: {}".format(text.upper()))

    if args.minusculas:
        print("- Su valor en minúsculas es: {}".format(text.lower()))

    if args.codigo_ascii:
        sum = 0
        for letter in text.rstrip():
            sum+=ord(letter)
        print("- Su valor en ascii es: {}".format(sum))

    if args.invertir:
        print("- Su valor invertido es: {}".format(text[::-1].lstrip()))
