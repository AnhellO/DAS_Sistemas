class WebDevelopement: 
  
    def accept(self, visitor): 
        visitor.visit(self) 
  
    def development(self, visitor): 
        print(visitor, "development in ", self) 
  
  
    def __str__(self): 
        return self.__class__.__name__ 
  
  
class XML(WebDevelopement): pass
class JSON(WebDevelopement): pass
class YAML(WebDevelopement): pass
  
class Visitor: 
  
    def __str__(self): 
        return self.__class__.__name__ 
  
class pAGE(Visitor): 
    def visit(self, crop): 
        crop.development(self) 
  
  
xml = XML() 
json = JSON() 
yaml = YAML() 
  
Pages = pAGE() 
  
xml.accept(Pages)   
json.accept(Pages) 
yaml.accept(Pages) 