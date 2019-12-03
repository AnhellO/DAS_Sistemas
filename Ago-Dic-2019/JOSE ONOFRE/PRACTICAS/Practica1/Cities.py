cities = {
    'Yucatan': {
        'pais': 'Mexico',
        'poblacion': 6158080,
        'Maravilla': 'Chichen Itza',
        },
    'Roma': {
        'pais': 'Italia',
        'poblacion': 60500000,
        'Maravilla': 'Coliseo',
        },
    'Cuzco': {
        'pais': 'Peru',
        'poblacion': 32170000,
        'Maravilla': 'Machu Pichu',
        }
    }

for city, city_info in cities.items():
    country = city_info['pais'].title()
    population = city_info['poblacion']
    mountains = city_info['Maravilla'].title()

    print("\n" + city.title() + " esta en " + country + ".")
    print("  Tiene una poblacion de  " + str(population) + ".")
    print("  EL " + mountains + " es la maravilla que tiene.")