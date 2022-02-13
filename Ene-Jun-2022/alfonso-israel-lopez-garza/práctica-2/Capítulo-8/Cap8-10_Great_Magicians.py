def make_great(magos):
    '''Imprime un saludo para cada mago'''
    for mago in magos:
        print("The great "+mago)

magicians = ['Harry Houdini','Dai Vernon','Criss Angel','Dynamo']
make_great(magicians)