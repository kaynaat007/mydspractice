from trees.bst import inorder


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List

def invertTree(root: TreeNode) -> TreeNode:

    if root != None:

        left_root = invertTree(root.left)
        right_root = invertTree(root.right)
        root.left = right_root
        root.right = left_root
        return root

def stack_invertTree(root):
    pass



# root = TreeNode(4)
# root.left = TreeNode(2)
# root.right = TreeNode(7)
#
# root.left.left = TreeNode(1)
# root.left.right = TreeNode(3)
#
# root.right.left = TreeNode(6)
# root.right.right = TreeNode(9)

root = TreeNode(8)
root.left = TreeNode(10)
root.left.left = TreeNode(12)


new_root = invertTree(root)
inorder(root)