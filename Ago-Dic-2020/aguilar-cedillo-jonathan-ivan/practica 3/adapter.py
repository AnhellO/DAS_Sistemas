class Target:
    """
    Target define la interfaz específica del dominio utilizada por el código de cliente.
    """

    def request(self) -> str:
        return "Objetivo: comportamiento del objetivo predeterminado"


class Adaptee:
    """
    El Adaptee contiene algunos comportamientos útiles, pero su interfaz es incompatible
    con el código de cliente existente. El Adaptee necesita alguna adaptación antes de
    el código del cliente puede usarlo.
    """

    def specific_request(self) -> str:
        return ".odatpada led laicepse otneimatropmoC"


class Adapter(Target, Adaptee):
    """
    El adaptador hace que la interfaz del Adaptee sea compatible con la del Target.
    interfaz a través de herencia múltiple.
    """

    def request(self) -> str:
        return f"Adapter: (TRANSLATED) {self.specific_request()[::-1]}"


def client_code(target: "Target") -> None:
    """
    El código de cliente admite todas las clases que siguen la interfaz de Target.
    """

    print(target.request(), end="")
    return target.request()


if __name__ == "__main__":
    print("Cliente: puedo trabajar bien con los objetos de destino.")
    target = Target()
    client_code(target)
    print("\n")

    adaptee = Adaptee()
    print("Cliente: la clase Adaptador tiene una interfaz extraña."
          "Mira, no lo entiendo:")
    print(f"Adaptee: {adaptee.specific_request()}", end="\n\n")

    print("Cliente: Pero puedo trabajar con él a través del Adaptador:")
    adapter = Adapter()
    client_code(adapter)