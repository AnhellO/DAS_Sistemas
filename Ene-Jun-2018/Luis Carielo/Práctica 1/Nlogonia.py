resultado=""
K=int(input())
if K>0 and K<=1000:
	while K!=0:
		N,M=list(map(int, input().split()))
		if N>-10000 or M<10000:
			for x in range(K):
				X,Y=list(map(int, input().split()))
				if X>=-10000 or Y<=10000:
					if X<N and Y>M:
						resultado += "NO\n"
					elif X>N and Y>M:
						resultado += "NE\n"
					elif X>N and Y<M:
						resultado += "SE\n"
					elif X<N and Y<M:
						resultado += "SO\n"
					elif X==N or Y==M:
						resultado += "divisa\n"
		K=int(input())

print(resultado)