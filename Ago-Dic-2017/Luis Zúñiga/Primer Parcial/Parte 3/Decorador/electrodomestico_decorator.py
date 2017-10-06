from Electrodomestico import Refrigerador
from Electrodomestico import Lavadora
from Electrodomestico import Television
from DecoradorElectrodomestico import DecoradorElectrodomestico
class Main():
       
    def main():
        television = Television('blanco','4,000','tv0111','17-04-11','México','PHILLIPS',True,True)
        telerobot = DecoradorElectrodomestico(television)
        telerobot.imprimeAtributos()
       
    if __name__ == "__main__":
        main()
        
