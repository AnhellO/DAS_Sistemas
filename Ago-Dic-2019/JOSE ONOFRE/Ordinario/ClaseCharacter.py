
class Personaje:

    def __init__(self,id,name,status,species,ttype,gender,originName,orginUrl,locationName,locationUrl,image,episode,url,created):
        self._id = id
        self._nameCh = name
        self._statusCh = status
        self._speciesCh = species
        self._typeCh = ttype
        self._genderCh = gender
        self._origin_nameCh = originName
        self._origin_urlCh = orginUrl
        self._location_NameCh = locationName
        self._location_UrlCh = locationUrl
        self._imageCh = image
        self._episodeCh = episode
        self._urlCh = url
        self._createdCh = created

    def __str__(self):
	    return '''id: {}\nName: {}\nStatus: {} \nSpecies: {}\nType: {}\nGender: {}\nOriginName: {}\nOriginUrl: {}\nLocationName: {}\nLocationUrl: {}\nImage: {}\nEpisode: {}\nUrl: {}\nCreate: {}'''.format(self._id, self._nameCh, self._statusCh, self._speciesCh, self._typeCh, self._genderCh, self._origin_nameCh, self._origin_urlCh, self._location_NameCh, self._location_UrlCh, self._imageCh, self._episodeCh, self._urlCh, self._createdCh)
