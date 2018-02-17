resultado=""
K=int(input())
if K>0 and K<=1000:
	while K!=0:
		N,M=list(map(int,input().split()))
		if N<=-10000 or M>=10000:
			break
		else:
			for X in range(K):
				X,Y=list(map(int,input().split()))
				if X<-10000 or Y>10000:
					break
				else:
					if X<N and Y>M:
						resultado+="NO"
					elif X>N and Y>M:
						resultado+="NE"
					elif X>N and Y<M:
						resultado+="SE"
					elif X<N and Y<M:
						resultado+="SO"
					elif X==N or Y==M:
						resultado+="DIVISA"
				K=int(input())
print(resultado)	