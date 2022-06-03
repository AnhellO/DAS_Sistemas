import yaml
from yaml import Loader
yaml_file = open('sample.yaml', 'r')
data= yaml.load(yaml_file, Loader=Loader)
for i in range (0, len(data['people']['person']),1):
    if int(data['people']['person'][i]['id']) %3 == 0:
        print(data['people']['person'][i]['first_name'])
print (" ")
for i in range (0, len(data['people']['person']),1):
    if len(data['people']['person'][i]['first_name']) == 5 and len(data['people']['person'][i]['last_name']) == 5:
        print(data['people']['person'][i]['first_name'])

for i in range (0, len(data['people']['person']),1):
    data['people']['person'][i]['email']='---'
with open('updated.yaml', 'w') as j:
 yaml.dump(data,j)
