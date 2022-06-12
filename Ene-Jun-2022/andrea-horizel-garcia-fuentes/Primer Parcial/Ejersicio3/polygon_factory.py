class PolygonFactory:
    def __init__(self, creator):
        self.creator = creator

    def getPolygon(self):
        return self.creator.createFigure()
