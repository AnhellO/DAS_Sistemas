class SoyUnico(object):

    __instance = None
    strvalue = None

    def __str__(self):
        return hex(id(self))

    def __new__(cls):
        if SoyUnico.__instance is None:
            SoyUnico.__instance = object.__new__(cls)
        return SoyUnico.__instance


def main():

    instancia1_ = SoyUnico()
    instancia1_.strvalue = "Movimiento 1"
    print(instancia1_)
    instancia2_ = SoyUnico()
    instancia2_.strvalue = "Movimiento 2"
    print(instancia2_)
    print(instancia1_)
    print(instancia2_)

if __name__ == "__main__":
    main()