#For Reference - https://people.cs.clemson.edu/~bcdean/dp_practice/dp_5.swf

def generate_all_dimensions(arr):
	r = []
	for height, length, breadth  in arr:
		h1 = height
		d1 = min(length, breadth)
		w1 = max(length, breadth)
		r.append([d1*w1, h1, d1, w1])

		h2 = length
		d2 = min(height,breadth)
		w2 = max(height,breadth)
		r.append([d2*w2, h2, d2, w2])

		h3 = breadth
		d3 = min(height,length)
		w3 = max(height,length)
		r.append([d3*w3, h3, d3, w3])

	r.sort(reverse=True)
	[k.pop(0) for k in r]
	return r
	
def can_stack(r, box1, box2):
	return r[box1][1]<r[box2][1] and r[box1][2]<r[box2][2]

def box_stacking_problem(arr):
	r  = generate_all_dimensions(arr)
	d = []

	R = [idx for idx in range(len(r))]
	[d.append(height) for height, length, breadth in r]

	for box1 in range(1, len(r)):
		m = []
		for box2 in range(box1):
			if can_stack(r, box1, box2):
				height_box2 = d[box2]
				height_box1 = r[box1][0]
				stack_height = height_box2 + height_box1
				if stack_height > d[box1]:
					d[box1] = stack_height
					R[box1] = box2
	
	max_height = max(d)
	start_index = d.index(max_height)
	print("\nThe maximum height by building stack of boxes is {}\n". format(max(d)))


l = [[4, 6, 7], [1, 2, 3], [4, 5, 6], [10, 12, 32]]  
box_stacking_problem(l)