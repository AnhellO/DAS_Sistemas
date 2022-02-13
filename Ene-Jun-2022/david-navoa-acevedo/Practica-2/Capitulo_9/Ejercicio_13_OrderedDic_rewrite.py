from collections import OrderedDict

glossary = OrderedDict()

glossary['interface'] = 'its like a assigment'
glossary['classes'] = 'used to make classes'
glossary['db'] = ' databases'
glossary['files'] = ' files used to write code'
glossary['imports'] = 'use of atributes or methods in other files'

def print_formatted_dict(dictionary):

    for conditional, meaning in dictionary.items():
        print("{} : {}".format(conditional, meaning))

print_formatted_dict(glossary)