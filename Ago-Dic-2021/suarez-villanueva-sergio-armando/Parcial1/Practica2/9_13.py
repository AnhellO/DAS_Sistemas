from collections import OrderedDict

d = OrderedDict()
d['Import'] = 'Bring a document'
d['Print'] = 'Print'
d['Class'] = 'Code for creating objects'
d['Def'] = 'To define a method'

for key,value in d.items():
    print(str(key) + ": " + str(value) + "\n")