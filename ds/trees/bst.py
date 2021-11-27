

class Node:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = None


class BST:

    def __init__(self):
        self.root = None

    def init(self, *args):
        for e in args:
            self.insert(Node(e))

    def to_string_inorder(self, root):
        if not root:
            return None
        return f'{self.to_string_inorder(root.left)}#{root.val}{self.to_string_inorder(root.right)}'

    def to_string_preorder(self, root):
        if not root:
            return None
        return f'#{root.val}{self.to_string_preorder(root.left)}{self.to_string_preorder(root.right)}'



    def insert(self, node):
        """
        insert a node into x
        """
        y = None
        T = self.root
        while T is not None:
            y = T
            if node.val < T.val:
                T = T.left
            else:
                T = T.right
        node.parent = y
        if y is None:
            self.root = node
        elif node.val < y.val:
            y.left = node
        else:
            y.right = node

    def inorder(self, root):

     if root is not None:

        self.inorder(root.left)
        print(root.val)
        self.inorder(root.right)


def inorder(root):

     if root is not None:

        inorder(root.left)
        print(root.val)
        inorder(root.right)