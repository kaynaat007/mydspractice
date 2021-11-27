# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


MOD = pow(10, 9) + 7


def get_total_sum(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return root.val
    left_sum = get_total_sum(root.left)
    right_sum = get_total_sum(root.right)
    return left_sum + right_sum + root.val


def util(root, total_sum, ans):
    # solve base cases
    if root is None:
        return 0

    if root.left is None and root.right is None:
        return root.val

    left_sum = util(root.left, total_sum, ans)
    right_sum = util(root.right, total_sum, ans)
    including_root_left_sum = total_sum - left_sum
    left_product = ((left_sum % MOD) * (including_root_left_sum % MOD)) % MOD
    including_root_right_sum = total_sum - right_sum
    right_product = ((including_root_right_sum % MOD) * (right_sum % MOD )) % MOD
    ans[0] = max(ans[0], max(left_product, right_product))
    return left_sum + right_sum + root.val


def maxProduct(root: TreeNode) -> int:
    total_sum = get_total_sum(root)
    print('total sum: {}'.format(total_sum))
    ans = [0]
    util(root, total_sum, ans)
    return ans[0]


root = TreeNode(val=10)
root.left = TreeNode(6)
root.right = TreeNode(5)

root = TreeNode(10)
root.left = TreeNode(6)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)

root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
root.right.right = TreeNode(4)
root.right.right.left = TreeNode(5)
root.right.right.right = TreeNode(6)



print(maxProduct(root))