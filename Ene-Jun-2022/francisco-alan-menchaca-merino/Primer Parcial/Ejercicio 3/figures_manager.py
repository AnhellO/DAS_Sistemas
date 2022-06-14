class PolygonFactory:
    def __init__(self, figure_creator):
        self._figure_creator = figure_creator

    def getPolygon(self):
        return self._figure_creator.createFigure()
