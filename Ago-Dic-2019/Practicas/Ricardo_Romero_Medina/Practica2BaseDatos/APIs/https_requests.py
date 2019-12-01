import requests
import usuario
import basedatos

class traer_usuario():
    r = requests.get('https://jsonplaceholder.typicode.com/users')
    text = r.json()
    basedatos.crear_tabla()

    for texto in text:
        usua = usuario.usuarios(texto['id'],texto['name'],texto['username'],texto['email'],texto['address']['street'],texto['address']['suite'],texto['address']['city'],texto['address']['zipcode'],texto['address']['geo']['lat'],texto['address']['geo']['lng'],texto['phone'],texto['website'],texto['company']['name'],texto['company']['catchPhrase'],texto['company']['bs'])
        basedatos.Insertar(usua)

#traer_usuario()
#basedatos.Ver_Todos_Usuarios()
basedatos.Ver_Un_Usuario(2)
