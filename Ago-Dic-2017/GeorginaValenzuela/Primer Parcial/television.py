class Television(Electrodomestico)

    def __init__(self, modelo, marca, color, numSerie, voltaje):
        super().__init__(modelo, marca, color, numSerie, voltaje)
        self.pulgadas = pulgadas
        
#Metodo getter y setter de pulgadas
    def get_pulgadas(self):
        return self.pulgadas

    def set_pulgadas(self):
        self.pulgadas = pulgadas

#Metodo para conectarse a internet solo manda un mensaje
    def conectarse_internet
        print ("Estas conectado a internet"):
