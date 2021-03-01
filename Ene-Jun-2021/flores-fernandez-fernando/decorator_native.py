def CharacterArmorDecorator(function):
    def wrapper(name):
        return f"{function(name)} Armor: Yes"
    return wrapper
        
@CharacterArmorDecorator
def CharacterConcreteComponent(name):
    
    def equip():
        return f"{name} equipment: Empty"
    
    return equip  
  
def main():
    character = CharacterConcreteComponent("Luxor")
   
    print(character())
    
if __name__ == '__main__':
    main()    


        
    
    
    
    
