from Factory import Factory
class Main():
       
    def main():
        fabrica = Factory()
        guitarra = fabrica.Instrument_music(1,'rojo','10,000','4/4','regular slinky','Stratocaster','1.750 Kg')
        guitarra.imprime_especificaciones()
     
        bateria = fabrica.Instrument_music(2,'Blanco','10,000','14x5','4','2','75kg')
        bateria.datos_bateria()
         
    if __name__ == "__main__":
        main()
        
