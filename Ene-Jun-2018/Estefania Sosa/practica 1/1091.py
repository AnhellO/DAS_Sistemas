import sys
sys.stdin
k=1
while k>0 and k<=1000:
	k=int(input())
	N,M=list(map(int, input().split(' ')))
	if N>=-10000 or M<=10000:
		for x in range(k):
			X,Y=list(map(int, input().split(' ')))
			if X>=-10000 or Y<=10000:
				if X>N and Y>M:
					print("NE")
				elif X<N and Y>M:
					print("NO")
				elif X<N and Y<M:
					print("SO")
				elif X>N and Y<M:
					print("SE")
				elif X==N or Y==M:
					print("divisa")
