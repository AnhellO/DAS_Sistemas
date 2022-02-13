""" Practica 8-14 - Cars

Write a function that stores information about a car in a diction-
ary . The function should always receive a manufacturer and a model name . It
should then accept an arbitrary number of keyword arguments. Call the func-
tion with the required information and two other name-value pairs, such as a
color or an optional feature . Your function should work for a call like this one:

car = make_car('subaru', 'outback', color='blue', tow_package=True)

Print the dictionary that’s returned to make sure all the information was
stored correctly."""

from enum import auto


def make_car(fabricante, modelo, **detalles):
    dicc_auto ={'Fabricante': fabricante.title(),
               'Modelo': modelo.title(),}

    for detalle, value in detalles.items():
        dicc_auto[detalle] = value

    return dicc_auto

Auto = make_car('Mazda', 'CX-5', color='Negro')
print(Auto)

Camioneta = make_car('Jeep', 'Cherokee', color='Gris', año='2003')
print(Camioneta)