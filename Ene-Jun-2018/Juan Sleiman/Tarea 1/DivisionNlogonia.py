'''variables x, y , n , m
N y M seran para mover el punto de division, X e Y serán las coordenadas actuales.'''
queries = 1
output = []
while queries > 0 and queries <= 1000:
	queries = int(input())
	if queries > 0 and queries <= 1000:
		N,M = input().split(' ')
		i=0
		while i < queries and int(N) > -10000 and int(N) < 10000 and int(M) > -10000 and int(M) < 10000:
			X,Y = input().split(' ')
			if int(X) >= -10000 and int(X) <= 10000 and int(Y) >= -10000 and int(Y) <= 10000:
				if int(X) > int(N) and int(Y) > int(M):
					output.append('NE')
				elif int(X) > int(N) and int(Y) < int(M):
					output.append('SE')
				elif int(X) < int(N) and int(Y) > int(M):
					output.append('NO')
				elif int(X) < int(N) and int(Y) < int(M):
					output.append('SO')
				else:
					output.append('divisa')
			i+=1
	else:
		print('\n'.join(output))