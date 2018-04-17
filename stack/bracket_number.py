#https://practice.geeksforgeeks.org/problems/print-bracket-number/0

T = int(input())

for _ in range(T):
		N = input().split()
		#print(N)
		stack = []
		l = []
		c = 0
		for i in N:
			if i == '(':
				c +=1
				stack.append(c)
				l.append(c)
			elif i == ')':
				l.append(stack.pop())
		str1 = ' '.join(str(e) for e in l)
		print(str1)
