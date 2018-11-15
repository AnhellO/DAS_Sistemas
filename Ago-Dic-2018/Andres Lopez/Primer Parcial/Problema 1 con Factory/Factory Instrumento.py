from Instrument_music import Guitarra
from Instrument_music import Bateria


class Factory(object):
    """Se implementa un factory para crear Instrument_music"""
   

    def __init__(self):
        pass


    def electrodomestico(self, Instrument_music, *args):
        if Instrument_music == 1:
            return Guitarra(*args)
        elif Instrument_music ==2:
            return Bateria(*args)
        else:
            return None
