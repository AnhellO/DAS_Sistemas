from mailchimp3 import MailChimp

class MailChimpListas():
    def __init__(self):
        # llave y usuario
        self.client = MailChimp(mc_api='3094e19582b69b6cfc001555b6ef170b-us20', mc_user='angiie_rdzc')

    def addContactToList(self, email, first_name, last_name):
        # método para agregar contactos a la lista
        self.client.lists.members.create('8dbaa21fc4', {
            'email_address': email,
            'status': 'subscribed',
            'merge_fields': {
                'FNAME': first_name,
                'LNAME': last_name,
            },
        })

    def getList(self):
        # ver los contactos que hay en la lista
        suscriptores = self.client.lists.members.all('8dbaa21fc4', count=100, offset=0, fields="members.email_address")
        return suscriptores

def main():
    chimp = MailChimpListas()
    # contactos a guardar en la lista
    contacts = [{"email": "nooemii.chaaparra@gmail.com", "first_name": "Noemi", "last_name": "Flores"},
                {"email": "erikmontoya15@Icloud.com", "first_name": "Erik", "last_name": "Montoya"},
                {"email": "luis_al_or@hotmail.com", "first_name": "Luis", "last_name": "Ornelas"},
                {"email": "joseaperaltav@hotmail.com", "first_name": "Jose", "last_name": "Peralta"},
                {"email": "jdac_06@hotmail.com", "first_name": "Juan", "last_name": "Almaguer"},
                {"email": "karla_berlanga28@hotmail.com", "first_name": "Karla", "last_name": "Berlanga"},
                {"email": "asjz2892@gmail.com", "first_name": "Angel", "last_name": "Jaime"}]

    for contact in contacts:
        # agregando contactos
        chimp.addContactToList(contact['email'], contact['first_name'], contact['last_name'])

    # imprimimos la lista de suscriptores
    print("LISTA DE SUSCRIPTORES:\n" , chimp.getList())

if __name__ == "__main__":
    main()
