# 6-11. Cities: Make a dictionary called cities. Use the names of three cities as keys in your dictionary.
# Create a dictionary of information about each city and include the country that the city is in,
# its approximate population, and one fact about that city.
# The keys for each city’s dictionary should be something like country, population, and fact.
# Print the name of each city and all of the information you have stored about it.

cities = {
    'Saltillo': {
        'country': 'Mexico',
        'population': 1045000,
        'number of museums': '36',
        },
    'Monterrey': {
        'country': 'Mexico',
        'population': 2300000,
        'number of museums': '18',
        },
    'Guadalajara': {
        'country': 'Mexico',
        'population': 1680285,
        'number of museums': '23',
        }
    }

for city, city_info in cities.items():
    country = city_info['country'].title()
    population = city_info['population']
    museums = city_info['number of museums'].title()

    print("\n" + city.title() + " is in " + country + ".")
    print("  It has a population of about " + str(population) + ".")
    print("  This city has " + museums + " museums.")