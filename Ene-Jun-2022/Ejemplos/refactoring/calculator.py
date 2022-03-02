class Calculator:
    def __init__(self, a: int = None, b: int = None) -> None:
        self.__a = a
        self.__b = b
    
    def set_a(self, a) -> None:
        self.__a = a
        
    def get_a(self) -> int:
        return self.__a
    
    def set_b(self, b) -> None:
        self.__b = b

    def get_b(self) -> int:
        return self.__b
    
    def sum(self) -> int:
        return self.__a + self.__b
    
    def substract(self) -> int:
        return self.__a - self.__b