class Calculator:
    def __init__(self, a: int, b: int) -> None:
        self.a = a
        self.b = b

    def suma(self) -> int:
        return self.a + self.b
    
    def resta(self) -> int:
        return self.a - self.b