from collections import OrderedDict

glosary = OrderedDict()

glosary['class'] = 'extensible program-code-template for creating objects'
glosary['object'] = 'objects are the things you think about first in designing a program'
glosary['instance'] = 'is a specific realization of any object'
glosary['inheritance'] = 'the procedure in which one class inherits the attributes and methods of another class'
glosary['syntax'] = 'the rules that define the structure of a language'

for word, meaning in glosary.items():
    print(f"{word.title()}: {meaning}")
