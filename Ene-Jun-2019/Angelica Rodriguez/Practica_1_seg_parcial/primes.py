r=range(2,999)
[print(x)for x in r if sum(x%d==0 for d in r)<2]
