def nodeDepths(root, depth=0):
    if root is None:
        return 0
    sum = 0
    sum += depth
    sum = sum + nodeDepths(root.left, depth + 1) + \
        nodeDepths(root.right, depth + 1)
    return sum

# This is the class of the input binary tree.


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
