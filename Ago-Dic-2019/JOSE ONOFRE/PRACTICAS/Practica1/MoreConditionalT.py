color = 'azul'
print(color  == 'azul')

palabra = 'ambiente'
print('///////////////////////////////')
if palabra != 'mundo':
    print("Las palabras no son iguales!")
print('///////////////////////////////')
tamano = 10
print(tamano==10)

cantidad = 13
if cantidad != 10:
    print("La cantidad no es la indicada")

print('///////////////////////////////')

edad = 17
print(edad<20)

edad = 18
print(edad<=18)
print('///////////////////////////////')
edad1 = 15
edad2 = 22
print(edad1<20 and edad2>21)

cantidad1 = 10
cantidad2 = 30
print(cantidad1<15 or cantidad2<25)

cantidad1 = 100
cantidad2 = 40
print(cantidad1<50 or cantidad2<25)

print('///////////////////////////////')

invitados = ['Marco','Angela','Leo','Raquel','Mario']
user='Angela'

if user in invitados:
    print(user.title()+", eres parte de los invitados")

user='Diego'

if user not in invitados:
    print(user.title()+", no eres parte de los invitados")
