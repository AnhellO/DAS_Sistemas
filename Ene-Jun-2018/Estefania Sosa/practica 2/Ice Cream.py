class Restaurant():
    def __init__(self,_name,cuisine_type):
        self._name=_name
        self.cuisine_type=cuisine_type

    def describe_restaurant(self):
        print(self._name.title() + " este es el nombre"+",")
        print(self.cuisine_type.title() + " su especialidad")

    def open_restaurant(self):
        print(self._name.title() + " ABIERTO")
        
class IceCreamStand(Restaurant):
    def __init__(self,_name,cuisine_type="IceCream"):
        super().__init__(_name,cuisine_type)
        self.flavors=[]

    def flavorsTip(self):
        for x in self.flavors:
            print(x)

ic =IceCreamStand("sultana","gelato")
ic.flavors=["a","b","c"]
ic.flavorsTip()
r = Restaurant("la comidilla","mexicana")
r.open_restaurant()
r.describe_restaurant()
