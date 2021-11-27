from ds.trees.bst_bst_to_greater_sum_tree import TreeNode


class Solution:

    total_sum = 0

    def util(self, root, l, r):

        if root is None:
            return

        if l <= root.val <= r:
            self.total_sum += root.val

        elif root.val < l:
            self.util(root.right, l, r)
        else:
            self.util(root.left, l, r)

    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:

        self.util(root, L, R)
        return self.total_sum



'''
[10,5,15,3,7,null,18]
7
15
'''