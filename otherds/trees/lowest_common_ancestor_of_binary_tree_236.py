class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

    if root is None or root.val == p.val or root.val == q.val:
        return root

    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)

    if left is None:
        return right
    elif right is None:
        return left
    else:
        return root


def lowestCommonAncestorIterative(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

    if root is None or root.val == p.val or root.val == q.val:
        return root

    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)

    if left is None:
        return right
    elif right is None:
        return left
    else:
        return root

root = TreeNode(3)
root.left = TreeNode(5)
root.left.left = TreeNode(6)
root.right = TreeNode(1)
root.right.right = TreeNode(8)
root.right.left = TreeNode(0)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)

p = TreeNode(6)
q = TreeNode(8)

'''

  3
 / \
1   2
 
'''

# root = TreeNode(3)
# root.left = TreeNode(1)
# root.right = TreeNode(2)
#
# p = TreeNode(1)
# q = TreeNode(2)

print(lowestCommonAncestor(root, p, q).val)
