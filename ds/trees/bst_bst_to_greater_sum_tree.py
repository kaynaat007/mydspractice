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


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:

    sum_so_far = 0

    def bstToGst(self, root):


            if root.right:
                self.bstToGst(root.right)
            self.sum_so_far = self.sum_so_far + root.val
            root.val = self.sum_so_far
            if root.left:
                self.bstToGst(root.left)
            return root


b = BST()
b.init(4, 1, 6,  0, 2, 5, 7, 3, 8)
s = Solution()
s.bstToGst(b.root)
b.inorder(b.root)






