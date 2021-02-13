from autobus import autobus
from vehiculo import vehiculo


def main():
    flotilla = [
        vehiculo(260, 180, 5),
        autobus(150, 200, 50),
        vehiculo(2800, 100, 10),
        autobus(300, 800, 100)
    ]

    for i in flotilla:

        if isinstance(i, autobus):
            print(f'Soy un Autobus muy gelipe con: {i}\n'
                  f'Con una tarifa de {i.tarifaAutobus()}')


if __name__ == '__main__':
    main()
