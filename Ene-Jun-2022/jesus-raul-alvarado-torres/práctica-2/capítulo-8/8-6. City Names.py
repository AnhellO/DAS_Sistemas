""" Practica 8-6 - City Names

Write a function called city_country() that takes in the name
of a city and its country. The function should return a string
formatted like this:     "Santiago, Chile"
Call your function with at least three city-country pairs,
and print the value that’s returned."""

def city_country(Ciudad, País):
    return f"{Ciudad.title()}, {País.title()}"

Ciudad = city_country('Saltillo', 'México')
print(Ciudad)
Ciudad = city_country('Monterrey', 'México')
print(Ciudad)
Ciudad = city_country('Nueva York', 'Estados Unidos')
print(Ciudad)