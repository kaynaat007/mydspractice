
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    depth_x = None
    depth_y = None
    parent_x = None
    parent_y = None

    def util(self, root, parent, depth, x, y):

        if root is None:
            return False

        v1 = self.util(root.left, root, depth + 1, x, y)
        v2 = self.util(root.right, root, depth + 1, x, y)

        if root.val == x:
            self.depth_x = depth
            self.parent_x = parent

        if root.val == y:
            self.depth_y = depth
            self.parent_y = parent

        if self.depth_x and self.depth_y and self.parent_x and self.parent_y:
            return self.depth_x == self.depth_y and self.parent_x != self.parent_y
        return v1 or v2

    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:

        return self.util(root, None, 0, x, y)




