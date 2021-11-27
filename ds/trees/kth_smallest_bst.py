

from trees import bst

class Solution:

    c = 0
    ans = None

    def kth_smallest_util(self, root, k):

        if not root:
            return

        self.kth_smallest_util(root.left, k)
        self.c += 1
        if self.c == k:
            self.ans = root.val
            return
        self.kth_smallest_util(root.right, k)

    def kthSmallest(self, root, k) -> int:

        self.kth_smallest_util(root, k)
        return self.ans


b = bst.BST()

# b.init(10, 5, 6,  4, 15)
# k = 3


# b.init(3, 1, 2, 4)
# k = 1

b.init(5, 3, 4, 2, 1, 6)
k = 3

s = Solution()
print(s.kthSmallest(b.root, k))

