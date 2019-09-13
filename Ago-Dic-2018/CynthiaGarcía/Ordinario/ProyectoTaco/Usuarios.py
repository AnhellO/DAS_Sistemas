from tacoCRUD import Crud
import requests
import json


class Usuario():
    def __init__(self):
        self.url = 'https://randomuser.me/api/'

    def getUsuarioRandom(self):
        request = requests.get(self.url)
        self.nombre = request.json()['results'][0]['name']['first']
        self.apellido = request.json()['results'][0]['name']['last']
        self.calle = request.json()['results'][0]['location']['street']
        self.ciudad = request.json()['results'][0]['location']['city']
        self.correo = request.json()['results'][0]['email']
        self.nombreusuario = request.json()['results'][0]['login']['username']
        return self

 #usuario = Usuario()s
 #u = usuario.getUsuarioRandom()

 #c = Crud()
 #c.agregaUsuario(u.nombre, u.apellido, u.calle, u.ciudad, u.correo, u.nombreusuario)
