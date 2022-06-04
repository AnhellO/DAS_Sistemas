from xml.dom.minidom import Element
import xml.etree.ElementTree as ET
tree = ET.parse('sample.xml')
root = tree.getroot()
for i in range (0,len(root),1):
    if int(root[i][0].text) % 2 == 0:
        print (root[i][1].text)
print(" ")
for i in range (0,len(root),1):
    aux=root[i][4].text
    aux2=aux[len(aux)-4]+aux[len(aux)-3]+aux[len(aux)-2]+aux[len(aux)-1]
    if aux2== '.edu' or aux2== '.gov':
        print (root[i][1].text)

for ip_address in root.iter('ip_address'):
    ip_address.text='127.0.0.1'
    tree.write('updated.xml')