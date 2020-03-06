import abc

# Componente
class ArchivoComponent(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def imprimeEstructura(self):
        pass

    def get_nombre(self):
        return self.nombre # Nombre del archivo

    def get_tipo(self):
        return self.tipo # Directorio o archivo