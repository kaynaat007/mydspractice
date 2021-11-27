class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def util(root, current_sum, target_sum):

    if root is None:
        return False

    if root is not None and root.left is None and root.right is None:
        return current_sum + root.val == target_sum

    current_sum += root.val
    return util(root.left, current_sum, target_sum) or util(root.right, current_sum, target_sum)


def hasPathSum(root: TreeNode, target: int) -> bool:

    if root is None:
        return False
    return util(root, 0, target)


# root = TreeNode(5)
# root.left = TreeNode(4)
# root.right = TreeNode(3)


root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(1)


# root = TreeNode(1)
# root.left = TreeNode(2)

print(hasPathSum(root, 19))



