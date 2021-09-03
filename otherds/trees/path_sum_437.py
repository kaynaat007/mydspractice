from typing import List
from collections import deque, defaultdict


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
    """

    :param root: current node
    :param current_sum: current sum so far
    :param target_sum: target sum
    :param stack:  current elements in stack
    :param res: final result array
    :return:
    Modified to return from any point from root if we find the sum.
    """

    if root is None:
        return

    prev = stack.copy()

    if root.val + current_sum == target_sum:
        stack = stack + [root.val]
        res.append(stack)

    current_sum += root.val
    dfs_with_local_params(root.left, current_sum, target_sum, prev + [root.val], res)
    dfs_with_local_params(root.right, current_sum, target_sum, prev + [root.val], res)


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


class PathSumThree:

    def __init__(self):
        self.count = 0

    def helper(self, root, prefix_hash, current_sum, target):

        if root is None:
            return 0

        current_sum += root.val
        remaining_sum = current_sum - target
        if remaining_sum in prefix_hash and prefix_hash[remaining_sum] > 0:
            self.count += prefix_hash[remaining_sum]
        prefix_hash[current_sum] += 1
        self.helper(root.left, prefix_hash, current_sum, target)
        self.helper(root.right, prefix_hash, current_sum, target)
        prefix_hash[current_sum] -= 1

    def pathSumThree(self, root: TreeNode, target: int) -> int:

        if root is None:
            return 0
        prefix_hash = defaultdict(int)
        prefix_hash[0] = 1
        self.helper(root, prefix_hash, 0, target)
        return self.count


# root = TreeNode(5)
# root.left = TreeNode(1)
# root.right = TreeNode(3)
# root.right.right = TreeNode(3)

# print(pathSumThree(root, 6))

root = TreeNode(10)
root.left = TreeNode(5)
root.left.left = TreeNode(3)
root.left.left.left = TreeNode(3)
root.left.right = TreeNode(2)
root.left.right.right = TreeNode(1)
root.left.left.right = TreeNode(-2)
root.right = TreeNode(-3)
root.right.right = TreeNode(11)


root = TreeNode(1)
root.left = TreeNode(-2)
root.left.left = TreeNode(1)
root.left.left.left = TreeNode(-1)
root.left.right = TreeNode(3)
root.right = TreeNode(-3)
root.right.left = TreeNode(-2)


# print(pathSumThree(root, 8)) # 3
# print(pathSumThree(root, -3)) # 1
path = PathSumThree()

# root = TreeNode(3)
# root.left = TreeNode(5)
# root.left.left = TreeNode(1)
# root.left.left.left = TreeNode(-3)
#
#
#
# root = TreeNode(5)
# root.left = TreeNode(1)
# root.right = TreeNode(3)
# root.right.right = TreeNode(3)


print(path.pathSumThree(root, -1))










