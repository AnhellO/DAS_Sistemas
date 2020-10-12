# import the required modules 
from abc import ABCMeta, abstractmethod 
import copy 
  
# class 
class Courses_At_GFG(metaclass = ABCMeta): 
      
    #constructor  
    def __init__(self): 
        self.id = None
        self.type = None
  
    @abstractmethod
    def course(self): 
        pass
  
    def get_type(self): 
        return self.type
  
    def get_id(self): 
        return self.id
  
    def set_id(self, sid): 
        self.id = sid 
  
    def clone(self): 
        return copy.copy(self) 
  
# class - DSA course 
class DSA(Courses_At_GFG): 
    def __init__(self): 
        super().__init__() 
        self.type = "Data Structures and Algorithms"
  
    def course(self): 
        print("Inside DSA::course() method") 
  
# class - SDE Course 
class SDE(Courses_At_GFG): 
    def __init__(self): 
        super().__init__() 
        self.type = "Software Development Engineer"
  
    def course(self): 
        print("Inside SDE::course() method.") 
  
# class - STL Course 
class STL(Courses_At_GFG): 
    def __init__(self): 
        super().__init__() 
        self.type = "Standard Template Library"
  
    def course(self): 
        print("Inside STL::course() method.") 

class DYAS(Courses_At_GFG): 
    def __init__(self): 
        super().__init__() 
        self.type = "Diseño Y Arquitectura de Software"
  
    def course(self): 
        return("DYAS es un curso prrón!")
  
# class - Courses At GeeksforGeeks Cache 
class Courses_At_GFG_Cache: 
      
    #Cache to store useful information 
    cache = {} 
  
    @staticmethod
    def get_course(sid): 
        COURSE = Courses_At_GFG_Cache.cache.get(sid, None) 
        return COURSE.clone() 
  
    @staticmethod
    def load(): 
        sde = SDE() 
        sde.set_id("1") 
        Courses_At_GFG_Cache.cache[sde.get_id()] = sde 
  
        dsa = DSA() 
        dsa.set_id("2") 
        Courses_At_GFG_Cache.cache[dsa.get_id()] = dsa 
  
        stl = STL() 
        stl.set_id("3") 
        Courses_At_GFG_Cache.cache[stl.get_id()] = stl 

        dyas = DYAS() 
        dyas.set_id("4") 
        Courses_At_GFG_Cache.cache[dyas.get_id()] = dyas
        
  
if __name__ == '__main__': 
    
    Courses_At_GFG_Cache.load() 
  
    sde = Courses_At_GFG_Cache.get_course("1") 
    print(sde.get_type()) 
  
    dsa = Courses_At_GFG_Cache.get_course("2") 
    print(dsa.get_type()) 
  
    stl = Courses_At_GFG_Cache.get_course("3") 
    print(stl.get_type()) 

    dyas = Courses_At_GFG_Cache.get_course("4") 
    print(dyas.get_type()) 
    
    STL.course(stl)
    DYAS.course(dyas)
    print(stl.get_id())