import unittest
from Singleton import SoyUnico

def test_instance():
    My_Instancia1 = SoyUnico()
    My_Instancia1.strvalue = 'Instancia 1'
    str1 = str(My_Instancia1)

    My_Instancia2 = SoyUnico()
    My_Instancia2.strvalue = 'Instancia 2'
    str2 = str(My_Instancia2)

    print(str1)
    print(str2)

    assert str1 == str2, "Test fallido por que las ubicaciones de memoria son diferentes"


