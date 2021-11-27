

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def rob_util(root):

    if root is None:
        return 0, 0

    incl_left, exl_left= rob_util(root.left)
    incl_right, exl_right= rob_util(root.right)
    incl_root = root.val + exl_left + exl_right
    excl_root = max(incl_left, exl_left) + max(incl_right, exl_right)
    return incl_root, excl_root


def rob(root: TreeNode) -> int:

    a, b = rob_util(root)
    return max(a, b)

def recursive_rob(root):
    if root is None:
        return 0


root = TreeNode(14)
root.left = TreeNode(2)
root.right = TreeNode(3)

# root = TreeNode(3)
# root.left = TreeNode(4)
# root.right = TreeNode(5)
# root.left.left = TreeNode(1)
# root.left.right = TreeNode(3)
# root.right.right = TreeNode(1)

root = TreeNode(3)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(3)
root.right.right = TreeNode(1)

# root = TreeNode(4)
# root.left = TreeNode(1)
# root.left.left = TreeNode(2)
# root.left.left.left = TreeNode(3)


# root = TreeNode(2)
# root.left = TreeNode(1)
# root.right = TreeNode(3)
# root.left.right = TreeNode(4)


print(rob(root))