def Decorator():
    def super_user(cls):#parametro hace referencia:a  la clse anidada
        #define una nueva cclase  esta clase extiende las funcionalidades de la clase base
        class SuperUser(cls):
            def equip(self):
                return f'{self.equip_2()}'
            def __str__(self):
               return f'{self.equip()}'
        return SuperUser

    return super_user

@Decorator()
class CharacterConcreteComponent:
    def __init__(self, name):
      self.name = name
    
    def get_name(self):
        return self.name
    
    def equip_2(self):
        return f'{self.get_name()} equipment: Empty'



@Decorator()
class ArmorConcreteDecorator:
    def __init__(self, name):
        self.name = name
    
    def get_name(self):
        return self.name

    def equip_2(self):
        message = f'{self.get_name()}'   
        return f"{message.replace(' Empty', '')}\nArmor: Yes"

@Decorator()
class SwordConcreteDecorator:
    def __init__(self, name):
        self.name = name
    
    def get_name(self):
        return self.name

    def equip_2(self):
        message = f'{self.get_name()}'   
        return f"{message.replace(' Empty', '')}\nSword: Yes"


 
@Decorator()
class ShieldConcreteDecorator:
    def __init__(self, name):
        self.name = name
    
    def get_name(self):
        return self.name

    def equip_2(self):
        message = f'{self.get_name()}'   
        return f"{message.replace(' Empty', '')}\nShield: Yes"
        

@Decorator()
class PowerUpsConcreteDecorator:
    def __init__(self, name):
        self.name = name
    
    def get_name(self):
        return self.name

    def equip_2(self):
        message = f'{self.get_name()}'   
        return f"{message.replace(' Empty', '')}\nPower-ups: Yes"


if __name__ == "__main__":
    concrete_component = CharacterConcreteComponent('Luxor')
    #print(concrete_component.equip())
    concrete_decorator_a = ArmorConcreteDecorator(concrete_component)
    #print(concrete_decorator_a.equip())
    concrete_decorator_b = SwordConcreteDecorator(concrete_decorator_a)
    #print(concrete_decorator_b.equip())
    concrete_decorator_c = ShieldConcreteDecorator(concrete_decorator_b)
    concrete_decorator_d =PowerUpsConcreteDecorator(concrete_decorator_c)
    concrete_decorator_d.equip()
    #print(concrete_decorator_d.equip())

