class Node():
    def __init__(self, value, str_name):
        self.key = value
        self.name = str_name
        self.left = None
        self.right = None


def bst_insert(root, value, str_name):
    """
    insert a key value in a tree
    :param root: BSTNode object that represents
        the root of the tree
    :param value: an integer representing the value to insert
    :param str_name: a string corresponding to
        the literal format of the value
    :return: a BSTNode object
    """
    if root is None:
        return Node(value, str_name)

    if value < root.key:
        root.left = bst_insert(root.left, value, str_name)
    else:
        root.right = bst_insert(root.right, value, str_name)

    return root

def bst_insert_iterative(root, value, str_name):
    """
    insert a key value in a tree
    :param root: BSTNode object that represents
        the root of the tree
    :param value: an integer representing the value to insert
    :param str_name: a string corresponding to
        the literal format of the value
    :return: a BSTNode object
    """
    
    newnode = Node(value, str_name)
 
    x = root
    y = None
 
    while (x != None):
        y = x
        if (value < x.key):
            x = x.left
        else:
            x = x.right
     
    if (y == None):
        y = newnode
 
    elif (value < y.key):
        y.left = newnode
 
    else:
        y.right = newnode
    return y


def bst_find(root, value):
    """
    print the found value in a literal format
    :param root: BSTNode object that represents
        the root of the tree
    :param value: an integer representing the value to find
    """
    if root is None:
        return

    if root.key == value:
        return root.name

    if root.key < value:
        return bst_find(root.right, value)

    return bst_find(root.left, value)

def bst_find_iterative(root, value):
    """
    print the found value in a literal format
    :param root: BSTNode object that represents
        the root of the tree
    :param value: an integer representing the value to find
    """
    x = root
    while x is not None:
        if x.key == value:
            return x.name
        if x.key < value:
            x = x.right
        else:
            x = x.left
    
    return


def show(root):
    """
    print the tree in a preorder visit
    :param root: BSTNode object that represent the root of the tree
    """
    if root:
        print str(root.key) + ":" + root.name, 
        show(root.left)
        show(root.right)
    else:
        print "NULL",


def inorder_visit(root):
    if root:
        inorder_visit(root.left)
        print(root.name)
        inorder_visit(root.right)


def preorder_visit(root):
    if root:
        print(root.name)
        preorder_visit(root.left)
        preorder_visit(root.right)


def postorder_visit(root):
    if root:
        postorder_visit(root.left)
        postorder_visit(root.right)
        print(root.name)