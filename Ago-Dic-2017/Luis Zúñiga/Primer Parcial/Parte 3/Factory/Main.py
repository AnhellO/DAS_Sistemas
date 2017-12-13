from Factory import Factory
class Main():
       
    def main():
        fabrica = Factory()
        refri = fabrica.electrodomestico(1,'rojo','10,000','ref009','28-04-2017','México','GE','10',False,0)
        refri.imprime_especificaciones()
     
        lavadora = fabrica.electrodomestico(2,'Blanco','10,000','lvk9090','09-05-09','México','Whirlpool',8,10)
        lavadora.datos_lavadora()
         
        tv = fabrica.electrodomestico(3,'negro','10,000','tv0012','08-06-13','México','SAMSUNG',True,True)
        tv.imprimeAtributos()
        print(tv.datos_tv())

    if __name__ == "__main__":
        main()
        
