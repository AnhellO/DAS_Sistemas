from faker import Faker
fake = Faker()

#Abrir el archivo
#archivo = open('README.md','r')

#Leer el archivo usamos ‘r’: Por defecto, para leer el fichero.
with open('README.md', 'r') as file :
    archivo = file.read()

# Remplazamos la palabra 'Python con faker'
nombre_falso = fake.name()
archivo = archivo.replace('Python', str(nombre_falso))

# Escribimos el remplazo usando 'w' para escribir, en el fichero
with open('README.md', 'w') as file:
  file.write(archivo)