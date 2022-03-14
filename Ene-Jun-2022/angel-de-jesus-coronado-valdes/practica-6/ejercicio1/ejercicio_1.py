from abc import ABC, abstractmethod

class Component(ABC):
    
    @abstractmethod
    def showDetails(self,fold):
        pass
    

class Leaf(Component):
  
    def __init__(self, *arr):  
        self.pos = arr[0]
  
    def showDetails(self,fold):
        #print("\t", end ="")
        #print(self.pos)
        return self.pos


class Composite(Component):
  
    def __init__(self, *arr):
        self.pos = arr[0]
        self.children = []

  
    def add(self, child):
        self.children.append(child)
        return "added successfully"
  
    def remove(self, child):
        self.children.remove(child)
        for i in self.children:
            if i != child:
                return "successfully erased"
        
  
    def showDetails(self,fold):
        
        if self.pos == "home/":
            print(self.pos)
            
            
        if self.pos == fold:
            print("     ",fold)
        
        
        for child in self.children:
            #print("\t", end ="")
            p = child.showDetails(fold)
            if p != None:
                if self.pos == fold:
                    print("         -",p)
            
            

if __name__ == "__main__":
    
    tree = Composite("home/") #creamos el arbol por default
    
    
    branch1 = Composite("picture/")
    branch2 = Composite("music/")
    leaf = Leaf("prueba.txt")
    
    leaf11 = Leaf("photo.png")
    leaf12 = Leaf("photo2.png")
    leaf13 = Leaf("photo3.png")
    
    leaf33 = Leaf("mydog.mp4")
    leaf22 = Leaf("En El Río - Arcadia Libre (Video Oficial).mp3")
    
    b2 = branch2.add(leaf33)
    print(b2)
    b2 = branch2.add(leaf22)
    print(b2)
    
    b3 = branch1.add(leaf11)
    print(b3)
    b3 = branch1.add(leaf12)
    print(b3)
    b3 = branch1.add(leaf13)
    print(b3)
    
    t1 = tree.add(branch1)
    t1 = tree.add(branch2)
    print(t1)
    tree.showDetails("picture/")
    tree.showDetails("music/")
    print("\n****************borrado****************")
    b2 = branch2.remove(leaf33)
    b3 = branch1.remove(leaf12)
    print(b2)
    print(b3+"\n")
    tree.showDetails("picture/")
    tree.showDetails("music/")
    
    
    
        
