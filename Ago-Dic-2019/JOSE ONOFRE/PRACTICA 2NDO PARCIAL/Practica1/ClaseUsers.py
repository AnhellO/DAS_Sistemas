
class Usuarios:

    def __init__(self, id, name, username, email, address,addressgeo, phone, website, company):
        self._id = id
        self._name = name
        self._username = username
        self._email = email
        self._address = address
        self._addressgeo = addressgeo
        self._phone = phone
        self._website = website
        self._company = company

    def __str__(self):
	    return '''id: {}\nName: {}\nUsername: {}\nEmail: {}\nAddress: {}\nAddresGeo: {}\nPhone: {}\nWebsite: {}\nCompany: {}'''.format(self._id, self._name, self._username, self._email, self._address, self._addressgeo, self._phone, self._website, self._company).strip()



