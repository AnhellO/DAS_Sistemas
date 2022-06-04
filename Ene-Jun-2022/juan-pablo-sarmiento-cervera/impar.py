import json
with open('sample.json','r') as j:
    doc=json.load(j)
for i in range (0, len(doc['people']['person']),1):
    if int(doc['people']['person'][i]['id']) %2 != 0:
        print (doc['people']['person'][i]['first_name'])
print (" ")
for i in range (0, len(doc['people']['person']),1):
    if len(doc['people']['person'][i]['company']) == 4 or len(doc['people']['person'][i]['company']) == 6:
         print (doc['people']['person'][i]['first_name'])

for i in range (0, len(doc['people']['person']),1):
    doc['people']['person'][i]['phone_number']='XX-XX-XXX'


with open('updated.json','w') as j:
    json.dump(doc,j)