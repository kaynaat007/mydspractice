from typing import List

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def find_max(nums, i, j):

    max_index = i
    for k in range(i, j+1):
        if nums[k] > nums[max_index]:
            max_index = k
    return max_index


def construct_util(i, j, nums):

    if j < 0:
        return None

    if i > j:
        return None

    k = find_max(nums, i, j)

    root = TreeNode(val=nums[k])
    root.left = construct_util(i, k-1, nums)
    root.right = construct_util(k+1, j, nums)

    return root

def print_inorder(root):

    if root:
        print_inorder(root.left)
        print(root.val)
        print_inorder(root.right)


def constructMaximumBinaryTree(nums: List[int]) -> TreeNode:

    root = construct_util(0, len(nums)-1, nums)
    print('first method..')
    print_inorder(root)


def constructMaximumBinaryTreeV2(nums: List[int]) -> TreeNode:

    stack = []
    root = None
    for curr in nums:

        n = TreeNode(curr)
        if root and curr > root.val:
            root = n

        if root is None:
            root = n

        if stack and curr < stack[-1].val:
            top = stack[-1]
            top.right = n
            stack.append(n)
        else:
            prev = None
            while stack and stack[-1].val < curr:
                prev = stack.pop()
            if not stack:
                n.left = prev
            else:
                stack[-1].right = n
                n.left = prev
            stack.append(n)
    return root


nums = [3,2,1,6,0,5]
# nums = [1]
# nums = [1, 5, 3]
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nums = [10, 9, 8, 7]
nums = [6, 5, 4, 1, 9, 10]
constructMaximumBinaryTree(nums)
constructMaximumBinaryTreeV2(nums)
