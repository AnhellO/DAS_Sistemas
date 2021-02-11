from abc import ABC, abstractclassmethod
import requests

class ComplexCars(object): 
  
    """Separar clases para carros complejos"""
  
    def __init__(self): 
  
        pass
  
    def cars(self, car_name): 
  
        return "Patron Complejo[% s]" % (car_name) 

  
  
class CarFamilies(object): 
  
    """creamos un diccionario para almacenar el tipo de carro"""
  
    car_family = {} 
  
    def __new__(cls, name, car_family_id): 
        try: 
            id = cls.car_family[car_family_id] 
        except KeyError: 
            id = object.__new__(cls) 
            cls.car_family[car_family_id] = id
        return id
  
    def set_car_info(self, car_info): 
  
        """configurar informacion del carro"""
  
        cg = ComplexCars() 
        self.car_info = cg.cars(car_info) 
  
    def get_car_info(self): 
  
        """retorna la informacion del carro"""
  
        return (self.car_info) 
  
  
  
if __name__ == '__main__': 
    car_data = (('a', 1, 'Audi'), ('a', 2, 'Ferrari'), ('b', 1, 'Audi')) 
    car_family_objects = [] 
    for i in car_data: 
        obj = CarFamilies(i[0], i[1]) 
        obj.set_car_info(i[2]) 
        car_family_objects.append(obj) 
  
    """identificaciones similares dicen que son los mismos objetos """
  
    for i in car_family_objects: 
        print("id = " + str(id(i))) 
        print(i.get_car_info()) 
              