#Matrix-chain-multiplication {Reference cormen book- Dynamic programming}

def matrix_chain_mul(matrix_order):
	#alist.insert(0,'dummy')
	n = len(matrix_order)
	table = [[ int(1) for x in range(n)] for y in range(n)]
	s = [[ int(0) for x in range(n)] for y in range(n)]

	for i in range(1, n):
		table[i][i] = 0
	
	for l in range(2, n):
		for i in range(1, n-l+1):
			j= i+l-1
			r = []
			for k in range(i,j):
				#print("{}-{}".format(i,j))
				#print("{}-{}-{}".format(i-1,k,j))
				q = table[i][k] + table[k+1][j] + matrix_order[i-1]*matrix_order[k]*matrix_order[j]
				#print("{}--{}--{}*{}*{}\n".format(table[i][k], table[k+1][j],matrix_order[i-1],matrix_order[k],matrix_order[j] ))
				r.append(q)
				table[i][j] = min(r)
	
	[print(table[k]) for k in range(1,n-1)]
	print("\nMinimum cost for multiplication of matrix - {}\n" .format(table[1][n-1]))
	return table[1][n-1]


a = [30,35,15,5,10,20,25]
matrix_chain_mul(a)