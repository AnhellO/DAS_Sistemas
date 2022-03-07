import abc

# Componente
class ArchivoComponent(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def imprimeEstructura(self):
        pass

    # Nombre del archivo
    def get_nombre(self):
        return self.nombre

    # Directorio o archivo
    def get_tipo(self):
        return self.tipo