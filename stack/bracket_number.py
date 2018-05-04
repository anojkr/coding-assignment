#https://practice.geeksforgeeks.org/problems/print-bracket-number/0

T = int(input())
for _ in range(T):
		N = input().strip()
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

"""
Example:
Input:
3​
( a + ( b * c ) ) + ( d / e )​
( ( ( ) ) ( ( ) ) )
( ( ( ( ( )
Output:
1 2 2 1 3 3
1 2 3 3 2 4 5 5 4 1
1 2 3 4 5 5

Explanation:
Test case 1:The highlighted brackets in the given expression (a+(b*c))+(d/e) has been assigned the numbers as: 1 2 2 1 3 3.
"""