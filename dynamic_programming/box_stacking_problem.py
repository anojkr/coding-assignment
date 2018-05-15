#For Reference - https://people.cs.clemson.edu/~bcdean/dp_practice/dp_5.swf

def generate_all_dimensions(arr):
	r = []
	for x in arr:
		h1 = x[0]
		d1 = min(x[1],x[2])
		w1 = max(x[1],x[2])
		r.append([d1*w1,h1,d1,w1])

		h2 = x[1]
		d2 = min(x[0],x[2])
		w2 = max(x[0],x[2])
		r.append([d2*w2,h2,d2,w2])

		h3 = x[2]
		d3 = min(x[0],x[1])
		w3 = max(x[0],x[1])
		r.append([d3*w3,h3,d3,w3])

	r.sort(reverse=True)
	[k.pop(0) for k in r]
	return r
	
def can_stack(r, box1, box2):
	return r[box1][1]<r[box2][1] and r[box1][2]<r[box2][2]

def box_stacking_problem(arr):
	r  = generate_all_dimensions(arr)
	d = []

	R = [idx for idx in range(len(r))]
	[d.append(t[0]) for t in r]

	for i in range(1, len(r)):
		m = []
		for k in range(i):
			if can_stack(r,i,k):
				stack_height = d[k] + r[i][0]
				if stack_height > d[i]:
					d[i] = stack_height
					R[i] = k
	
	max_height = max(d)
	start_index = d.index(max_height)
	print("\nThe maximum height by building stack of boxes is {}\n". format(max(d)))


l = [[4, 6, 7], [1, 2, 3], [4, 5, 6], [10, 12, 32]]  
box_stacking_problem(l)