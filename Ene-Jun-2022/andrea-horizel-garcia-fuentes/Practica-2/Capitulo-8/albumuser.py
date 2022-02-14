def make_album(artista, titulo, tracks=0):
    #8.8
    album_dict = {
        'artista': artista.title(),
        'titulo': titulo.title(),
        }
    if tracks:
        album_dict['canciones'] = tracks
    return album_dict
    
titulo_prompt = "\nque album es tu favorito? "
artista_prompt = "que artista es? "

print("ingrese en detener.")

while True:
    titulo = input(titulo_prompt)
    if titulo== 'quit':
        break
    
    artista = input(artista_prompt)
    if artista == 'quit':
        break

    album = make_album(artista, titulo)
    print(album)

print("\ngracias por tu respuesta!")