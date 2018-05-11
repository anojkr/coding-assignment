def no_of_leaves_bst(root):
    node = root
    if node == None:
        return 0
    elif node.left == None and node.right == None:
        return 1
    else:
        return no_of_leaves_bst(node.left) + no_of_leaves_bst(node.right)

def no_of_fullnode(root):
    node = root
    if node == None:
        return 0
    elif node.left != None and node.right != None:
        return 1 + no_of_fullnode(node.left) + no_of_fullnode(node.right)
    else:
        return 0

def height_of_tree(root):
    #Height of leaf node is consider 1 here
    node = root
    if node == None:
        return 0
    else:
        l = height_of_tree(node.left)
        r = height_of_tree(node.right)
        #print("Height of node {} = {}".format(node.data, max(l,r)+1))
        return max(l, r)+1

def balance_factor_of_node(root):
    node = root
    if node is None:
        return 0
    l = height_of_tree(node.left)
    r = height_of_tree(node.right)
    print("\nBalance Factor of Node {} = {}\n".format(node.data,l-r))
    return l-r

def balance_factor_of_tree(root):
    node = root
    if node is not None:
        lr  = balance_factor_of_tree(node.left)
        l   = height_of_tree(node.left)
        rr  = balance_factor_of_tree(node.right)
        r   = height_of_tree(node.right)
        print("\nBalance Factor of Tree {} = {}\n".format(node.data,l-r))

def is_leaf(node):
    #Height of leaf node is consider 1 here
    if height_of_tree(node) is 1:
        print("Leaf Node")