#Longest common subsequence problem
def lcs_problem(alist, blist, m, n):
	table = [[0] * (n+1)] * (m+1)
	print(table)
	for i in range(0, m+1):
		for j in range(0, n+1):
			if i is 0 or j is 0:
				table[i][j] = 0
			elif i>0 and j>0 and alist[i-1]==blist[j-1]:
				table[i][j] = 1+table[i-1][j-1]
			else:
				table[i][j] = max(table[i-1][j], table[i][j-1])
	[print(k) for k in table]
	print("\nLongest common subsequence = {}\n".format(table[m][n]))

a = list("XMJYAUZ")
b = list("MZJAWXU")
lcs_problem(a, b, len(a), len(b))


