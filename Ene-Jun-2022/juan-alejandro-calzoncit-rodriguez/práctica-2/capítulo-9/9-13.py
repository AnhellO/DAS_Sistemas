from collections import OrderedDict

glossary = OrderedDict()

glossary['string'] = 'A series of characters.'
glossary['comment'] = 'A note in a program that the Python interpreter ignores.'
glossary['list'] = 'A collection of items in a particular order.'
glossary['loop'] = 'Work through a collection of items, one at a time.'
glossary['dictionary'] = 'A collection of key-value pairs.'
glossary['conditional test'] = 'A comparison between two values.'


for word, definition in glossary.items():
    print("\n" + word.title() + ": " + definition)