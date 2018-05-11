import heapq

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def huffman_code(Q):
    re = dict()
    root = 0
    while len(Q) is not 1:
        heapq.heapify(Q)
        r_1 = heapq.heappop(data)
        r_2 = heapq.heappop(data)
        if r_1 in re and r_2 not in re:
            h_1 = re[r_1]
            h_2 = Node(r_2)
        elif r_1 not in re and r_2 in re:
            h_1 = Node(r_1)
            h_2 = re[r_2]
        elif r_1 not in re and r_2 not in re:
            h_1 = Node(r_1)
            h_2 = Node(r_2)
        else:
            h_1 = re[r_1]
            h_2 = re[r_2]
        total = (h_1.data[0] + h_2.data[0], h_1.data[1] + h_2.data[1])
        data.append((total))
        s = Node(total, h_1, h_2)
        re[total] = s
        root = s
        print(data)
    print("\n")
    print_result(root,r="")

def print_result(root, r):
    if root.left is None and root.right is None:
    	print("{} : {}".format(root.data[0], r))
    	return
    print_result(root.left, r+"0")
    print_result(root.right, r+"1")


data = [(13, 'd'), (16, 'e'), (45, 'f'), (5, 'a'), (9, 'b'), (12, 'c')]
huffman_code(data)
