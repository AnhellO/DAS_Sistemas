class personaje():
    def __init__(self, id='', name='', status='', species='', tipe='', gender='', OriginName='', OriginUrl='', LocationName='',LocationUrl='',image='', episode='',
                 url='', created=''):
        self._id = id
        self._name = name
        self._status = status
        self._species = species
        self._tipe = tipe
        self._gender = gender
        self._OriginName=OriginName
        self._OriginUrl=OriginUrl
        self._LocationName= LocationName
        self.LocationUrl=LocationUrl
        self._image=image
        self._episode=episode
        self._url=url
        self._created=created


    def __str__(self):
        return 'id: {}\nName: {}\nstatus: {}\nspecie: {}\ntipe: {}\ngender: {}\nname origin: {}\nurl Origin: {}\n name location: {}\nurl Location: {}\nimage: {}\nepisode: {}\nurl: {}\ncreated: {} '\
            .format(self._id,
                    self._name,
                    self._status,
                    self._species,
                    self._type,
                    self._gender,
                    self._OriginName,
                    self._OriginUrl,
                    self._LocationName,
                    self._LocationUrl,
                    self._image,
                    self._episode,
                    self._url,
                    self._created)
