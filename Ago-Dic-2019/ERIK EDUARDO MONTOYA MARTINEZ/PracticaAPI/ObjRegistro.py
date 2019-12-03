class Registro(object):
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

        return 'id: {} ' \
               '\nname:{} ' \
               '\nusername: {} ' \
               '\nemail: {} ' \
               '\naddress: ' \
               '\n\tstreet: {} ' \
               '\n\tsuite: {} ' \
               '\n\tcity: {} ' \
               '\n\tzipcode: {} ' \
               '\nGeo: ' \
               '\n\tLAT: {} ' \
               '\n\tLng: {} ' \
               '\nPhone: {} ' \
               '\nWebsite: {} ' \
               '\nCompay: ' \
               '\n\tName: {} ' \
               '\n\tCatchPhrase: {} ' \
               '\n\tBs: {}'\
            .format(self._id,
                    self._name,
                    self._username,
                    self._email,
                    self._street,
                    self._suite,
                    self._city,
                    self._zipcode,
                    self._lat,
                    self._lng,
                    self._phone,
                    self._website,
                    self._nameC,
                    self._catchPhrase,
                    self._bs)