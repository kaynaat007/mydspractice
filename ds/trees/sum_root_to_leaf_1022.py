
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    total_sum = 0

    def util(self, root, sum_at_current_stack):

        if root is None:
            return

        if root.val == 1:
            sum_at_current_stack = 2 * sum_at_current_stack + 1
        else:
            sum_at_current_stack = 2 * sum_at_current_stack

        if root.left is None and root.right is None:
            self.total_sum += sum_at_current_stack

        self.util(root.left, sum_at_current_stack)
        self.util(root.right, sum_at_current_stack)

    def sumRootToLeaf(self, root: TreeNode) -> int:
        if root is None:
            return 0

        self.util(root, 0)
