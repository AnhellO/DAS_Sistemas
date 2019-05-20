from API_Marvel import makeGet
from database import DataBase

def main():
    db = DataBase('avengers.db')
    print(
    """¡BIENVENIDO A MARVEL!\n¿Tienes curiosidad de conocer los personajes de la tetralogía de Avengers?\nSelecciona:
    1. Buscar personajes de la pelicula "The Avengers"
    2. Buscar personajes de la pelicula "Avengers:Age of Ultron"
    3. Buscar personajes de la pelicula "Avengers:Infinity War"
    4. Guardar en base de datos los personajes de "The Avengers"
    5. Guardar en base de datos los personajes de "Avengers:Age of Ultron"
    6. Guardar en base de datos los personajes de "Avengers:Infinity War"
    7. Mostrar los personajes en "The Avengers"
    8. Mostrar los personajes en "Avengers:Age of Ultron"
    9. Mostrar los persoajes en "Avengers:Infinity War"
    0. Salir \n--------------------------------------------------------------------------
    """)
    pelicula= int(input())
    print('\n')
    while pelicula!=0:
        if pelicula == 1:
            lista = makeGet(pelicula)
            print('***************THE AVENGERS***************\n')
            for i in range(len(lista)):
                print('Personaje: '+str(i+1))
                print(lista[i])
                print("\n")
        if pelicula == 2:
            lista = makeGet(pelicula)
            print('***************THE AVENGERS: AGE OF ULTRON***************\n')
            for i in range(len(lista)):
                print('Personaje: '+str(i+1))
                print(lista[i])
                print("\n")
        if pelicula == 3:
            print('***************THE AVENGERS: INFINITY WAR***************\n')
            lista = makeGet(pelicula)
            for i in range(len(lista)):
                print('Personaje: '+str(i+1))
                print(lista[i])
                print("\n")
        if pelicula == 4:
            lista = makeGet(1)
            print('***************THE AVENGERS***************\n')
            for i in range(len(lista)):
                print('Personaje: '+str(i+1))
                print(lista[i])
                print("\n")
            print('¿Cuál personaje quieres guardar?\nTeclea el número de personaje')
            print('Quieres guardar todos los personajes?\nTeclea 0')
            personaje = int(input())
            if personaje == 0:
                for p in lista:
                    db.SaveCharacter(p)
            elif personaje > len(lista) or personaje < 0:
                print('No existe ese personaje. Elije otro')
            else:
                print(db.SaveCharacter(lista[personaje-1]))
        if pelicula == 5:
            lista = makeGet(2)
            print('***************THE AVENGERS: AGE OF ULTRON***************\n')
            for i in range(len(lista)):
                print('Personaje: '+str(i+1))
                print(lista[i])
                print("\n")
            print('¿Cuál personaje quieres guardar?\nTeclea el número de personaje')
            print('Quieres guardar todos los personajes?\nTeclea 0')
            personaje = int(input())
            if personaje == 0:
                for p in lista:
                    db.SaveCharacter(p)
            elif personaje > len(lista) or personaje < 0:
                print('No existe ese personaje. Elije otro')
            else:
                print(db.SaveCharacter(lista[personaje-1]))
        if pelicula == 6:
            lista = makeGet(3)
            print('***************THE AVENGERS: INFINITY WAR***************\n')
            for i in range(len(lista)):
                print('Personaje: '+str(i+1))
                print(lista[i])
                print("\n")
            print('¿Cuál personaje quieres guardar?\nTeclea el número de personaje')
            print('Quieres guardar todos los personajes?\nTeclea 0')
            personaje = int(input())
            if personaje == 0:
                for p in lista:
                    db.SaveCharacter(p)
            elif personaje > len(lista) or personaje < 1:
                print('No existe ese personaje. Elije otro')
            else:
                print(db.SaveCharacter(lista[personaje-1]))

        if pelicula == 7:
            lista = db.ShowCharacters(1)
            print("PERSONAJES DE LA PELICULA 'THE AVENGERS'")
            if type(lista)==str:
                print(lista+"\n")

            else:
                for i in range(len(lista)):
                    print('Personaje: '+str(i+1))
                    print(lista[i])
                    print("\n")
        if pelicula == 8:
            lista = db.ShowCharacters(2)
            print("PERSONAJES DE LA PELICULA 'THE AVENGERS: AGE OF ULTRON'")
            if type(lista)==str:
                print(lista+"\n")
            else:
                for i in range(len(lista)):
                    print('Personaje: '+str(i+1))
                    print(lista[i])
                    print("\n")
        if pelicula == 9:
            lista = db.ShowCharacters(3)
            print("PERSONAJES DE LA PELICULA 'THE AVENGERS: INFINITY WAR'")
            if type(lista)==str:
                print(lista+"\n")
            else:
                for i in range(len(lista)):
                    print('Personaje: '+str(i+1))
                    print(lista[i])
                    print("\n")



        print(
        """¡BIENVENIDO A MARVEL!\n¿Tienes curiosidad de conocer los personajes de la tetralogía de Avengers?\nSelecciona:
        1. Buscar personajes de la pelicula "The Avengers"
        2. Buscar personajes de la pelicula "Avengers:Age of Ultron"
        3. Buscar personajes de la pelicula "Avengers:Infinity War"
        4. Guardar en base de datos los personajes de "The Avengers"
        5. Guardar en base de datos los personajes de "Avengers:Age of Ultron"
        6. Guardar en base de datos los personajes de "Avengers:Infinity War"
        7. Mostrar los personajes en "The Avengers"
        8. Mostrar los personajes en "Avengers:Age of Ultron"
        9. Mostrar los persoajes en "Avengers:Infinity War"
        0. Salir \n--------------------------------------------------------------------------
        """)
        pelicula= int(input())
        print('\n')

if __name__ == '__main__':
    main()
