"""
Fibonaci Number using Bottom-up Dynamic programming approach
"""
def fibonacci_num(num):
	table = {}
	for k in range(1, num+1):
		if k<=2:
			f=1
		else:
			f = table[k-1] + table[k-2]
		table[k] = f
	print(table[k])
	return table[k]

fibonacci_num(100)