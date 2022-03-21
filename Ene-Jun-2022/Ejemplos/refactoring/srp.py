# WRONG: No respeta el SRP
# class User:
#     def __init__(self, name: str, age: int) -> None:
#         self.name = name
#         self.age = age
    
#     def __str__(self) -> str:
#         return f"Name: {self.name} - Age: {self.age}"
    
#     def serialize(self, format: str) -> str:
#         return f"We have serialized to {format} format: {self}"
    
# GOOD: Respeta el SRP pero viola el OCP
# class User:
#     def __init__(self, name: str, age: int) -> None:
#         self.name = name
#         self.age = age
    
#     def __str__(self) -> str:
#         return f"Name: {self.name} - Age: {self.age}"

# class Serializer:
#     def __init__(self, user: User) -> None:
#         self.user = user
    
#     def serialize(self, format: str) -> str:
#         if format == 'json':
#             return self.__serialize_json()
        
#         if format == 'xml':
#             return self.__serialize_xml()
        
#         if format == 'yaml':
#             return self.__serialize_yaml()

#     def __serialize_json(self) -> str:
#         return f"We have serialized to JSON format: {self.user}"

#     def __serialize_xml(self) -> str:
#         return f"We have serialized to XML format: {self.user}"

#     def __serialize_yaml(self) -> str:
#         return f"We have serialized to YAML format: {self.user}"

import abc

# VERY GOOD: Respeta y mejora el SRP, y respeta el OCP
class User:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
    
    def __str__(self) -> str:
        return f"User -> Name: {self.name} - Age: {self.age}"

class Address:
    def __init__(self, street: str, number: str, city: str) -> None:
        self.street = street
        self.number = number
        self.city = city
    
    def __str__(self) -> str:
        return f"Address -> Street: {self.street} - Number: {self.number} - City: {self.city}"

class Serializer(metaclass=abc.ABCMeta):
    def __init__(self, obj) -> None:
        self.obj = obj
    
    @abc.abstractmethod
    def serialize(self) -> str:
        pass

class JsonSerializer(Serializer):
    def serialize(self) -> str:
        return f"We have serialized to JSON format: {self.obj}"

class XmlSerializer(Serializer):
    def serialize(self) -> str:
        return f"We have serialized to XML format: {self.obj}"

class YamlSerializer(Serializer):
    def serialize(self) -> str:
        return f"We have serialized to YAML format: {self.obj}"

def main():
    u = User('Random', 25)
    a = Address('Perez Treviño', 8, 'Salti-York')
    serializer = JsonSerializer(u)
    print(serializer.serialize())
    serializer.obj = a
    print(serializer.serialize())

if __name__ == '__main__':
    main()