""" Practica 8-15 - Printing Models

Put the functions for the example print_models.py in a
separate file called printing_functions.py. Write an import statement at the top
of print_models.py, and modify the file to use the imported functions."""

import printing_functions as pf

unprinted_designs = ['Funda iphone', 'Robot', 'Dron']
completed_models = []

pf.print_models(unprinted_designs, completed_models)
pf.show_completed_models(completed_models)