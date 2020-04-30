import requests
import json

def getCivilizations():
    uri = f'https://age-of-empires-2-api.herokuapp.com/api/v1/civilizations'
    r = requests.get(uri)
    data=r.json()
    rvalue=[]
    for i in data["civilizations"]:
        num=i['id']
        name=i['name']
        army=i['army_type']
        expansion=i['expansion']
        dictionary={'num': num, 'name': name, 'army':army, 'expansion': expansion}
        rvalue.append(dictionary)
    return rvalue

def getCivilization(num):
    uri = f'https://age-of-empires-2-api.herokuapp.com/api/v1/civilization/{num}'
    r = requests.get(uri)
    data=r.json()
    num=data['id']
    name=data['name']
    army=data['army_type']
    expansion=data['expansion']
    rvalue={'num': num, 'name': name, 'army':army, 'expansion': expansion}
    return rvalue

def getUnits():
    uri = f'https://age-of-empires-2-api.herokuapp.com/api/v1/units'
    r=requests.get(uri)
    data=r.json()
    rvalue=[]
    for i in data['units']:
        num=i['id']
        name=i['name']
        age=i['age']
        try:
            cost_wood=i['cost']['Wood']
        except:
            cost_wood='FREE'
        try:    
            cost_gold=i['cost']['Gold']
        except:
            cost_gold='FREE'
        try:
            cost_food=i['cost']['Food']
        except:
            cost_food="FREE"
        try:
            cost_stone=i['cost']['Stone']
        except:
            cost_stone="FREE"
        hp=i['hit_points']
        try:    
            attack_range=i['range']
        except:
            attack_range="N/A"
        try:    
            attack=i['attack']
        except:
            attack='N/A'
        try:
            armor=i['armor']
        except:
            armor="N/A"
        try:
            accuracy=i['accuracy']
        except:
            accuracy="N/A"     
        dictionary={'num':num, 'name':name, 'age':age,'cost_wood':cost_wood,'cost_gold':cost_gold,'cost_food':cost_food,"cost_stone":cost_stone,'hp':hp, 'attack_range': attack_range, 'attack':attack,'armor': armor, 'accuracy':accuracy}
        rvalue.append(dictionary)
    return rvalue

def getUnit(num):
    uri = f'https://age-of-empires-2-api.herokuapp.com/api/v1/unit/{num}'
    r=requests.get(uri)
    data=r.json()
    
    num=data['id']
    name=data['name']
    age=data['age']
    try:
        cost_wood=data['cost']['Wood']
    except:
        cost_wood="FREE"
    try:
        cost_gold=data['cost']['Gold']
    except:
        cost_gold="FREE"
    try:
        cost_stone=data['cost']['Stone']
    except:
        cost_stone="FREE"
    try:
        cost_food=data['cost']['Food']
    except:
        cost_food="FREE"
    hp=data['hit_points']
    try:    
        attack_range=data['range']
    except:
        attack_range="N/A"
    try:    
        attack=data['attack']
    except:
        attack='N/A'
    try:
        armor=data['armor']
    except:
        armor="N/A"
    try:
        accuracy=data['accuracy']
    except:
        accuracy="N/A"

    rvalue={'num':num, 'name':name, 'age':age,'cost_wood':cost_wood,'cost_gold':cost_gold,'cost_food':cost_food,"cost_stone":cost_stone,'hp':hp, 'attack_range': attack_range, 'attack':attack,'armor': armor, 'accuracy':accuracy}
    return rvalue



if __name__=='__main__':
    print(":P")

    