import math
from abc import ABC,abstractmethod

#****************[ The Abstract Factory interface ]**************
#declares a set of methods that return
#different abstract products.
class Figures(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


#*******************[ Concrete Factories ]*********************
#produce a family of products that belong to a single
#variant.
class Retangle(Figures):
    def area(self):
        return TotalAreaRetangle() #product retangle

    def perimeter(self):
        return TotalPerimeterRetangle() #producto perimeter   

class Cycle(Figures):
    def area(self):
        return TotalAreaCycle() #product cycle

    def perimeter(self):
        return TotalPerimeterCycle() #producto cycle


#****************[ The Abstract Factory interface ]**************
#   Product area
class Area(ABC):
    @abstractmethod
    def FuctionArea(self):
        pass

""" Each distinct product of a product family should have a base interface. All
    variants of the product must implement this interface.
"""
class TotalAreaRetangle(Area):
    def FuctionArea(self,arr):
        return arr[0] * arr[1]

class TotalAreaCycle(Area):
    def FuctionArea(self,arr):
        return math.pi * arr[0] **2


#****************[ The Abstract Factory interface ]**************
#   Product perimeter
class Perimeter(ABC):
    @abstractmethod
    def FuctionPerimeter(self):
        pass

class TotalPerimeterRetangle(Perimeter):
    def FuctionPerimeter(self,arr):
        return 2 * (arr[0] * arr[1])

class TotalPerimeterCycle(Perimeter):
    def FuctionPerimeter(self,arr):
        return 2 * math.pi * arr[0]

#****************[ The client code ]**************
"""The client code works with factories and products only through abstract
   types: AbstractFactory and AbstractProduct.
"""
class Client:
    def ClientCode(self,abtractfactory,arr):
        area = abtractfactory.area()
        perimeter = abtractfactory.perimeter()

        print(area.FuctionArea(arr))
        print(perimeter.FuctionPerimeter(arr))
        print(arr)

if __name__ == "__main__":
    client = Client()
    print("======= [ Recatngle ] ========")
    client.ClientCode(Retangle(),[3,3])
    print("\n")
    print("======= [ cycle ] ========")
    client.ClientCode(Cycle(),[3])
