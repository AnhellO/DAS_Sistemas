#8.1
def display_message():
    print("Estoy aprendiendo funciónes!!")

display_message()

#8.2
def favorite_book(Libro):
    print("Uno de mis libros favoritos es: " + Libro.title() + " !")

favorite_book('La Biblia')

#8.3
def make_shirt(Tamaño, Mensaje):
    print("Talla: " + Tamaño + ", Descripcion: " + Mensaje + ".")

make_shirt('Mediana' , 'Victor')
make_shirt(Tamaño='Mediana' , Mensaje='Victor')

#8.4
def make_shirt2(Tamaño = 'Grande', Mensaje = 'Me encanta python'):
    print("Talla: " + Tamaño + ", Descripcion: " + Mensaje + ".")

make_shirt2()

def make_shirt3(Tamaño, Mensaje = 'Me encanta python'):
    print("Talla: " + Tamaño + ", Descripcion: " + Mensaje + ".")

make_shirt3(Tamaño = 'Mediana')
make_shirt3(Tamaño = 'Grande')

def make_shirt4(Tamaño, Mensaje = 'Prefiero Java'):
    print("Talla: " + Tamaño + ", Descripcion: " + Mensaje + ".")

make_shirt4(Tamaño = 'Chica')

#8.5
def describe_city(ciudad, pais = 'Canada'):
    print(ciudad + " esta en " + pais)

describe_city(ciudad = 'Vancouver')
describe_city(ciudad = 'Toronto')
describe_city(ciudad = 'Bangalore')

#8.6
def city_country(ciudad, Pais):
    ciudad_completa = ciudad + ', ' + Pais
    return ciudad_completa

Union = city_country('Mumbai','India')
print(Union)
Union2 = city_country('Nueva Delhi','India')
print(Union2)
Union3 = city_country('Vadodara','India')
print(Union3)

#8.7
def make_album(artista, album):
    album = {'Artista': artista, 'Album': album}
    return album

Union4 = make_album('Herencia Cristiana', 'Entre Tu y Yo')
print(Union4)
Union5 = make_album('Herencia Cristiana', 'Ama')
print(Union5)
Union6 = make_album('Herencia Cristiana', 'Aquio estoy de nuevo')
print(Union6)
def make_album2(artista, album, pistas):
    album = {'Artista': artista, 'Album': album, 'Pistas': pistas}
    return album

Union7 = make_album2('Herencia Cristiana', 'Fuego que quema', '5')
print(Union7)
bandera = True
while bandera == True:
    bandera = False
    print("\n Por favor ingresa valores:")
    artist = input("Artista: ")
    
    albuum = input("Album: ")
    
    Unir_album = make_album(artist, albuum)
    print(Unir_album)


#8.9    
lista = ['Harry', 'Hermione', 'Ron']    
def show_magicians(Mago):
    print(Mago)    


show_magicians(lista)

#8.10
def make_great():
    print("The great " + lista[0] + ", The great " + lista[1] + ", The great " + lista[2])

make_great()

#8.11
def make_great2():
    Nueva_Lista = ['The great ' + lista[0] + ', The great ' + lista[1] + ', The great ' + lista[2]] 
    return Nueva_Lista

Nueva_Lista2 = make_great2()
print(lista)
print(Nueva_Lista2)


#8.12
def sandwich():
    Cantidad = int(input("Cantidad de ingredientes: "))
    Lista_ingredientes = []
    while 0 != Cantidad:
        Ingrediente = input("Ingrediente: ")
        Lista_ingredientes.append(Ingrediente)
        Cantidad -= 1

    print(Lista_ingredientes) 
    
sandwich()

#8.13
def build_profile(first, last, **user_info):    
    profile = {}     
    profile['first_name'] = first    
    profile['last_name'] = last    
    #for key, value in user_info.items():        
	#    profile[key] = value
    return profile

user_profile = build_profile('Victor', 'De Leon', location='Mexico', field='Desarollador')
print(user_profile)

#8.14
def make_car(Nombre, Valor, color, tow_package ):
    listaa = 'Nombre: ' + Nombre, ' Valor: ' + Valor, ' Color: ' + color, ' tow_packege: ' + tow_package
    return listaa

car = make_car('subaru', 'outback', color='blue', tow_package='True')
print(car)
