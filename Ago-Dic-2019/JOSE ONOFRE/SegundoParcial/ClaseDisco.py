
class Disc:

    def __init__(self,id,name,country,date,status):
        self._id = id
        self._artista = name
        self._pais = country
        self._fecha = date
        self._estado = status
        

    def __str__(self):
	    return '''id: {}\nartista: {}\npais: {} \nfecha: {} \nestado: {}'''.format(self._id, self._artista, self._pais, self._fecha, self._estado).strip()