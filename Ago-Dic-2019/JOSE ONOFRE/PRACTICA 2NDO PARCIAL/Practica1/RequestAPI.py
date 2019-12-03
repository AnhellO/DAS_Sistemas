import requests
import pprint
import ClaseUsers
import UsersBD

r = requests.get('https://jsonplaceholder.typicode.com/users')

#print(r)
#pprint.pprint(r.json())

todo = r.json()
#pprint.pprint(todo)

for usuario in todo:
    objeto = ClaseUsers.Usuarios(id = usuario['id'], name = usuario['name'], username = usuario['username'], email = usuario['email'], address = usuario['address'], addressgeo = usuario['address']['geo'], phone = usuario['phone'], website = usuario['website'], company = ['company'])
    print('\n----------Datos del usuario-------------\n')
    #print(objeto)
    UsersBD.insertarUsuario(objeto)

#UsersBD.VisualizarUsuarios()

