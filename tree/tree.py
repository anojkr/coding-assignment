class Node:

	def __init__(self, data):

		self.data 	= data
		self.left 	= None
		self.right 	= None
		self.parent	= None


class Binary_Search_Tree:
	r = []
	def __init__(self, data):
		self.data 	= data
		self.left 	= None
		self.right 	= None

	def insert_node(self, root, *newdata):
		for data in newdata:
			node = root
			if node.data >=data:
				if node.left != None:
					self.insert_node(node.left, data)
				else:
					t = Node(data)
					node.left = t
					t.parent = node
			else:
				if node.right != None:
					self.insert_node(node.right, data)
				else:
					t = Node(data)
					node.right = t
					t.parent = node

	def search_node(self, root, data):
		node = root
		if node == None or node.data == data:
			return node
		elif node.data > data:
				return self.search_node(node.left,  data)
		elif node.data < data:
				return self.search_node(node.right, data)

	def inorder_min(self, root):
		node = root
		if node.right!=None:
			node = node.right
			while node.left !=None:
				node = node.left
			return node
		elif node.left!=None:
			node = node.left
			while node.left !=None:
				node = node.left
			return node
		else:
			pass


	def delete_node(self, root, data):
		node = self.search_node(root, data)
		if node.left == None and node.right==None:
			if node.parent.data>=node.data:
				node.parent.left 	=	None
			else: 
				node.parent.right 	=	None
			return node

		else:
			t = self.inorder_min(node)
			s = self.delete_node(t, t.data)
			if node.parent.data>=node.data:
				node.parent.left 	= s
				s.left = node.left
				s.right = node.right
			else:
				node.parent.right 	= s
				s.left = node.left
				s.right = node.right

	def inorder_traversal(self, root, r):
		node = root
		if node!=None:
			self.inorder_traversal(node.left, r)
			r.append(node.data)
			self.inorder_traversal(node.right, r)
		return r

	def preorder_treversal(self, root, r):
		node = root
		if node!=None:
			r.append(node.data)
			self.preorder_treversal(node.left, r)
			self.preorder_treversal(node.right, r)
		return r

	def postorder_traversal(self, root, r):
		node = root
		if node!=None:
			self.postorder_traversal(node.left, r)
			self.postorder_traversal(node.right, r)
			r.append(node.data)
		return r

	def traversal(self, type, root):
		r= []
		if type == 'inorder':
			return self.inorder_traversal(root,	r)
		elif type == 'postorder':
			return self.postorder_traversal(root, r)
		elif type == 'preorder':
			return self.preorder_treversal(root, r)

b = Binary_Search_Tree(50)
b.insert_node(b,30,70,20,40,60,80,15,25,35,45,55,65,75,85)
print(b.traversal('inorder', b))
print(b.traversal('preorder', b))
print(b.traversal('postorder', b))

b.delete_node(b,30)
print("\n")
print(b.traversal('inorder', b))
print(b.traversal('preorder', b))
print(b.traversal('postorder', b))


b.delete_node(b,40)
print("\n")
print(b.traversal('inorder', b))
print(b.traversal('preorder', b))
print(b.traversal('postorder', b))

