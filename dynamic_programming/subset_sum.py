def subset_sum(s, sum):
	c = sum + 1
	r = len(s)+1
	
	table = [[int(0) for x in range(c)] for y in range(r)]
	for b in range(r):
		for sumz in range(c):
			if sumz==0:
				table[b][sumz] = True
			elif sumz != 0 and b == 0:
				table[b][sumz] = False
			elif sumz<s[b-1]:
				table[b][sumz] = table[b-1][sumz]
			elif sumz>=s[b-1]:
				table[b][sumz] = table[b-1][sumz-b] or table[b-1][sumz-s[b-1]]
	[print(k) for k in table]

#a = [3, 34, 4, 12, 5, 2]
a = [1, 2, 3]
subset_sum(a,6)