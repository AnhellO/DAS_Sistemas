class Cup:
    color = ""

    # This is the factory method
    @staticmethod
    def getCup(cupColor):
        if (cupColor == "red"):
            return RedCup()
        elif (cupColor == "blue"):
            return BlueCup()
        else:
            return None

class RedCup(Cup):
    color = "red"

class BlueCup(Cup):
    color = "blue"

# A little testing
redCup = Cup.getCup("red")
print (redCup.color, redCup.__class__.__name__)

blueCup = Cup.getCup("blue")
print(blueCup.color, blueCup.__class__.__name__)
