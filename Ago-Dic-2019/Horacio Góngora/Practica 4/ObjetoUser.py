class User(object):
    def __init__(self, **args):
        self._id = args.get('id')
        self._name = args.get('name')
        self._username = args.get('username')
        self._email = args.get('email')
        self._street = args.get('street')
        self._suite = args.get('suite')
        self._city = args.get('city')
        self._zipcode = args.get('zipcode')
        self._lat = args.get('lat')
        self._lng = args.get('lng')
        self._phone = args.get('phone')
        self._website = args.get('website')
        self._company = args.get('company')
        self._nameC = args.get('nameC')
        self._catchPhrase = args.get('catchPhrase')
        self._bs = args.get('bs')

    def __str__(self):
        return f'''Id ->{self._id}\nName -> {self._name}\nUserName -> {self._username}\nEmail -> {self._email}\nAdrees:\n\tStreet -> {self._street}\n\tSuite -> {self._suite}\n\tCity -> {self._city}\n\tZipCode -> {self._zipcode}\nGeo:\n\tLat -> {self._lat}\n\tLng -> {self._lng}\nPhone -> {self._phone}\nWebSite -> {self._website}\nCompany:\n\tName -> {self._nameC}\n\tCatchPhrase -> {self._catchPhrase}\n\tBs -> {self._bs}'''