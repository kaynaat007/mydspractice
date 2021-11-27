from trees import bst


class Solution:
    diameter = 0

    def diameter_util(self, root):

        if not root:
            return 0
        l1 = self.diameter_util(root.left)
        l2 = self.diameter_util(root.right)
        self.diameter = max(self.diameter, l1 + l2)
        return max(l1, l2) + 1

    def diameterOfBinaryTree(self, root: bst.Node) -> int:

        self.diameter_util(root)
        return self.diameter


b = bst.BST()
b.init(20, 10, 15, 18, 8, 9, 4, 7)

s = Solution()
print(s.diameterOfBinaryTree(b.root))


