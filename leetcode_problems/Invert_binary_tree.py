from dtos import Node

def invert(node):

    if (node == None):
        return
    else:

        temp = node
        invert(node.left)
        invert(node.right)

        temp = node.left
        node.left = node.right
        node.right = temp
