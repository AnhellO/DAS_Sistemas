from ClassCalculator import Calculator

class Main:
    
    def get_input(self,message):
        return input(message)
    
    def menu(self):
        t = True
        while t:
            m = "---Menu---\n"
            m += "Escribe la abreviación adecuada\n"
            m += "Suma: x mas y\nResta: x menos y\nMultiplicacion: x por y\nDivision: x entre y\n"
            m += "Potencia: x elevado_a y\nRaiz: x raiz_de y\nPara salir escriba 'salir'\n\n"
            inpt = self.get_input(m)
            if inpt == 'Exit':
                print("\nHasta pronto.")
                t= False
            else:
                data = inpt.split(' ')
                print("Resultado = "+ str(self.Calc(int(data[0]),data[1],int(data[2]))))
                t = True

    def Calc(self,a, oper, b):
        X=Calculator(a,b)
        switch={
            'mas':X.suma,
            'menos':X.resta,
            'por':X.multi,
            'entre':X.divi,
            'elevado_a':X.pote,
            'raiz_de':X.raiz
            }
        return switch.get(oper)()

Cycle = Main()
print(Cycle.menu())