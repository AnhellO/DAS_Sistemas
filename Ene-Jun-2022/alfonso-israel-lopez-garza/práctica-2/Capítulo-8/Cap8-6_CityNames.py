def city_country(city,country):
    '''Une la ciudad y el pais con formato ("Santiago, Chile")'''
    ubicacion = '"'+city +', ' +country +'"'
    return ubicacion.title()

for i in range(3):
    ciudad = input("Ingrese la ciudad: ")
    pais = input("Ingrese el pais: ")
    localidad = city_country(ciudad,pais)
    print(localidad)