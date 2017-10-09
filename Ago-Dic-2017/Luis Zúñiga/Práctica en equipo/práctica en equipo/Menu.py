from bs4 import BeautifulSoup
import requests
import feedparser


import sys
import shlex
import os
from prueba_orm import *

class Option():

     def option(self):
        print('''
        STACK SCRAPER.
        Versión 0.0
        Alumnos:
                Omar Abasta.
                Iván Carreón.
                Enrique Castillo.
                Clemente Zúñiga.

        'Para salir escriba `salir` o `exit`'
        Por el momento sólo cuenta con una función:
        url `link-de-la-pregunta` para realizar el proceso de scraping y
        guardado en la base de datos.
        Bugs conocidos: truena si se intenta registrar un mismo usuario en la
        base de datos :(
        ''')

class Main:

    def main():
        print('#'*80)
        o = Option()
        o.option()
        while True:
            try:
                #recibe los argumentos
                cmd, *args = shlex.split(input('Scraper>>'))


                #Comandos técnicos
                if cmd=='exit' or cmd=='salir':
                    break

                elif cmd=='cls' or cmd=='clear':
                    os.system('cls')

                elif cmd=='pwd':
                    os.system('echo %cd%')


                elif cmd == 'url':
                    try:
                        set = SetAll(args[0])
                        set.set_all()
                        o.option()
                    except Exception as inst:
                        print(inst)



                    except Exception as inst:
                        print(inst)
                else:
                    print('Comando desconocido: {}'.format(cmd))

            except:
                a = 0



    if __name__ == "__main__":
        main()
