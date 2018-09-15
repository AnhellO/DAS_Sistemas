def show_magicians(nombres_magos):
    for magician in nombres_magos:
        print(magician)

def make_great(nombres_magos):
    great_magicians = []

    while nombres_magos:
        mago = nombres_magos.pop()
        great_magician = mago + ' the Great'
        great_magicians.append(great_magician)

    for great_magician in great_magicians:
        nombres_magos.append(great_magician)

    return nombres_magos

nombres_magos = ['Luis', 'Pedro', 'Antonio']
show_magicians(nombres_magos)

print("\nGrandes Magos:")
great_magicians = make_great(nombres_magos[:])
show_magicians(great_magicians)

print("\nMagos Originales:")
show_magicians(nombres_magos)
