def describe_city(city='Saltillo', country='México'):
    '''Función que muestra en pantalla la ciudad y de que pais es.'''
    print(f"{city} es en {country}.")

describe_city() #Usando los 2 argumentos por defecto
describe_city('Monterrey') #Cambiando el primer argumento por Monterrey
describe_city(city='Tokio', country='Japon') #Cambiando el valor de ambos argumentos