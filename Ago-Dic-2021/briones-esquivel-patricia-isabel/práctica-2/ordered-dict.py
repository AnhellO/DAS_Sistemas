# ------- Ejercicio 9,13- OrderedDict Rewrite -------
from collections import OrderedDict

glossary = OrderedDict()

glossary['whitespace'] = 'Any nonprinting character.'
glossary['float'] = 'The fact that a decimal point can appear at any position in a number.'
glossary['lists'] = 'Ordered collections.'
glossary['string'] = 'Simply a series of characters.'

for word, definition in glossary.items():
    print("\n" + word.title() + ": " + definition)