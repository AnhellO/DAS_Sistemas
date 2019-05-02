import operator
import codecs
d={}
f= codecs.open('SPECS.md','r','utf-8')
s = f.readlines()
for i in range(48,79):
    d[s[i].split(':')[0][2:5]] = [s[i].split(':')[1][2:(len(s[i].split(':')[1])-3)]]
d[s[79].split(':')[0][2:5]] = [s[79].split(':')[1][2:(len(s[79].split(':')[1])-2)]]
r=sorted(d.items(), key=operator.itemgetter(0))
r.reverse()
for i in r: print(i[0].upper(),'es el código ISO 3166-2 para el estado de',i[1][0].capitalize())
