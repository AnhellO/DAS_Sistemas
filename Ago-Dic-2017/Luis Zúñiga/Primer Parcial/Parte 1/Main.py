from Refrigerador import Refrigerador
from Television import Television
from Lavadora import Lavadora
import sys
class Main():
       
    def main():
        lista_refris = []
        ref = Refrigerador('rojo','10,000','ref009','28-04-2017','México','GE','10',False,0)
        lista_refris.append(ref)
        ref = Refrigerador('Blanco','8,000','ref1010','10-08-16','México','IEM','7',False,0)
        lista_refris.append(ref)
        ref = Refrigerador('Negro','7,000','re222','01-01-11','México','HI','9',True,0)
        lista_refris.append(ref)

        for i in lista_refris:
            i.imprime_especificaciones()
        
        #ref.menu_temperatura()
        #print('Nueva tempreratura: {} grados'.format(ref.get_temperatura()))

        lista_tv = []
        tv = Television('negro','10,000','tv0012','08-06-13','México','SAMSUNG',True,True)
        lista_tv.append(tv)
        tv = Television('blanco','4,000','tv0111','17-04-11','México','PHILLIPS',True,True)
        lista_tv.append(tv)
        tv = Television('gris','2,000','tvSSSS','3-02-12','México','AVIO',True,True)
        lista_tv.append(tv)
        
        for i in lista_tv:
            i.imprimeAtributos()
            print(i.datos_tv())
        lista_lavadoras = []
        lavadora = Lavadora('Blanco','10,000','lvk9090','09-05-09','México','Whirlpool',8,10)
        lista_lavadoras.append(lavadora)
        lavadora = Lavadora('blanco','7100','lvv001','01-02-12','México','Zenith',10,7)
        lista_lavadoras.append(lavadora)
        lavadora = Lavadora('blanco','7100','lvv001','30-07-13','México','Elías',18,11)
        lista_lavadoras.append(lavadora)
        for i in lista_lavadoras:
           i.datos_lavadora()      
       
    if __name__ == "__main__":
        main()
        