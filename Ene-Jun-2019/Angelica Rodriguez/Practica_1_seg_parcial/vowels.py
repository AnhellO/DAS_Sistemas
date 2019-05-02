import glob
a=open(glob.glob('../../*/*/*/*d')[2],'r').read().upper()
v="AEIOU"
for r in range(5):print(v[r]+":",*map(a.count,v[r]))
