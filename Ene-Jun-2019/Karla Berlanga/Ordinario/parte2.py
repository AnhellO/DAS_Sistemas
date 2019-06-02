from mailchimp3 import MailChimp

""" Se crea una clase para representar los métodos que nos
proporciona el paquete mailchimp3 para poder conectarse a la API de MailChimp """

class Chimp():
    def __init__(self):
        #Se inicializa el cliente con la api generada en la pagina web y nuestro usuario
        self.client = MailChimp(mc_api='591cd04cce86613128dc359476d8ac99-us20', mc_user='kberlanga')

    def getAudiences(self):
        #En este método llamamos las audiencias/listas que tenemos en nuestra cuenta
        return self.client.lists.all(get_all=True, fields="lists.name,lists.id")

    def addMember(self,id, data):
        """En este método agregamos contactos a nuestras audiencias/listas existentes
        recibiendo como parametros el id de la lista a la que vamos a agregar el contacto
        y los datos del contacto en un diccionario con los siguientes datos:
                data = {
                'email_address': contacto['email'],
                'status': 'subscribed',
                'merge_fields': {
                'FNAME': contacto['first'],
                'LNAME': contacto['last'],
                    },
                }
        """
        self.client.lists.members.create(id,data)

    def getMembers(self, id):
        #Este método provee los contactos que existen en determinada lista, dando como
        #parametro el id de la lista y retorna una lista de los contactos
        resultado = self.client.lists.members.all(id, get_all=True)
        members = []
        for member in resultado['members']:
            full_name = member['merge_fields']
            first = full_name['FNAME']
            last = full_name['LNAME']
            email = member['email_address']
            data = {'first':first, 'last':last, 'email':email}
            members.append(data)
        return members





def main():
    mc= Chimp()
    #Se traen las listas existentes
    audiencias = mc.getAudiences()['lists']
    i=1
    #Se imprimen las Audencias, su nombre y su id
    print("--------------Audiencias-----------")
    for list in audiencias:
        print("N°: "+str(i))
        print("Id: "+list['id'])
        print("Nombre: " + list['name'])
        i+=1

    #Se da la opcion de elegir a que audencia se quiere agregar uno o más contactos
    print("\nElige una Audencia para agregar/ver a tus contactos")
    id = int(input())

    contactos = [
    {'first': 'Nohemi Esther', 'last':'Flores Pardo', 'email':'nooemii.chaaparra@gmail.com'},
    {'first': 'Angelica Maria', 'last':'Rodriguez Cabello', 'email':'angelica_marc@hotmail.com'},
    {'first': 'Erik Eduardo', 'last':'Montoya Martinez', 'email':'erikmontoya15@icloud.com'},
    {'first': 'Luis Alberto', 'last':'Ornelas Hinojosa', 'email':'luis_al_or@hotmail.com'},
    {'first': 'José Alberto', 'last':'Peralta Valdes', 'email':'joseaperaltav@hotmail.com'},
    {'first': 'Juan de Dios', 'last':'Almaguer Constante', 'email':'jdac_06@hotmail.com'},
    {'first': 'Angel Santiago', 'last':'Jaime Zavala', 'email':'asjz2892@gmail.com'}
    ]

    for contacto in contactos:
        #Se filtran los datos de los contactos de tal manera que quede la estructura que acepta
        #la API para hacer el post
        data = {
        'email_address': contacto['email'],
        'status': 'subscribed',
        'merge_fields': {
        'FNAME': contacto['first'],
        'LNAME': contacto['last'],
            },
        }
        #Se agrega cada contacto
        #mc.addMember(audiencias[id-1]['id'], data)

    #Se imprimen los contactos de determinada lista
    print(*mc.getMembers(audiencias[id-1]['id']))



if __name__ == '__main__':
    main()
