
glossary = {'if': 'Condicional', 'for': 'Ciclo con contador', 'elif': 'condicional seguido de otro condicional', 'dictionary': 'like a glossary', 'def': 'used to create a functions'}

def print_formatted_dict(dictionary):

    for conditional, meaning in dictionary.items():
        print("{} : {}".format(conditional, meaning))

print_formatted_dict(glossary)

def add_more_to_glossary(dictionary):
    dictionary['interface'] = 'its like a assigment'
    dictionary['classes'] = 'used to make classes'
    dictionary['db'] = ' databases'
    dictionary['files'] = ' files used to write code'
    dictionary['imports'] = 'use of atributes or methods in other files'

add_more_to_glossary(glossary)
print_formatted_dict(glossary)