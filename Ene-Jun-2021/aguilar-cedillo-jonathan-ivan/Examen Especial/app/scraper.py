import xml.etree.ElementTree as ET
from mongo import mongo
import time
with open('person.xml', 'rt') as f:
    tree = ET.parse(f)
    root = tree.getroot()
    personas=[]
    for elem in root:
        # print(elem.tag)
        persona={}
        for subelem in elem:
            persona[subelem.tag]=subelem.text
            # print(persona)
        personas.append(persona)
    cliente=mongo()
    mdb = cliente.mydb
    people = mdb["people"]
    for persona in personas:
        inserted=0
        while(inserted!=1):
            try:
                people.insert(persona)
                inserted=1
            except:
                time.sleep(3)
                print('Timeout, reconnecting...')
                inserted=0
    cliente.close()