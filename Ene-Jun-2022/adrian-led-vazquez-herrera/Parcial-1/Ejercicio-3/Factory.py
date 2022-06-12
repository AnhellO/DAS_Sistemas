#DAS 8vo semestre
#Parcial 1, E: 3 Factory Method
#Factory

from Interface_instances import *

class PolygonFactory:
    
    def create_polygon(shape):
        if shape=="Triangle":
            return Triangle()
        elif shape=="Square":
            return Square()
        elif shape=="Pentagon":
            return Pentagon()
        else:
            return "Polygon not found"
