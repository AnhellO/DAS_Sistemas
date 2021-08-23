class Armor:
    def __init__(self, func):
        self.func = func

    def __call__(self):
        return self.func() + " with armor"

class Sword:
    def __init__(self, func):
        self.func = func

    def __call__(self):
        return self.func() + " with sword"

class Shield:
    def __init__(self, func):
        self.func = func

    def __call__(self):
        return self.func() + " with shield"

class Flamethrower:
    def __init__(self, func):
        self.func = func

    def __call__(self):
        return self.func() + " with flamethrower"

class ArmorSword:
    def __init__(self, func):
        self.func = func

    def __call__(self):
        return self.func() + " with armor and sword"


class Human:
    def __str__(self):
        return "Selected human"