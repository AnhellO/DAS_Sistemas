from abc import ABCMeta,abstractmethod

#*componente se declara la interfaz
#*tanto para el componente concreto como para baseDecorator
class SteveComponent(metaclass=ABCMeta):
    @abstractmethod
    def add_item(self) -> str:
        pass

#*Concret Component define el comportamiento-
#*basico de los decoradores pueden alterar
class SteveConcretComponent(SteveComponent):

    def add_item(self) -> str:
        return str(self)

    def __str__(self) -> str:
        return "Steve Basico"


#*refencia al objeto envuelto . delega las operaciones
class SteveBaseDecorator(SteveComponent, metaclass=ABCMeta):
    steve = SteveComponent

    def __init__(self, steve:SteveComponent) -> None:
        self.steve = steve

    @abstractmethod
    def add_item(self) -> str:
        return self.steve.add_item()

#*decoradores concretos definen la funcionalidad adicional de los componentes
class CascoConcreteDecorator(SteveBaseDecorator):
      def add_item(self) -> str:
        #return f"{super().add_item().replace()}"
        return f"{self.steve.add_item()} con casco"

class EspadaConcreteDecorator(SteveBaseDecorator):
      def add_item(self) -> str:
        return f"{self.steve.add_item()} con espada"



if __name__ == "__main__":

    enemigo = SteveConcretComponent()
    enemigo_casco = CascoConcreteDecorator(enemigo)
    print(enemigo_casco.add_item())


    enemigo_casco_espada = EspadaConcreteDecorator(enemigo_casco)
    danio = enemigo_casco_espada.add_item()
    enemigo_casco_espada = EspadaConcreteDecorator(enemigo_casco)
    print("steve danio",danio)


    enemigo2 = SteveConcretComponent()
    danio2 = enemigo2.add_item()
    print("steve basics",danio2)


    enemigo = SteveConcretComponent()
    enemigo_casco = CascoConcreteDecorator(enemigo)
    enemigo_casco_espada = EspadaConcreteDecorator(enemigo_casco)
    danio = enemigo_casco_espada.add_item()