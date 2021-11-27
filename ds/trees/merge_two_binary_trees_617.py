from ds.trees.bst_bst_to_greater_sum_tree import TreeNode
'''
[1,3,2,5]
[2,1,3,null,4,null,7]
'''

class Solution:

    def util(self, t1, t2):

        if t1 is None and t2 is None:
            root = TreeNode()
            return root

        elif t1 is not None:
            root = TreeNode()
            root.val = t1.val
            root.left = t1.left
            return root

        elif t2 is not None:
            root = TreeNode()
            root.val = t2.val
            root.right = t2.right
            return root

        else:
            root = TreeNode()
            root.val = t1.val + t2.val
            root.left = self.util(t1.left, t2.left)
            root.right = self.util(t1.right, t2.right)
        return root


    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:

        return self.util(t1, t2)



