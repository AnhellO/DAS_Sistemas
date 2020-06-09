import requests
from peewee import *

data = requests.get('https://breakingbadapi.com/api/characters').json()

myDB = MySQLDatabase(
    'breaking',
    host='breaking_db',
    port=3306,
    user='root',
    passwd='root'
)

class characters(Model):
    id = IntegerField()
    name = CharField()
    birthday = CharField()
    img = CharField()
    estado = CharField()
    nickname = CharField()
    portrayed = CharField()

    class Meta:
        database = myDB
        db_table: 'characters'

def populate():
    for chars in data:
        id = chars['char_id']
        name = chars['name']
        birthday = chars['birthday']
        img = chars['img']
        status = chars['status']
        nickname = chars['nickname']
        portrayed = chars['portrayed']
        characters.insert(id=id,
                          name=name,
                          birthday=birthday,
                          img=img,
                          estado=status,
                          nickname=nickname,
                          portrayed=portrayed,
                         )
if __name__ == '__main__':
    populate()