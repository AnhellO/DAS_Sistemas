def show_magicians(magos):
    '''Imprime cada mago'''
    for mago in magos:
        print(mago)

def make_great(magicians):
    magos = []
    '''Agrega un saludo para cada mago'''
    for i in magicians:
        magos.append("The great " +i)
    return magos

magicians = ['Harry Houdini','Dai Vernon','Criss Angel','Dynamo']
mago = make_great(magicians[:])

show_magicians(magicians)
show_magicians(mago)