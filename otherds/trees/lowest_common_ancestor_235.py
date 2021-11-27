from trees import bst

"""
The lowest common ancestor is defined between two nodes p and q as 
the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself)
"""


class Solution:

    def lowestCommonAncestor(self, root , p,  q):

        if root.val == p.val or root.val == q.val or (p.val < root.val and q.val > root.val) or (q.val < root.val and p.val > root.val):
            return root
        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)


b = bst.BST()
b.init(10, 8, 20, 4, 9)

p = bst.Node(val=4)
q = bst.Node(val=9)

s = Solution()
print(s.lowestCommonAncestor(b.root, p, q).val)


