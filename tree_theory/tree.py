class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None


class Binary_Search_Tree:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert_node(self, root, *newdata):
        for data in newdata:
            node = root
            if node.data >= data:
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
            return self.search_node(node.left, data)
        elif node.data < data:
            return self.search_node(node.right, data)

    def inorder_min(self, root):
        node = root
        if node.right != None:
            node = node.right
            while node.left != None:
                node = node.left
            return node
        elif node.left != None:
            node = node.left
            while node.left != None:
                node = node.left
            return node
        else:
            pass

    def delete_node(self, root, data):
        node = self.search_node(root, data)
        if node == None:
            print("Element not exist")
        elif node.left == None and node.right == None:
            if node.parent.data >= node.data:
                node.parent.left = None
            else:
                node.parent.right = None
            return node

        else:
            t = self.inorder_min(node)
            s = self.delete_node(t, t.data)
            if node.parent.data >= node.data:
                node.parent.left = s
                s.left = node.left
                s.right = node.right
            else:
                node.parent.right = s
                s.left = node.left
                s.right = node.right


b = Binary_Search_Tree(50)
b.insert_node(b,30,70,20,40,60,80,15,25,35,45,55,65,75,85)

import tree_traversal, tree_operations
print("\nInorder Traversal    = {}\n".format(tree_traversal.traversal('inorder', b)))
print("\nPreorder Traversal   = {}\n".format(tree_traversal.traversal('preorder', b)))
print("\nPostorder Traversal  = {}\n".format(tree_traversal.traversal('postorder', b)))

#b.delete_node(b, 20)

print("\nNo. of Leaves in BST       = {}\n".format(tree_operations.no_of_leaves_bst(b)))
print("\nNo. of Full node in BST    = {}\n".format(tree_operations.no_of_fullnode(b)))
print("\nMaximum Height of BST      = {}\n".format(tree_operations.height_of_tree(b)))
