import json
import psycopg2
from peewee import *
from models import MyPerson

# class person():
   
#    def __init__(self, _id:str,_balance:str,_age:int,_name:str,_company:str,_email:str,_phone:str,_address:str,_about:str,_registered:str):
#       self.id = _id
#       self.balance = _balance
#       self.age = _age
#       self.name = _name
#       self.company = _company
#       self.phone = _phone
#       self.email = _email
#       self.address = _address
#       self.about = _about
#       self.registered = _registered
    

def get_data_from_file():
    with open('data.json') as json_file:
        data =  json.load(json_file)
        return data
    

def get_persons_from_file(data:list):
    list_p = []
    for x in data:
        _id = x.get('_id')
        _balance = x.get('balance')
        _age = int(x.get('age'))
        _name = x.get('name').get('first') + x.get('name').get('last')
        _company = x.get('company')
        _phone = x.get('phone')
        _email = x.get('email')
        _address = x.get('address')
        _about = x.get('about')
        _registered = x.get('registered')
        list_p.append(MyPerson(
            person_id = _id,
    balance = _balance,
    age = _age,
    name = _name,
    company = _company,
    phone = _phone,
    email = _email,
    address = _address,
    about = _about,
    registered = _registered))
    return list_p


def main():
    # query = 'insert into persons(person_id,balance,age,name,company,email,phone,address,about,registered) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    # conn = psycopg2.connect(host='localhost',dbname='Person_Database',user='foo',password='bar123')
    # curs = conn.cursor()
    data = get_data_from_file()
    inds = get_persons_from_file(data)
    # for ind in inds:
    #     curs.execute(query,(ind.id,ind.balance,ind.age,ind.name,ind.company,ind.email,ind.phone,ind.address,ind.about,ind.registered))
    #     print(f'{ind.name} ha sido registrado')
    # conn.commit()
    # conn.close()
    for ind in inds:
        ind.save()
        print(f'Se registro a {ind.name}')

if __name__ == "__main__":
    main()
    