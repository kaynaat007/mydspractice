from trees import bst

class Solution:

    ans = 0

    def util(self, root, prev):

        if not root:
            return 0
        if prev is None:
            y = root
        elif prev.val != root.val:
            y = root
        else:
            y = prev

        l1 = self.util(root.left, y)
        l2 = self.util(root.right, y)

        if y and y.val == root.val:
            self.ans = max(self.ans, l1 + l2)
            return max(l1, l2) + 1
        else:
            return 0

    def longestUnivaluePath(self, root) -> int:

        self.util(root, None)
        return self.ans

