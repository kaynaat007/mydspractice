import sys
import math

import pdb

from trees import bst


class Solution:

    ans = math.inf
    prev = None

    def is_leaf(self, root):

        return root and root.left is None and root.right is None

    def min_bst_util(self, root):

        if not root:
            return

        if self.is_leaf(root):
            if self.prev:
                self.ans = min(self.ans, abs(root.val - self.prev.val))
            self.prev = root
            return
        self.min_bst_util(root.left)
        if self.prev:
            self.ans = min(self.ans, abs(root.val - self.prev.val))
        self.prev = root

        self.min_bst_util(root.right)

    def minDiffInBST(self, root:  bst.Node) -> int:
        """
        """
        self.min_bst_util(root)
        return self.ans





b = bst.BST()
# b.init(4, 2, 6, 1, 3)

# b.init(4, 2)

# b.init(4, 2, 3)
# b.init(20, 10, 25)

# b.init(1, 0, 48, 12, 49)

b.init(90, 69, 49, 89, 52)

s = Solution()
print(s.minDiffInBST(b.root))
# b.inorder(b.root)

if __name__ == '__mian__':
    pass

