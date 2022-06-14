class Animal:
    def _init_(self, name: str, sound: str):
        self.name = name
        self.sound = sound

    def get_name(self) -> str:
        return self.name

    def get_sound(self) -> str:
        return self.sound

class method:
    def main():
        animals = [Animal('Fish','glu'), Animal('cat','Miau'), Animal('Rooster', 'kikiriki'), Animal('Bee', 'ststststt')]
        for animal in animals:
            print(f"animal: {animal.get_name()}, sonido: {animal.get_sound()}")

if __name__ == "_main_":
    method().main()