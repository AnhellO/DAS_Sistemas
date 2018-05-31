from Motocicleta import Motocicleta
from Automovil import Automovil
from Camion import Camion
from Agencia import Agencia

agencia = Agencia
"""
agencia.venta(agencia,1,3,'der')
agencia.venta(agencia,1,2,'sssdae')
agencia.venta(agencia,4,3,'slsldks')
agencia.venta(agencia,2,3,'dasdasks')
agencia.venta(agencia,3,5,'adasdees')
agencia.imprimeVentas(agencia)
"""
motocicleta = Motocicleta('Italika','2010','amarillo','gasolina','automática',\
    '100',20,20000)
print (motocicleta.datosDeMoto())
auto = Automovil('Corsa', '2004', 'verde', 'gasolina', 'standard', '5', 'si',\
    '20', 20, 50000)
print(auto.datosDeAuto())
auto.reduceExistencias()
print(auto.datosDeAuto())
"""
camion = Camion('torton', '2010', 'blanco', 'diesel', 'standard', '6', '200', '12', 3, 100000)
agencia.altaCamion(agencia,camion)
#print(camion.devuelveSku())
camioncito = agencia.searchCamion(agencia,'tor2010diestablanco')
print(camioncito.datosDeCamion())
#agencia.bajaCamion(agencia,camioncito)
camioncito.reduceExistencias()
print('\n\n\n')
print(camioncito.datosDeCamion())
agencia.bajaCamion(agencia,camioncito)
print(camioncito.datosDeCamion())

"""
#print(camion.datosDeCamion())

