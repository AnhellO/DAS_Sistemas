
class Locacion:

    def __init__(self,id,name,ttype,dimension,residents,url,created):
        self._id = id
        self._nameLoc = name
        self._typeLoc = ttype
        self._dimensionLoc = dimension
        self._residentsLoc = residents
        self._urlLoc = url
        self._createdLoc = created

    def __str__(self):
	    return '''id: {}\nName: {}\nType: {}\nDimension: {}\nResidents: {}\nUrl: {}\nCreated: {}'''.format(self._id, self._nameLoc, self._typeLoc, self._dimensionLoc, self._residentsLoc, self._urlLoc, self._createdLoc).strip()
