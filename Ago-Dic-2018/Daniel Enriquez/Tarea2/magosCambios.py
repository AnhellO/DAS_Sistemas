magos=['daniel','juan','pedro','luis']
nueva=magos[:]
temporal=[]
def make_great(nueva):

    while nueva:

        result = nueva.pop()
        temporal.append('El gran '+result)

    while temporal:

        result2 = temporal.pop()
        nueva.append(result2)

def show_magicians(nueva):
    for mago in nueva:
        print(mago)

for mago in magos:
    print(mago)

make_great(nueva)
show_magicians(nueva)
