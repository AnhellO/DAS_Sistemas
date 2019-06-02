from databaseAnime import DataBase
from parte1 import APIFactory

def main():
    db = DataBase('AnimeMangaCharacter.db')
    animes = APIFactory.apiType('anime')
    lista_animes = animes.makeGet()
    mangas = APIFactory.apiType('manga')
    lista_mangas = mangas.makeGet()
    characters = APIFactory.apiType('characters')
    lista_characters = characters.makeGet()
    #for i in range(15):
    #    print(db.saveAnime(lista_animes[i]))
    #    print(db.saveManga(lista_mangas[i]))
    #    print(db.saveCharacter(lista_characters[i]))



    print(*db.showAnimes(), sep='\n')
    print(*db.showMangas(), sep='\n')
    print(*db.showCharacters(), sep='\n')


if __name__ == '__main__':
    main()
