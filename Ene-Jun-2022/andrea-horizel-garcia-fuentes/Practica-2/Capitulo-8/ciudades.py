#8.6
def city_country(ciudad, pais):
    
    return(ciudad.title() + ", " + pais.title())

ciudad = city_country('santiago', 'chile')
print(ciudad)

ciudad = city_country('Cancun', 'Mexico')
print(ciudad)

ciudad = city_country('Madrid', 'España')
print(ciudad)
