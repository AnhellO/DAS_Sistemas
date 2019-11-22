

class artist():

    name=None
    date=None
    area=None
    type=None
    gender=None
    score=None

    def __init__(self,ar,da,na,ge,ty,sc):
        self.name=na
        self.date=da
        self.area=ar
        self.type=ty
        self.gender=ge
        self.score=sc

    def __str__(self):
        return "[{},{},{},{},{},{}]".format(self.area,self.date,self.name,self.gender,self.type,self.score)
