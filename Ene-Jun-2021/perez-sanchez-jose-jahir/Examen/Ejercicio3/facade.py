#La clase Lavadora que se diria que tiene la complejidad real del problema, obviamente aqui por simplicidad solo te regresa lo que esta haciendo
class Lavadora():
    def lavado(self):
        return "Lavando..."

    def enjuagado(self):
        return "Enjuagando..."

    def centrifugado(self):
        return "Centrifugando..."
#La LavadoraFacade que no te muestra que hace Lavadora y solo te da el resultado, al menos asi le entiendo yo a facade
class LavadoraFacade():
    def ciclo_completo(self):
        return f"{Lavadora().lavado()}\n{Lavadora().enjuagado()}\n{Lavadora().centrifugado()}\nFinalizado!\n"
    def solo_lavado(self):
        return f"{Lavadora().lavado()}\nFinalizado!\n"
    def solo_enjuagado(self):
        return f"{Lavadora().enjuagado()}\nFinalizado!\n"
    def solo_centrifugado(self):
        return f"{Lavadora().centrifugado()}\nFinalizado!\n"
#Pruebas del codigo
def main():
    print(LavadoraFacade().ciclo_completo())
    print(LavadoraFacade().solo_centrifugado())


if __name__ == "__main__":
    main()