class CharacterConcreteComponent:
    def __init__(self, name):
        self.name = name
        self.obj_name = ""
    
    def _equipment(func):
        def name(self):
            return f"{self.name} equipment:" + func(self)
        return name
    
    @_equipment
    def equip(self):
        return " Empty"

    _equipment = staticmethod(_equipment)

class ArmorConcreteDecorator:
    def __init__(self, obj):
        self.obj = obj
        self.name = obj.name
        self.obj_name = "\nArmor: Yes"
    
    @CharacterConcreteComponent._equipment
    def equip(self):
        return self.obj.obj_name+"\nArmor: Yes"

class SwordConcreteDecorator:
    def __init__(self, obj):
        self.obj = obj
        self.name = obj.name
        self.obj_name =  "\nSword: Yes"

    @CharacterConcreteComponent._equipment
    def equip(self):
        return self.obj.obj_name+"\nSword: Yes"