

class disk():

    name=None
    artist=None
    country=None


    def __init__(self,na,ar,co):
        self.name=na
        self.artist=ar
        self.country=co

    def __str__(self):
        return "[{},{},{}]".format(self.name,self.artist,self.country)
