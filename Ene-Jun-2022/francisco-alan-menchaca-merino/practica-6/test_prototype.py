from prototype import Prototype, Oveja


class TestPrototype:
    def test_object_attributes(self):
        dolly = Oveja('Dolly', 'Dorper')

        assert dolly.get_nombre() == "Dolly"
        assert dolly.get_tipo() == "Dorper"

    def test_instantiation(self):
        derek = Oveja('Derek', 'Suffolk')

        assert isinstance(derek, Prototype)
        assert isinstance(derek, Oveja)

    def test_clone_function(self):
        pedro = Oveja('Pedro', 'Ouessant')
        pedro_clone = pedro.clone()

        assert pedro.__str__() == pedro_clone.__str__()
        assert isinstance(pedro, Prototype)
        assert isinstance(pedro, Oveja)

    def test_clone_attributes(self):
        pedro = Oveja('Pedro', 'Quessant')
        pedro_clone = pedro.clone()

        assert pedro_clone.get_nombre() == "Pedro"
        assert pedro_clone.get_tipo() == "Quessant"
