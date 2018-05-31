queries = int(input())
i = 1
cont=1
while queries > 0 and i <= queries:

	print('\n')
	trees = []
	Lprom = []
	specie = input()
	trees.append(specie)
	while len(specie) <= 30 and len(trees) <= 1000000 and specie != '':

		specie = input()
		if specie != '':
			trees.append(specie)


		sortedtrees = sorted(trees)

	for s in sortedtrees:
		x = cont/len(sortedtrees)*100
		x1 = "%.4f" %x
		Lprom.append(x1)

	for s, l in zip(sortedtrees, Lprom):
		print (s, l)
	i+=1

	#hi
