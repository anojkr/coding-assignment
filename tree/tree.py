class Node:

	def __init__(self, data):

		self.data 	= data
		self.left 	= None
		self.right 	= None
		self.parent	= None


class Binary_Search_Tree:
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
					t.parent = node.data
			else:
				if node.right != None:
					self.insert_node(node.right, data)
				else:
					t = Node(data)
					node.right = t
					t.parent = node.data

	def search_node(self, root, data):
		node = root
		if node == None or node.data == data:
			return node
		elif node.data > data:
				return self.search_node(node.left,  data)
		elif node.data < data:
				return self.search_node(node.right, data)


	def inorder_traversal(self, root):
		node = root
		if node!=None:
			self.inorder_traversal(node.left)
			print(node.data)
			self.inorder_traversal(node.right)

	def preorder_treversal(self, root):
		node = root
		if node!=None:
			print(node.data)
			self.preorder_treversal(node.left)
			self.preorder_treversal(node.right)
	def postorder_traversal(self, root):
		node = root
		if node!=None:
			self.postorder_traversal(node.left)
			self.postorder_traversal(node.right)
			print(node.data)


b = Binary_Search_Tree(10)
b.insert_node(b,25,30,5,15,50,60,45)
#b.preorder_treversal(b)
b.inorder_traversal(b)
#b.postorder_traversal(b)
#b.delete_node(b,45)
#b.inorder_traversal(b)
print(b.search_node(b,45))
