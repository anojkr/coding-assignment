import heapq

I = [int(x) for x in input().split()]
N,T = I[0],I[1]
l = [int(x) for x in input().split()]


for _ in range(T):
		Q = int(input())
		ma = l[:]
		mi = [int(-x) for x in l]
		heapq.heapify(ma)
		heapq.heapify(mi)

		while Q>0:
			min_num = heapq.pop(ma)
			max_num = -heapq.pop(mi)
			dif = max_num - min_num
			heapq.push(ma, dif)
			heapq.push(mi, -dif)
			





		