magos=['daniel','juan','pedro','luis']

def make_great(magos):
    temporal=[]
    while magos:

        result = magos.pop()
        temporal.append('El gran '+result)

    while temporal:

        result2 = temporal.pop()
        magos.append(result2)

def show_magicians(magos):
    for mago in magos:
        print(mago)

make_great(magos)
show_magicians(magos)

#for i in range(0, len(lista)):
    #lista[i] += 'el gran'
