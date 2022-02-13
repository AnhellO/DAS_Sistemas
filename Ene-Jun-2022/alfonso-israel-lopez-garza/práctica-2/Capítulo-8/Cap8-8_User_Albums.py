def make_album(artist_name,album_title,tracks=""):
    '''Crea un diccionario con nombre del artista, titulo del album y numero de tracks(opcional)'''
    dictionary = {'Nombre del artista':artist_name, 'Titulo del album': album_title}
    if tracks:
        dictionary['Tracks'] = tracks
    return dictionary

while True:
    salida = input("Si desea salir ingrese (q) ")
    if salida == 'q':
        break
    artista = input("Nombre del artista: ")
    album = input("Titulo del album: ")
    num_traks = input("Numero de tracks: (opcional) ")
    diccionario = make_album(artista,album,num_traks)
    print(diccionario)