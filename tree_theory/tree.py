class Node:

    def __init__(self, data):
        self.data   = data
        self.left   = None
        self.right  = None
        self.parent = None


class Binary_Search_Tree:

    def __init__(self, data):
        self.data   = data
        self.left   = None
        self.right  = None
        self.parent = None

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
        if node is None:
            print("Element not exist")
            return node

        elif node.parent is not None:
            #Delete of leaf node
            if node.left == None and node.right == None:
                if node.parent.data >= node.data:
                    node.parent.left = None
                else:
                    node.parent.right = None

            #Delete of node having two child
            elif node.left!= None and node.right!=None:
                t = self.inorder_min(node)
                self.delete_node(t, t.data)
                if node.parent.data >= node.data:
                    node.parent.left = t
                    t.left = node.left
                    t.right = node.right
                else:
                    node.parent.right = t
                    t.left = node.left
                    t.right = node.right

            #Delete node having one child
            else:
                t = self.inorder_min(node)
                print(t.data)
                if node.left is None and node.parent.data<=node.data:
                    node.parent.right = t
                elif node.right is None and node.parent.data>=node.data:
                    node.parent.left = t

        #Delete root node
        else:
            t = self.inorder_min(node)
            s = self.delete_node(t, t.data)
            t.left = node.left
            t.right = node.right
            t.parent  = None
            root = t
        return root


#b = Binary_Search_Tree(50)
#b.insert_node(b,30,70,20,40,60,80,15,25,35,45,55,65,75,85)

b = Binary_Search_Tree(5)
b.insert_node(b,1,10,20,30,40,50,60,70)

import tree_traversal, tree_operations
print("\nInorder Traversal    = {}\n".format(tree_traversal.traversal('inorder', b)))
print("\nPreorder Traversal   = {}\n".format(tree_traversal.traversal('preorder', b)))
print("\nPostorder Traversal  = {}\n".format(tree_traversal.traversal('postorder', b)))

#c = b.delete_node(b, 50)
c=b.delete_node(b, 5)

print("\nInorder Traversal    = {}\n".format(tree_traversal.traversal('inorder', c)))
print("\nPreorder Traversal   = {}\n".format(tree_traversal.traversal('preorder', c)))
print("\nPostorder Traversal  = {}\n".format(tree_traversal.traversal('postorder', c)))


print("\nNo. of Leaves in BST       = {}\n".format(tree_operations.no_of_leaves_bst(c)))
print("\nNo. of Full node in BST    = {}\n".format(tree_operations.no_of_fullnode(c)))
print("\nMaximum Height of BST      = {}\n".format(tree_operations.height_of_tree(c)))
