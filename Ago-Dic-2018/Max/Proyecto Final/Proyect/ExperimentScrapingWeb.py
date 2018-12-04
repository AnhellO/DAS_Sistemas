from bs4 import BeautifulSoup
import requests
#Autor y programador - "Maximiliano García De Santiago"
def Scraping(): #Experimentacion de scrapeo receta
    url = 'http://taco-randomizer.herokuapp.com/'
    REQ = requests.get(url)

    BS = BeautifulSoup(REQ.text, 'html.parser') #Navegando por la arquitectura html de etiquetas
    div_principal = BS.find_all('div',{'class':'row'}) #Box row

    name_taco = BS.find('h1')
    div_contribuidores = BS.find_all('h6',{'class':'light'})
    Sub_receta_1 = div_principal[1].find('div',{'class':'recipe'})
    Sub_receta_2 = div_principal[2].find('div',{'class':'recipe'})
    Sub_receta_3 = div_principal[3].find('div',{'class':'recipe'})
    Sub_receta_4 = div_principal[4].find('div',{'class':'recipe'})

#    print(div_principal)
#    print(name_taco)
#    print(str(div_contribuidores))
#    print('---------------------Esta es la Sub-Receta 1------------------------' + str(Sub_receta_1))
#    print('---------------------Esta es la Sub-Receta 2------------------------' + str(Sub_receta_2))
#    print('---------------------Esta es la Sub-Receta 3------------------------' + str(Sub_receta_3))
#    print('---------------------Esta es la Sub-Receta 4------------------------' + str(Sub_receta_3))

def ApiClient(): #experimentacion de request user
    url = 'https://randomuser.me/api/'
    reques = requests.get(url)
    if(reques.status_code == 200):
        DatosUser = reques.json()
#    print(DatosUser)
    results = DatosUser['results']
#    print(results)
    for i in results:
        gender = i['gender'] #Dato a usar
        Name = i['name']
        Email = i['email'] # Dato a usar
        Dob = i['dob']
#        print(Name)
    First = Name['first'] #Dato a usar
    Last = Name['last'] #Dato a usar
    Age = Dob['age'] #Dato a usar
#    print(First)
#    print(Last)
#    print(Email)
#    print(Age)


#Scraping()
#ApiClient()
