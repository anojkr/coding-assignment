def inorder_traversal(root, r):
    node = root
    if node != None:
        inorder_traversal(node.left, r)
        r.append(node.data)
        inorder_traversal(node.right, r)
    return r


def preorder_treversal(root, r):
    node = root
    if node != None:
        r.append(node.data)
        preorder_treversal(node.left, r)
        preorder_treversal(node.right, r)
    return r


def postorder_traversal(root, r):
    node = root
    if node != None:
        postorder_traversal(node.left, r)
        postorder_traversal(node.right, r)
        r.append(node.data)
    return r


def traversal(type, root):
    r = []
    if type == 'inorder':
        return inorder_traversal(root, r)
    elif type == 'postorder':
        return postorder_traversal(root, r)
    elif type == 'preorder':
        return preorder_treversal(root, r)
