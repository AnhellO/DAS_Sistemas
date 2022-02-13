""" Practica 8-5 - Cities

Write a function called describe_city() that accepts the name of
a city and its country. The function should print a simple sentence, such as
Reykjavik is in Iceland. Give the parameter for the country a default value.
Call your function for three different cities, at least one of which is not in the
default country."""

def describe_city(Ciudad, País='México'):
    txt = f"{Ciudad.title()} está en {País.title()}."
    print(txt)

describe_city('Saltillo')
describe_city('Monterrey')
#   No está en el pais por defecto
describe_city('Nueva York', 'Estados Unidos')