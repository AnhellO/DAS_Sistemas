colas = 1
salida = []
while colas > 0 and colas <= 1000:
	colas = int(input())
	if colas > 0 and colas <= 1000:
		N,M = input().split(' ')
		i=0
		while i < colas and int(N) > -10000 and int(N) < 10000 and int(M) > -10000 and int(M) < 10000:
			X,Y = input().split(' ')
			if int(X) >= -10000 and int(X) <= 10000 and int(Y) >= -10000 and int(Y) <= 10000:
				if int(X) > int(N) and int(Y) > int(M):
					salida.append('NE')
				elif int(X) > int(N) and int(Y) < int(M):
					salida.append('SE')
				elif int(X) < int(N) and int(Y) > int(M):
					salida.append('NO')
				elif int(X) < int(N) and int(Y) < int(M):
					salida.append('SO')
				else:
					salida.append('divisa')
			i+=1
	else:
		print('\n'.join(salida))
