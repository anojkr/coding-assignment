#Infix to postfix expression
# https://practice.geeksforgeeks.org/problems/infix-to-postfix/0
import re

T = int(input())
opr = {
	'^'	:	3,
	'/'	:	2,
	'*'	:	2,
	'+'	: 	1,
	'-'	:	1,
	'(' :	0,
	')'	:	0,
	'?' : 	0
}

stack = ['?']
postfix= []

for _ in range(T):
	N = input().split()
	for token in N:
		if token not in opr:
			postfix.append(token)
		elif  token == '(':
			stack.append(token)
		elif token == ')':
			x = stack.pop()
			while x != '(':
				postfix.append(x)
				x = stack.pop()
		else:
			while opr[stack[-1]]>= opr[token]:
				postfix.append(stack.pop())
			stack.append(token)

	while len(stack)>0:
		postfix.append(stack.pop())


str1 = ' '.join(str(e) for e in postfix)
print(str1)
