
class Episodio:

    def __init__(self,id,name,airdate,episode,characters,url,created):
        self._id = id
        self._nameEp = name
        self._airdateEp = airdate
        self._episodeEp = episode
        self._charactersEp = characters
        self._urlEp = url
        self._createdEp = created

    def __str__(self):
	    return '''id: {}\nName: {}\nAirDate: {}\nEpisode: {}\nCharacters: {}\nUrl: {}\nCreated: {}'''.format(self._id, self._nameEp, self._airdateEp, self._episodeEp, self._charactersEp, self._urlEp, self._createdEp).strip()
