def decorar(decoracion):
    def _decorar(func_name):
        def __decorar(*args, **kwargs):
            ret = func_name(*args, **kwargs)
            if decoracion is not None:
                ret += " decorada con %s en las paredes" % decoracion
            return ret
        return __decorate
    return _decorate 

@decorar("pintura")
def construccion_casa():
    return "Esta es una casa"
