from typing import List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Path:

    def __init__(self):
        self.result = []
        self.stack = []

    def util(self, root, current_sum, target_sum):

        if root is None:
            return False

        if root is not None and root.left is None and root.right is None:
            val = current_sum + root.val == target_sum
            if val is True:
                self.stack.append(root.val)
                self.result.append(self.stack.copy())
                self.stack.pop()
            return val

        self.stack.append(root.val)
        current_sum += root.val
        self.util(root.left, current_sum, target_sum)
        self.util(root.right, current_sum, target_sum)
        self.stack.pop()


def dfs_with_local_params(root, current_sum, target_sum, stack, res):

    if root is None:
        return False

    if root is not None and root.left is None and root.right is None:
        val = current_sum + root.val == target_sum
        if val is True:
            stack = stack + [root.val]
            res.append(stack)
        return val

    current_sum += root.val
    dfs_with_local_params(root.left, current_sum, target_sum, stack + [root.val], res)
    dfs_with_local_params(root.right, current_sum, target_sum, stack + [root.val], res)


def is_leaf(node):

    return node.left is None and node.right is None


def bfs_queue(root, target):
    """
    q elements are [root, current_sum_till_this_node_in_tree, array holding the nodes so far till this node]
    """
    q = deque()
    q.append([root, root.val, [root.val]])
    res = []

    while q:
        current_node, current_sum_so_far, current_list = q.pop()
        if is_leaf(current_node) and current_sum_so_far == target:
            res.append(current_list)

        if current_node.left is not None:
            q.append([current_node.left, current_sum_so_far + current_node.left.val, current_list + [current_node.left.val]])

        if current_node.right is not None:
            q.append([current_node.right, current_sum_so_far + current_node.right.val,
                      current_list + [current_node.right.val]])
    return res


def findAllPathsWithSumTargetSum(root: TreeNode, target: int) -> List[List[int]]:

    if root is None:
        return []
    path = Path()
    path.util(root, 0, target)
    return path.result


def findAllPathsWithSumTargetSumWithDFSWithLocalParams(root: TreeNode, target: int) -> List[List[int]]:

    if root is None:
        return []
    res = []
    dfs_with_local_params(root, 0, target, [], res)
    return res



# root = TreeNode(5)
# root.left = TreeNode(4)
# root.right = TreeNode(3)

root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(6)
root.left.left.right = TreeNode(2)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.left = TreeNode(5)
root.right.right.right = TreeNode(1)

# print(findAllPathsWithSumTargetSum(root, 22))
# print(findAllPathsWithSumTargetSum(root, 26))
# print(findAllPathsWithSumTargetSumWithDFSWithLocalParams(root, 22))

print(bfs_queue(root, 26))


