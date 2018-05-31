from Electrodomestico import Refrigerador
from Electrodomestico import Lavadora
from Electrodomestico import Television

class Factory(object):
    """Se implementa un factory para crear electrodomésticos"""
   

    def __init__(self):
        pass


    def electrodomestico(self, electrodomestico, *args):
        if electrodomestico == 1:
            return Refrigerador(*args)
        elif electrodomestico ==2:
            return Lavadora(*args)
        elif electrodomestico == 3:
            return Television(*args)
        else:
            return None



