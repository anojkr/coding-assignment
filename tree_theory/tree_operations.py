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
    node = root
    if node == None:
        return 0

    elif node.left == None and node.right == None:
        return 0
    else:
        l = height_of_tree(node.left)
        r = height_of_tree(node.right)
        return max(l, r) + 1
