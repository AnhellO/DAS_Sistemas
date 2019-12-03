
class Artista:

    def __init__(self,id,name,area,extscore,ilist,begin):
        self._id = id
        self._artista = name
        self._area = area
        self._score = extscore
        self._islist = ilist
        self._begin = begin

    def __str__(self):
	    return '''id: {}\nartista: {}\narea: {} \nscore \nilist: {} \nbegin: {}'''.format(self._id, self._artista, self._area, self._score, self._islist, self._begin).strip()


