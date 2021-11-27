from trees import bst


class Solution:

    def is_identical(self, s, t):

        if s is None and t is None:
            return True

        if s is None or t is None:
            return False

        return s.val == t.val and self.is_identical(s.left, t.left) and self.is_identical(s.right, t.right)

    def isSubtree(self, s, t) -> bool:

        if t is None and s is None:
            return True
        elif t is None:
            return False
        elif s is None:
            return False

        if self.is_identical(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)


b1 = bst.BST()
b1.init(1, 1)

b2 = bst.BST()
b2.init(1)

s_inorder = b1.to_string_inorder(b1.root)
s_preorder = b1.to_string_preorder(b1.root)

t_inorder = b2.to_string_inorder(b2.root)
t_preorder = b2.to_string_preorder(b2.root)

print((t_inorder in s_inorder) and (t_preorder in s_preorder))


# s = Solution()
# print(s.isSubtree(b1.root, b2.root))
