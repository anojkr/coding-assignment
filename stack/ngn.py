#Next Greatest/Highest Number 

#Test cases
T = int(input())
for t in range(T):
	# No. of elements in array
	N = int(input())
	I = [int(x) for x in input().split()]
	arr = [ I.count(x) for x in I]	
	#print("Array - {}".format(I))
	#print(" Frequency - {}".format(arr))
	stack = []
	pos = []
	t = [ -1 for x in range(len(arr))]
	stack.append(arr[0])
	pos.append(0)
	for s in range(1, len(arr)):
		next = arr[s]
		if len(stack)!=0:
			elements = stack.pop()
			idx = pos.pop()
			while elements<next:
				t[idx] = I[s] 
				if len(stack) == 0:
					break
				elements = stack.pop()
				idx = pos.pop()

			if next<=elements:
					stack.append(elements)
					pos.append(idx)

		stack.append(next)
		pos.append(s)
	str1 = ' '.join(str(e) for e in t)
	print(str1)
