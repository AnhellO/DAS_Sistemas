from faker import Faker
fake = Faker(['en_US'])

filename = 'README.md'

with open(filename,'r') as f:
    text = f.read()

#       Cambio los Python x python, sin mayuscula
camb1= text.replace('Python', 'python')
#       Cambio python por nombres aleatorios
camb2 = camb1.replace('python',fake.name())

#       Write nuevo archvio
with open('README-ALTERADO.md','w') as f:
    f.write(camb2)