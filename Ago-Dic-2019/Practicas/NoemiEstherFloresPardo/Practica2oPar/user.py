class User(object):
    def __init__(self, **args):
        self.id = args.get('id')
        self.name = args.get('name')
        self.username = args.get('username')
        self.email = args.get('email')
        self.street = args.get('street')
        self.suite = args.get('suite')
        self.city = args.get('city')
        self.zipcode = args.get('zipcode')
        self.lat = args.get('lat')
        self.lng = args.get('lng')
        self.phone = args.get('phone')
        self.website = args.get('website')
        self.company = args.get('company')
        self.nameC = args.get('nameC')
        self.catchPhrase = args.get('catchPhrase')
        self.bs = args.get('bs')

    def set_id(self, id):
        self.id = id
    def set_name(self, name):
        self.name = name
    def set_username(self, username):
        self.username = username
    def set_email(self, email):
        self.email = email
    def set_street(self, street):
        self.street = street
    def set_suite(self, suite):
        self.suite = suite
    def set_city(self, city):
        self.city = city
    def set_zipcode(self, zipcode):
        self.zipcode = zipcode
    def set_lat(self, lat):
        self.lat = lat
    def set_lng(self, lng):
        self.lng = lng
    def set_phone(self, phone):
        self.phone = phone
    def set_website(self, website):
        self.website = website
    def set_company(self, company):
        self.company = company
    def set_nameC(self, nameC):
        self.nameC = nameC
    def set_catchPhrase(self, catchPhrase):
        self.catchPhrase = catchPhrase
    def set_bs(self, bs):
        self.bs = bs

    def get_id(self):
        return self.id
    def get_name(self):
        return self.name
    def get_username(self):
        return self.username
    def get_email(self):
        return self.email
    def get_street(self):
        return self.street
    def get_suite(self):
        return self.suite
    def get_city(self):
        return self.city
    def get_zipcode(self):
        return self.zipcode
    def get_lat(self):
        return self.lat
    def get_lng(self):
        return self.lng
    def get_phone(self):
        return self.phone
    def get_website(self):
        return self.website
    def get_company(self):
        return self.company
    def get_nameC(self):
        return self.nameC
    def get_catchPhrase(self):
        return self.catchPhrase
    def get_bs(self):
        return self.bs

    def __str__(self):
        return """
        Id: {}\nName: {}\nUserName: {}\nEmail: {}\nStreet: {}\nSuite: {}\nCity: {}\nZipCode: {}\nGeo: {}\nLat: {}\nLng:
        {}\nPhone: {}\nWebSite: {}\nCompany: {}\nName: {}\nCatchPharse: {}\nBs: {}\n
        """.format(self.name, self.username, self.email, self.street, self.suite, self.city, self.zipcode, self.lat,
                            self.lng, self.phone, self.website, self.company, self.nameC, self.catchPhrase, self.bs)