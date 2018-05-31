
while True:
	caso = int(input())
	if caso == 0:
		break
		
	n = int(input())
	m = int(input())
	i = 0
	
	for i in i < caso:
		x = int(input())
		y = int(input())

		if x == n or y == m:
			print("divisa")
		elif x > n and y > m:
			print("NE")
		elif x < n and y > m:
			print("NO")
		elif x < n and y < m:
			print("SO")
		else:
			print("SE")

if caso != 0:
	break

