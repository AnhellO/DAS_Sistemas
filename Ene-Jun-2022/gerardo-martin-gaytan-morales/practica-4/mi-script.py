#1.- importar faker
from faker import Faker

fake = Faker()

#2.- leer archivo markdown
with open('README.md', 'r') as f:
    text = f.read()

#3.- rempazar las palabras Python o python por nombres
lowpython = text.replace('Python','python')
change = lowpython.replace('python',fake.name())
print(change)

#4.- escribir el resultado en un archivo markdown
with open('README-ALTERADO.md', 'w') as f:
    f.write(change)

