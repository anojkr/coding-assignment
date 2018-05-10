import tree, tree_operations, tree_traversal

class AVL(tree.Binary_Search_Tree):
		def __init__(self,data):
			tree.Binary_Search_Tree.__init__(self, data )
			self.balance_factor = 0

		def right_rotation(self, root):
			pass

		def insertion_node(self, root, *data):
			



x = AVL(10)
x.insert_node(x,20,30,40,50,60,70)
print(tree_operations.height_of_tree(x))
#tree_operations.balance_factor_of_node(x)
#print(tree_traversal.traversal('inorder', x))
tree_operations.balance_factor_of_tree(x)



		
